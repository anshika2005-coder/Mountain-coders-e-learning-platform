from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Course, Category, Lesson, Enrollment, LessonProgress, Quiz, Question, Announcement
from django.utils import timezone
import json

def home(request):
    courses = Course.objects.all().select_related('category', 'instructor')[:6]
    categories = Category.objects.all()
    announcements = Announcement.objects.filter(is_active=True).order_by('-created_at')[:3]
    stats = {
        'courses': Course.objects.count(),
        'students': Enrollment.objects.values('student').distinct().count(),
        'lessons': Lesson.objects.count(),
    }
    return render(request, 'courses/home.html', {
        'courses': courses, 'categories': categories,
        'announcements': announcements, 'stats': stats
    })

def course_list(request):
    courses = Course.objects.all().select_related('category', 'instructor')
    categories = Category.objects.all()
    q = request.GET.get('q', '')
    cat = request.GET.get('category', '')
    level = request.GET.get('level', '')
    if q:
        courses = courses.filter(Q(title__icontains=q) | Q(description__icontains=q))
    if cat:
        courses = courses.filter(category__id=cat)
    if level:
        courses = courses.filter(level=level)
    return render(request, 'courses/course_list.html', {
        'courses': courses, 'categories': categories,
        'selected_cat': cat, 'selected_level': level, 'query': q
    })

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    lessons = course.lessons.all()
    is_enrolled = False
    enrollment = None
    if request.user.is_authenticated:
        enrollment = Enrollment.objects.filter(student=request.user, course=course).first()
        is_enrolled = enrollment is not None
    return render(request, 'courses/course_detail.html', {
        'course': course, 'lessons': lessons,
        'is_enrolled': is_enrolled, 'enrollment': enrollment
    })

@login_required
def enroll_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    enrollment, created = Enrollment.objects.get_or_create(student=request.user, course=course)
    if created:
        messages.success(request, f'Successfully enrolled in {course.title}!')
    else:
        messages.info(request, 'You are already enrolled.')
    return redirect('course_detail', pk=pk)

@login_required
def lesson_detail(request, course_pk, lesson_pk):
    course = get_object_or_404(Course, pk=course_pk)
    lesson = get_object_or_404(Lesson, pk=lesson_pk, course=course)

    # If not enrolled, auto-enroll and redirect back so progress works correctly
    enrollment, created = Enrollment.objects.get_or_create(
        student=request.user, course=course
    )
    if created:
        messages.success(request, f'You have been enrolled in {course.title}!')

    lessons = course.lessons.all()
    progress_obj, _ = LessonProgress.objects.get_or_create(student=request.user, lesson=lesson)
    
    # Mark as complete if POST
    if request.method == 'POST':
        progress_obj.completed = True
        progress_obj.completed_at = timezone.now()
        progress_obj.save()
        # Update enrollment progress
        total = lessons.count()
        done = LessonProgress.objects.filter(student=request.user, lesson__course=course, completed=True).count()
        enrollment.progress = int((done / total) * 100) if total else 0
        enrollment.save()
        messages.success(request, 'Lesson marked as complete!')
        return redirect('lesson_detail', course_pk=course_pk, lesson_pk=lesson_pk)
    
    completed_ids = LessonProgress.objects.filter(
        student=request.user, lesson__course=course, completed=True
    ).values_list('lesson_id', flat=True)
    
    return render(request, 'courses/lesson_detail.html', {
        'course': course, 'lesson': lesson, 'lessons': lessons,
        'progress_obj': progress_obj, 'completed_ids': list(completed_ids),
        'enrollment': enrollment
    })

@login_required
def my_courses(request):
    enrollments = Enrollment.objects.filter(student=request.user).select_related('course', 'course__category')
    return render(request, 'courses/my_courses.html', {'enrollments': enrollments})

@login_required
def quiz_view(request, quiz_pk):
    quiz = get_object_or_404(Quiz, pk=quiz_pk)
    questions = quiz.questions.all()
    if request.method == 'POST':
        score = 0
        results = []
        for q in questions:
            ans = request.POST.get(f'q_{q.id}', '')
            correct = ans == q.correct_option
            if correct:
                score += 1
            results.append({'question': q, 'answer': ans, 'correct': correct})
        pct = int((score / len(questions)) * 100) if questions else 0
        return render(request, 'courses/quiz_result.html', {
            'quiz': quiz, 'results': results, 'score': score,
            'total': len(questions), 'percentage': pct
        })
    return render(request, 'courses/quiz.html', {'quiz': quiz, 'questions': questions})
