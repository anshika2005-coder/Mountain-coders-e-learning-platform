from django.contrib import admin
from .models import Category, Course, Lesson, Enrollment, Quiz, Question, Announcement, LessonProgress

admin.site.register(Category)
admin.site.register(Lesson)
admin.site.register(Enrollment)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Announcement)
admin.site.register(LessonProgress)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'level', 'instructor', 'is_offline_available', 'created_at']
    list_filter = ['level', 'category', 'is_offline_available']
    search_fields = ['title', 'description']
