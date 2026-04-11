/* ============================================
   Epoch — Main Application JavaScript
   ============================================ */

/* ---------- Theme Toggle ---------- */
(function() {
  var STORAGE_KEY = 'epoch-theme';
  var html = document.documentElement;

  function getPreferred() {
    var stored = localStorage.getItem(STORAGE_KEY);
    if (stored) return stored;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  var SUN = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg> Light';
  var MOON = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg> Dark';

  function applyTheme(theme) {
    html.classList.add('no-transition');
    html.setAttribute('data-theme', theme);
    localStorage.setItem(STORAGE_KEY, theme);
    setTimeout(function() { html.classList.remove('no-transition'); }, 20);
    var btn = document.getElementById('theme-toggle');
    if (btn) {
      btn.innerHTML = theme === 'dark' ? SUN : MOON;
      btn.setAttribute('aria-label', theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
    }
  }

  applyTheme(getPreferred());

  document.addEventListener('DOMContentLoaded', function() {
    var btn = document.getElementById('theme-toggle');
    if (btn) {
      btn.addEventListener('click', function() {
        var current = html.getAttribute('data-theme') || 'light';
        applyTheme(current === 'dark' ? 'light' : 'dark');
      });
    }
  });

  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {
    if (!localStorage.getItem(STORAGE_KEY)) applyTheme(e.matches ? 'dark' : 'light');
  });
})();

(function () {
  'use strict';

  /* ------------------------------------------------
     Toast / Alert Notifications
     ------------------------------------------------ */
  function getToastContainer() {
    let container = document.querySelector('.toast-container');
    if (!container) {
      container = document.createElement('div');
      container.className = 'toast-container';
      document.body.appendChild(container);
    }
    return container;
  }

  /**
   * Show a toast notification in the top-right corner.
   * @param {string} message - The message to display.
   * @param {string} [type='info'] - One of 'success', 'error', 'warning', 'info'.
   * @param {number} [duration=3000] - Auto-dismiss time in ms.
   */
  function showAlert(message, type, duration) {
    type = type || 'info';
    duration = duration || 3000;

    var container = getToastContainer();
    var toast = document.createElement('div');
    toast.className = 'toast toast-' + type;
    toast.textContent = message;
    container.appendChild(toast);

    var timer = setTimeout(function () {
      dismissToast(toast);
    }, duration);

    toast.addEventListener('click', function () {
      clearTimeout(timer);
      dismissToast(toast);
    });
  }

  function dismissToast(toast) {
    if (toast.classList.contains('removing')) return;
    toast.classList.add('removing');
    toast.addEventListener('animationend', function () {
      if (toast.parentNode) toast.parentNode.removeChild(toast);
    });
  }

  /* ------------------------------------------------
     Password Toggle
     ------------------------------------------------ */
  /**
   * Toggle visibility of a password input.
   * @param {string} inputId - The id of the password input element.
   */
  function togglePassword(inputId) {
    var input = document.getElementById(inputId);
    if (!input) return;
    var isHidden = input.type === 'password';
    input.type = isHidden ? 'text' : 'password';

    // Update toggle button SVG icon
    var wrapper = input.closest('.input-wrapper');
    if (wrapper) {
      var btn = wrapper.querySelector('.toggle-password');
      if (btn) {
        btn.setAttribute('aria-label', isHidden ? 'Hide password' : 'Show password');
        // Swap eye icon: open eye vs crossed eye
        if (isHidden) {
          btn.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94"/><path d="M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19"/><line x1="1" y1="1" x2="23" y2="23"/></svg>';
        } else {
          btn.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>';
        }
      }
    }
  }
  // Expose globally so inline onclick="togglePassword()" works
  window.togglePassword = togglePassword;

  /* ------------------------------------------------
     Quiz Functionality
     ------------------------------------------------ */
  var quizAnswers = {};

  /**
   * Handle quiz option selection.
   * @param {HTMLElement} element - The clicked option element.
   * @param {number} questionIdx - The zero-based question index.
   */
  function selectQuizOption(element, questionIdx) {
    // Clear previous selection for this question
    var parent = element.closest('.quiz-options');
    if (parent) {
      var options = parent.querySelectorAll('.quiz-option');
      for (var i = 0; i < options.length; i++) {
        options[i].classList.remove('selected');
      }
    }
    element.classList.add('selected');

    // Store the answer value
    var radio = element.querySelector('input[type="radio"]');
    if (radio) {
      radio.checked = true;
      quizAnswers[questionIdx] = radio.value;
    } else {
      quizAnswers[questionIdx] = element.dataset.value || element.textContent.trim();
    }
  }

  /**
   * Submit quiz answers to the server.
   * Collects all stored answers and POSTs them.
   */
  function submitQuiz() {
    var quizContainer = document.querySelector('.quiz-container');
    if (!quizContainer) {
      showAlert('No quiz found on this page.', 'error');
      return;
    }

    var topicId = quizContainer.dataset.topicId || '';
    var questions = quizContainer.querySelectorAll('.quiz-question');
    var answers = [];

    for (var i = 0; i < questions.length; i++) {
      var qId = questions[i].dataset.questionId || String(i);
      answers.push({
        question_id: qId,
        answer: quizAnswers[i] || null
      });
    }

    // Check that all questions are answered
    var unanswered = answers.filter(function (a) { return a.answer === null; });
    if (unanswered.length > 0) {
      showAlert('Please answer all ' + questions.length + ' questions before submitting.', 'warning');
      return;
    }

    var payload = {
      topic_id: topicId,
      answers: answers
    };

    fetch('/api/quiz/submit', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')
      },
      body: JSON.stringify(payload)
    })
      .then(function (res) {
        if (!res.ok) throw new Error('Server responded with status ' + res.status);
        return res.json();
      })
      .then(function (data) {
        renderQuizResults(data, quizContainer);
        showAlert('Quiz submitted successfully!', 'success');
      })
      .catch(function (err) {
        console.error('Quiz submit error:', err);
        showAlert('Failed to submit quiz. Please try again.', 'error');
      });
  }

  function renderQuizResults(data, container) {
    var score = data.score || 0;
    var total = data.total || 0;
    var results = data.results || [];

    // Mark each option correct/wrong
    var questions = container.querySelectorAll('.quiz-question');
    for (var i = 0; i < results.length && i < questions.length; i++) {
      var options = questions[i].querySelectorAll('.quiz-option');
      for (var j = 0; j < options.length; j++) {
        var radio = options[j].querySelector('input[type="radio"]');
        var val = radio ? radio.value : (options[j].dataset.value || '');
        options[j].classList.remove('selected');
        options[j].style.pointerEvents = 'none';

        if (val === results[i].correct_answer) {
          options[j].classList.add('correct');
        } else if (val === results[i].user_answer && val !== results[i].correct_answer) {
          options[j].classList.add('wrong');
        }
      }
    }

    // Show summary
    var resultsDiv = document.createElement('div');
    resultsDiv.className = 'quiz-results mt-3';
    resultsDiv.innerHTML =
      '<div class="score">' + score + '/' + total + '</div>' +
      '<p class="text-secondary mt-1">You scored ' + Math.round((score / total) * 100) + '%</p>' +
      '<button class="btn btn-primary mt-3" onclick="location.reload()">Try Again</button>';
    container.appendChild(resultsDiv);

    // Hide submit button
    var submitBtn = container.querySelector('[data-action="submit-quiz"]');
    if (submitBtn) submitBtn.classList.add('hidden');
  }

  /**
   * Start a quiz by fetching questions from the API.
   * @param {string|number} topicId - The topic identifier.
   */
  function startQuiz(topicId) {
    quizAnswers = {};

    var container = document.querySelector('.quiz-container');
    if (!container) {
      container = document.createElement('div');
      container.className = 'quiz-container';
      var main = document.querySelector('.container') || document.body;
      main.appendChild(container);
    }

    container.dataset.topicId = topicId;
    container.innerHTML = '<p class="text-secondary text-center mt-4">Loading quiz...</p>';

    fetch('/api/quiz/generate?topic_id=' + encodeURIComponent(topicId) + '&count=5')
      .then(function (res) {
        if (!res.ok) throw new Error('Status ' + res.status);
        return res.json();
      })
      .then(function (data) {
        renderQuiz(data, container);
      })
      .catch(function (err) {
        console.error('Quiz load error:', err);
        container.innerHTML = '';
        showAlert('Failed to load quiz. Please try again.', 'error');
      });
  }

  function renderQuiz(data, container) {
    var questions = data.questions || data || [];
    if (!questions.length) {
      container.innerHTML = '<p class="text-secondary text-center">No questions available.</p>';
      return;
    }

    var html = '';
    var markers = ['A', 'B', 'C', 'D', 'E', 'F'];

    for (var q = 0; q < questions.length; q++) {
      var question = questions[q];
      html += '<div class="quiz-question" data-question-id="' + (question.id || q) + '">';
      html += '<div class="question-number">Question ' + (q + 1) + ' of ' + questions.length + '</div>';
      html += '<div class="question-text">' + escapeHtml(question.question || question.text) + '</div>';
      html += '<div class="quiz-options">';

      var options = question.options || [];
      for (var o = 0; o < options.length; o++) {
        html += '<div class="quiz-option" onclick="MindMatrix.selectQuizOption(this, ' + q + ')" data-value="' + escapeHtml(options[o]) + '">';
        html += '<input type="radio" name="q' + q + '" value="' + escapeHtml(options[o]) + '">';
        html += '<span class="option-marker">' + (markers[o] || o + 1) + '</span>';
        html += '<span class="option-text">' + escapeHtml(options[o]) + '</span>';
        html += '</div>';
      }

      html += '</div></div>';
    }

    html += '<div class="text-center mt-3">';
    html += '<button class="btn btn-primary btn-lg" data-action="submit-quiz" onclick="MindMatrix.submitQuiz()">Submit Answers</button>';
    html += '</div>';

    container.innerHTML = html;
  }

  /* ------------------------------------------------
     Progress Ring
     ------------------------------------------------ */
  /**
   * Update a circular progress ring element.
   * @param {HTMLElement} element - The .progress-ring element.
   * @param {number} percentage - 0–100.
   */
  function updateProgressRing(element, percentage) {
    if (!element) return;
    percentage = Math.max(0, Math.min(100, percentage));
    element.style.setProperty('--progress', percentage + '%');

    var valueEl = element.querySelector('.progress-value');
    if (valueEl) {
      valueEl.textContent = Math.round(percentage) + '%';
    }
  }

  /* ------------------------------------------------
     Growth Chart
     ------------------------------------------------ */
  /**
   * Fetch growth data and render a chart.
   */
  function loadGrowthChart() {
    var container = document.querySelector('.growth-chart-container');
    if (!container) return;

    fetch('/api/growth')
      .then(function (res) {
        if (!res.ok) throw new Error('Status ' + res.status);
        return res.json();
      })
      .then(function (data) {
        renderGrowthChart(data, container);
      })
      .catch(function (err) {
        console.error('Growth chart error:', err);
        container.innerHTML = '<p class="text-secondary text-center">Unable to load growth data.</p>';
      });
  }

  function renderGrowthChart(data, container) {
    var labels = data.labels || [];
    var values = data.values || [];

    // If Chart.js is available, use it; otherwise render a simple bar representation
    if (typeof Chart !== 'undefined') {
      container.innerHTML = '<canvas id="growthCanvas"></canvas>';
      var ctx = document.getElementById('growthCanvas').getContext('2d');
      new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [{
            label: 'Progress',
            data: values,
            borderColor: '#3b82f6',
            backgroundColor: 'rgba(59, 130, 246, 0.1)',
            fill: true,
            tension: 0.4,
            pointBackgroundColor: '#3b82f6',
            pointBorderColor: '#fff',
            pointRadius: 4
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: {
              grid: { color: 'rgba(34,34,51,0.5)' },
              ticks: { color: '#8888aa' }
            },
            y: {
              grid: { color: 'rgba(34,34,51,0.5)' },
              ticks: { color: '#8888aa' },
              beginAtZero: true
            }
          },
          plugins: {
            legend: { labels: { color: '#ffffff' } }
          }
        }
      });
    } else {
      // Simple fallback bar chart
      var maxVal = Math.max.apply(null, values.concat([1]));
      var html = '<div style="display:flex;align-items:flex-end;gap:8px;height:220px;padding:16px 0;">';
      for (var i = 0; i < values.length; i++) {
        var h = Math.round((values[i] / maxVal) * 180);
        html += '<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:6px;">';
        html += '<span style="font-size:0.7rem;color:#8888aa;">' + values[i] + '</span>';
        html += '<div style="width:100%;height:' + h + 'px;background:linear-gradient(180deg,#2A6AD4,#1E54B7);border-radius:4px 4px 0 0;"></div>';
        html += '<span style="font-size:0.65rem;color:#8888aa;white-space:nowrap;">' + (labels[i] || '') + '</span>';
        html += '</div>';
      }
      html += '</div>';
      container.innerHTML = html;
    }
  }

  /* ------------------------------------------------
     Navigation
     ------------------------------------------------ */
  /**
   * Navigate to a URL with an optional smooth transition.
   * @param {string} url - The target URL.
   */
  function navigateTo(url) {
    if (!url) return;
    // Apply a fade-out if the View Transitions API is available
    if (document.startViewTransition) {
      document.startViewTransition(function () {
        window.location.href = url;
      });
    } else {
      document.body.style.opacity = '0';
      document.body.style.transition = 'opacity 0.2s ease';
      setTimeout(function () {
        window.location.href = url;
      }, 200);
    }
  }

  /* ------------------------------------------------
     Modal / Confirm Action
     ------------------------------------------------ */
  /**
   * Show a confirmation modal.
   * @param {string} message - Confirmation message.
   * @param {function} callback - Called with true (confirm) or false (cancel).
   */
  function confirmAction(message, callback) {
    // Remove any existing modal
    var existing = document.querySelector('.modal-overlay.confirm-modal');
    if (existing) existing.remove();

    var overlay = document.createElement('div');
    overlay.className = 'modal-overlay confirm-modal';
    overlay.innerHTML =
      '<div class="modal">' +
      '  <h3>Confirm</h3>' +
      '  <p>' + escapeHtml(message) + '</p>' +
      '  <div class="modal-actions">' +
      '    <button class="btn btn-secondary" data-action="cancel">Cancel</button>' +
      '    <button class="btn btn-primary" data-action="confirm">Confirm</button>' +
      '  </div>' +
      '</div>';

    document.body.appendChild(overlay);

    // Trigger reflow then activate
    requestAnimationFrame(function () {
      overlay.classList.add('active');
    });

    function close(result) {
      overlay.classList.remove('active');
      setTimeout(function () {
        if (overlay.parentNode) overlay.parentNode.removeChild(overlay);
      }, 300);
      if (typeof callback === 'function') callback(result);
    }

    overlay.querySelector('[data-action="cancel"]').addEventListener('click', function () { close(false); });
    overlay.querySelector('[data-action="confirm"]').addEventListener('click', function () { close(true); });
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) close(false);
    });
  }

  /* ------------------------------------------------
     Cookie Helpers
     ------------------------------------------------ */
  /**
   * Get a cookie value by name.
   * @param {string} name
   * @returns {string|null}
   */
  function getCookie(name) {
    var match = document.cookie.match(new RegExp('(^|;\\s*)' + name + '=([^;]*)'));
    return match ? decodeURIComponent(match[2]) : null;
  }

  /**
   * Set a cookie.
   * @param {string} name
   * @param {string} value
   * @param {number} [days=30]
   */
  function setCookie(name, value, days) {
    days = days || 30;
    var expires = new Date(Date.now() + days * 864e5).toUTCString();
    document.cookie = name + '=' + encodeURIComponent(value) + ';expires=' + expires + ';path=/;SameSite=Lax';
  }

  /* ------------------------------------------------
     Form Validation Helpers
     ------------------------------------------------ */
  function validateEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  function validatePassword(password) {
    // At least 8 chars, one letter, one number
    return password.length >= 8 && /[a-zA-Z]/.test(password) && /\d/.test(password);
  }

  /**
   * Validate a login form. Returns an object { valid, errors }.
   * @param {HTMLFormElement} form
   */
  function validateLoginForm(form) {
    var errors = {};
    var email = (form.querySelector('[name="email"]') || {}).value || '';
    var password = (form.querySelector('[name="password"]') || {}).value || '';

    if (!email.trim()) {
      errors.email = 'Email is required.';
    } else if (!validateEmail(email)) {
      errors.email = 'Please enter a valid email address.';
    }

    if (!password) {
      errors.password = 'Password is required.';
    }

    return { valid: Object.keys(errors).length === 0, errors: errors };
  }

  /**
   * Validate a signup form. Returns an object { valid, errors }.
   * @param {HTMLFormElement} form
   */
  function validateSignupForm(form) {
    var errors = {};
    var name = (form.querySelector('[name="name"]') || {}).value || '';
    var email = (form.querySelector('[name="email"]') || {}).value || '';
    var password = (form.querySelector('[name="password"]') || {}).value || '';
    var confirm = (form.querySelector('[name="confirm_password"]') || form.querySelector('[name="password_confirm"]') || {}).value || '';

    if (!name.trim()) {
      errors.name = 'Name is required.';
    }

    if (!email.trim()) {
      errors.email = 'Email is required.';
    } else if (!validateEmail(email)) {
      errors.email = 'Please enter a valid email address.';
    }

    if (!password) {
      errors.password = 'Password is required.';
    } else if (!validatePassword(password)) {
      errors.password = 'Password must be at least 8 characters with letters and numbers.';
    }

    if (password !== confirm) {
      errors.confirm_password = 'Passwords do not match.';
    }

    return { valid: Object.keys(errors).length === 0, errors: errors };
  }

  /**
   * Display validation errors below their respective fields.
   * @param {HTMLFormElement} form
   * @param {Object} errors - Keyed by field name.
   */
  function showFormErrors(form, errors) {
    // Clear existing errors
    var existing = form.querySelectorAll('.form-error');
    for (var i = 0; i < existing.length; i++) {
      existing[i].remove();
    }

    var keys = Object.keys(errors);
    for (var k = 0; k < keys.length; k++) {
      var field = form.querySelector('[name="' + keys[k] + '"]');
      if (field) {
        var group = field.closest('.form-group') || field.parentNode;
        var errEl = document.createElement('div');
        errEl.className = 'form-error';
        errEl.textContent = errors[keys[k]];
        group.appendChild(errEl);
      }
    }
  }

  /* ------------------------------------------------
     Utility
     ------------------------------------------------ */
  function escapeHtml(str) {
    var div = document.createElement('div');
    div.appendChild(document.createTextNode(str));
    return div.innerHTML;
  }

  /* ------------------------------------------------
     Data-Attribute Driven Initialization
     ------------------------------------------------ */
  function initComponents() {
    // Epoch session tracking for Quote 1
    var sessions = parseInt(localStorage.getItem('epoch-sessions') || '0') + 1;
    localStorage.setItem('epoch-sessions', sessions.toString());
    var isReturning = sessions > 1;
    var dwQuote = document.querySelector('.dw-quote');
    if (dwQuote && !isReturning) {
      dwQuote.textContent = 'Your first epoch begins now.';
      dwQuote.style.fontStyle = 'normal';
      dwQuote.style.color = 'var(--accent)';
    }

    // Accordion
    var accordionHeaders = document.querySelectorAll('.accordion-header');
    for (var i = 0; i < accordionHeaders.length; i++) {
      (function (header) {
        header.addEventListener('click', function () {
          var item = header.closest('.accordion-item');
          if (item) item.classList.toggle('open');
        });
      })(accordionHeaders[i]);
    }

    // Toggle password buttons
    var toggleBtns = document.querySelectorAll('[data-toggle-password]');
    for (var t = 0; t < toggleBtns.length; t++) {
      (function (btn) {
        btn.addEventListener('click', function () {
          togglePassword(btn.dataset.togglePassword);
        });
      })(toggleBtns[t]);
    }

    // Quiz option clicks (data-driven)
    var quizOptions = document.querySelectorAll('[data-quiz-option]');
    for (var q = 0; q < quizOptions.length; q++) {
      (function (opt) {
        opt.addEventListener('click', function () {
          var qIdx = parseInt(opt.dataset.quizOption, 10);
          selectQuizOption(opt, qIdx);
        });
      })(quizOptions[q]);
    }

    // Progress rings
    var rings = document.querySelectorAll('.progress-ring[data-progress]');
    for (var r = 0; r < rings.length; r++) {
      updateProgressRing(rings[r], parseFloat(rings[r].dataset.progress) || 0);
    }

    // Start quiz buttons
    var quizStarts = document.querySelectorAll('[data-start-quiz]');
    for (var s = 0; s < quizStarts.length; s++) {
      (function (btn) {
        btn.addEventListener('click', function () {
          startQuiz(btn.dataset.startQuiz);
        });
      })(quizStarts[s]);
    }

    // Auth form validation
    var loginForm = document.querySelector('[data-form="login"]');
    if (loginForm) {
      loginForm.addEventListener('submit', function (e) {
        var result = validateLoginForm(loginForm);
        if (!result.valid) {
          e.preventDefault();
          showFormErrors(loginForm, result.errors);
        }
      });
    }

    var signupForm = document.querySelector('[data-form="signup"]');
    if (signupForm) {
      signupForm.addEventListener('submit', function (e) {
        var result = validateSignupForm(signupForm);
        if (!result.valid) {
          e.preventDefault();
          showFormErrors(signupForm, result.errors);
        }
      });
    }

    // Confirm action buttons
    var confirmBtns = document.querySelectorAll('[data-confirm]');
    for (var c = 0; c < confirmBtns.length; c++) {
      (function (btn) {
        btn.addEventListener('click', function (e) {
          e.preventDefault();
          var msg = btn.dataset.confirm || 'Are you sure?';
          var href = btn.getAttribute('href') || btn.dataset.href;
          confirmAction(msg, function (confirmed) {
            if (confirmed && href) {
              window.location.href = href;
            }
          });
        });
      })(confirmBtns[c]);
    }

    // Mobile nav toggle
    var mobileToggle = document.querySelector('.mobile-toggle');
    if (mobileToggle) {
      mobileToggle.addEventListener('click', function () {
        var navbar = document.querySelector('.navbar');
        if (navbar) navbar.classList.toggle('nav-open');
      });
    }

    // Growth chart auto-load
    if (document.querySelector('.growth-chart-container[data-auto-load]')) {
      loadGrowthChart();
    }

    // Page fade-in
    document.body.style.opacity = '1';
    document.body.style.transition = 'opacity 0.3s ease';

    // ── Scroll Reveal via IntersectionObserver ──
    if ('IntersectionObserver' in window) {
      var revealElements = document.querySelectorAll('.reveal');
      if (revealElements.length) {
        var revealObserver = new IntersectionObserver(function(entries) {
          entries.forEach(function(entry) {
            if (entry.isIntersecting) {
              entry.target.classList.add('visible');
              revealObserver.unobserve(entry.target);
            }
          });
        }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });
        revealElements.forEach(function(el) { revealObserver.observe(el); });
      }
    } else {
      // Fallback: show everything
      document.querySelectorAll('.reveal').forEach(function(el) { el.classList.add('visible'); });
    }

    // ── Count-Up Animation for stat numbers ──
    var countElements = document.querySelectorAll('[data-count]');
    if (countElements.length) {
      var countObserver = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            var el = entry.target;
            var target = parseInt(el.dataset.count, 10);
            var duration = 1200;
            var start = performance.now();
            function tick(now) {
              var elapsed = now - start;
              var progress = Math.min(elapsed / duration, 1);
              // Ease-out expo
              var eased = 1 - Math.pow(1 - progress, 3);
              el.textContent = Math.round(target * eased);
              if (progress < 1) requestAnimationFrame(tick);
            }
            requestAnimationFrame(tick);
            countObserver.unobserve(el);
          }
        });
      }, { threshold: 0.5 });
      countElements.forEach(function(el) { countObserver.observe(el); });
    }

    // ── Button Ripple Effect ──
    document.querySelectorAll('.btn-primary, .btn-cobalt').forEach(function(btn) {
      btn.addEventListener('click', function(e) {
        var rect = btn.getBoundingClientRect();
        var ripple = document.createElement('span');
        ripple.className = 'btn-ripple';
        ripple.style.left = (e.clientX - rect.left) + 'px';
        ripple.style.top = (e.clientY - rect.top) + 'px';
        btn.appendChild(ripple);
        ripple.addEventListener('animationend', function() { ripple.remove(); });
      });
    });
  }

  /* ------------------------------------------------
     DOM Ready
     ------------------------------------------------ */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initComponents);
  } else {
    initComponents();
  }

  /* ------------------------------------------------
     Public API — exposed on window.MindMatrix
     ------------------------------------------------ */
  window.MindMatrix = {
    showAlert: showAlert,
    togglePassword: togglePassword,
    selectQuizOption: selectQuizOption,
    submitQuiz: submitQuiz,
    startQuiz: startQuiz,
    updateProgressRing: updateProgressRing,
    loadGrowthChart: loadGrowthChart,
    navigateTo: navigateTo,
    confirmAction: confirmAction,
    getCookie: getCookie,
    setCookie: setCookie,
    validateLoginForm: validateLoginForm,
    validateSignupForm: validateSignupForm,
    showFormErrors: showFormErrors
  };

})();

