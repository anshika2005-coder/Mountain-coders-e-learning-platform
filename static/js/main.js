// Mountain Coders - Main JS

document.addEventListener('DOMContentLoaded', () => {

  // Hamburger menu
  const hamburger = document.querySelector('.hamburger');
  const navLinks = document.querySelector('.nav-links');
  if (hamburger && navLinks) {
    hamburger.addEventListener('click', () => {
      navLinks.classList.toggle('open');
    });
  }

  // Auto-dismiss alerts
  document.querySelectorAll('.alert').forEach(alert => {
    setTimeout(() => {
      alert.style.opacity = '0';
      alert.style.transform = 'translateY(-8px)';
      alert.style.transition = 'all 0.4s';
      setTimeout(() => alert.remove(), 400);
    }, 4000);
  });

  // Animate stats counter
  document.querySelectorAll('.stat-num').forEach(el => {
    const target = parseInt(el.textContent.replace(/\D/g, ''), 10);
    if (isNaN(target)) return;
    let current = 0;
    const duration = 1400;
    const step = Math.ceil(target / (duration / 16));
    const timer = setInterval(() => {
      current = Math.min(current + step, target);
      el.textContent = current.toLocaleString();
      if (current >= target) clearInterval(timer);
    }, 16);
  });

  // Offline status banner
  function updateOfflineStatus() {
    const indicator = document.querySelector('.offline-dot');
    const label = document.querySelector('.offline-label');
    if (!indicator) return;
    if (!navigator.onLine) {
      indicator.style.background = '#e9c46a';
      if (label) label.textContent = 'Offline Mode';
    }
  }
  updateOfflineStatus();
  window.addEventListener('offline', updateOfflineStatus);
  window.addEventListener('online', () => {
    const indicator = document.querySelector('.offline-dot');
    if (indicator) indicator.style.background = '#52b788';
  });

  // Course search live filter
  const searchInput = document.getElementById('course-search');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      const q = e.target.value.toLowerCase();
      document.querySelectorAll('.course-card').forEach(card => {
        const title = card.querySelector('.course-title')?.textContent.toLowerCase() || '';
        const desc = card.querySelector('.course-desc')?.textContent.toLowerCase() || '';
        card.closest('.course-card-wrap')
          ? card.closest('.course-card-wrap').style.display = (title.includes(q) || desc.includes(q)) ? '' : 'none'
          : card.style.display = (title.includes(q) || desc.includes(q)) ? '' : 'none';
      });
    });
  }

  // Smooth reveal on scroll
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.course-card, .category-chips .chip, .announcement-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    observer.observe(el);
  });

  // Quiz form validation
  const quizForm = document.getElementById('quiz-form');
  if (quizForm) {
    quizForm.addEventListener('submit', (e) => {
      const questions = quizForm.querySelectorAll('.question-block');
      let allAnswered = true;
      questions.forEach(q => {
        const answered = q.querySelector('input[type="radio"]:checked');
        if (!answered) {
          allAnswered = false;
          q.style.border = '2px solid #e63946';
          q.style.borderRadius = '12px';
        } else {
          q.style.border = '';
        }
      });
      if (!allAnswered) {
        e.preventDefault();
        alert('Please answer all questions before submitting.');
      }
    });
  }

  // PDF viewer fallback
  document.querySelectorAll('.pdf-link').forEach(link => {
    link.addEventListener('click', (e) => {
      if (!navigator.onLine) {
        e.preventDefault();
        alert('You are offline. This PDF should be available in your downloads if you previously downloaded it.');
      }
    });
  });

  // Progress bar animation
  document.querySelectorAll('.progress-bar').forEach(bar => {
    const pct = bar.getAttribute('data-pct') || '0';
    bar.style.width = '0%';
    requestAnimationFrame(() => {
      setTimeout(() => { bar.style.width = pct + '%'; }, 200);
    });
  });
});