// Milestone card — QUOTE 2 trigger
function showMilestoneCard(topicName) {
  // Remove existing milestone cards
  var existing = document.querySelector('.milestone-card');
  if (existing) existing.remove();

  var card = document.createElement('div');
  card.className = 'milestone-card';
  card.setAttribute('role', 'alert');
  card.setAttribute('aria-live', 'assertive');
  card.innerHTML =
    '<div class="ms-header">' +
      '<div class="ms-icon"><svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg></div>' +
      '<span class="ms-label">Topic Mastered</span>' +
    '</div>' +
    '<div class="ms-topic">' + topicName + '</div>' +
    '<div class="ms-quote">Not a step. A turning point.</div>' +
    '<button class="ms-continue" onclick="dismissMilestone()">Continue &rarr;</button>';
  document.body.appendChild(card);

  // Auto-dismiss after 8 seconds
  window._msTimer = setTimeout(function() { dismissMilestone(); }, 8000);
}

function dismissMilestone() {
  clearTimeout(window._msTimer);
  var card = document.querySelector('.milestone-card');
  if (card) {
    card.classList.add('exit');
    card.addEventListener('animationend', function() { card.remove(); }, { once: true });
  }
}

// Expose globally for server-side calls
window.showMilestoneCard = showMilestoneCard;
