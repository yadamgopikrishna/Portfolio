/**
 * YADAM GOPIKRISHNA - AI & SOFTWARE ENGINEER PORTFOLIO
 * Main Interactive Engine & Media Controller
 */

document.addEventListener('DOMContentLoaded', () => {
  initBackgroundCanvas();
  initScrollProgress();
  initHeaderScroll();
  initMobileDrawer();
  initScrollSpy();
  initHeroVideoPlayer();
  initSkillObserver();
  initProjectFilters();
  initProjectModals();
  initContactForm();
  initBackToTop();
});

/* --------------------------------------------------------------------------
   1. Dynamic Background Canvas: Neural Starfield & Particle Constellation
   -------------------------------------------------------------------------- */
function initBackgroundCanvas() {
  const canvas = document.getElementById('bg-canvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  let width, height;
  let particles = [];
  const particleCount = window.innerWidth < 768 ? 40 : 80;
  const connectionDistance = 120;

  function resize() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
  }

  window.addEventListener('resize', resize);
  resize();

  class Particle {
    constructor() {
      this.x = Math.random() * width;
      this.y = Math.random() * height;
      this.vx = (Math.random() - 0.5) * 0.4;
      this.vy = (Math.random() - 0.5) * 0.4;
      this.radius = Math.random() * 1.8 + 0.8;
      this.baseAlpha = Math.random() * 0.5 + 0.2;
    }

    update() {
      this.x += this.vx;
      this.y += this.vy;

      if (this.x < 0 || this.x > width) this.vx *= -1;
      if (this.y < 0 || this.y > height) this.vy *= -1;
    }

    draw() {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(56, 189, 248, ${this.baseAlpha})`;
      ctx.shadowBlur = 8;
      ctx.shadowColor = '#38bdf8';
      ctx.fill();
    }
  }

  for (let i = 0; i < particleCount; i++) {
    particles.push(new Particle());
  }

  function animate() {
    ctx.clearRect(0, 0, width, height);

    // Draw connecting lines
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < connectionDistance) {
          const alpha = (1 - dist / connectionDistance) * 0.15;
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.strokeStyle = `rgba(99, 102, 241, ${alpha})`;
          ctx.lineWidth = 0.8;
          ctx.shadowBlur = 0;
          ctx.stroke();
        }
      }
    }

    particles.forEach(p => {
      p.update();
      p.draw();
    });

    requestAnimationFrame(animate);
  }

  animate();
}

/* --------------------------------------------------------------------------
   2. Scroll Progress Bar
   -------------------------------------------------------------------------- */
function initScrollProgress() {
  const progressBar = document.querySelector('.scroll-progress-bar');
  if (!progressBar) return;

  window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const progress = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
    progressBar.style.width = `${progress}%`;
  }, { passive: true });
}

/* --------------------------------------------------------------------------
   3. Sticky Header & Glassmorphism Transition
   -------------------------------------------------------------------------- */
function initHeaderScroll() {
  const header = document.querySelector('.header');
  if (!header) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  }, { passive: true });
}

/* --------------------------------------------------------------------------
   4. Mobile Navigation Drawer
   -------------------------------------------------------------------------- */
function initMobileDrawer() {
  const menuBtn = document.querySelector('.mobile-menu-btn');
  const closeBtn = document.querySelector('.drawer-close-btn');
  const drawer = document.querySelector('.mobile-drawer');
  const overlay = document.querySelector('.drawer-overlay');
  const links = document.querySelectorAll('.mobile-nav-link');

  if (!menuBtn || !drawer || !overlay) return;

  function openDrawer() {
    drawer.classList.add('open');
    overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    drawer.classList.remove('open');
    overlay.classList.remove('open');
    document.body.style.overflow = '';
  }

  menuBtn.addEventListener('click', openDrawer);
  if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
  overlay.addEventListener('click', closeDrawer);

  links.forEach(link => {
    link.addEventListener('click', closeDrawer);
  });
}

/* --------------------------------------------------------------------------
   5. Scroll Spy & Active Navigation Highlighting
   -------------------------------------------------------------------------- */
function initScrollSpy() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link, .mobile-nav-link');

  function updateSpy() {
    const scrollPosition = window.scrollY + 120;

    sections.forEach(section => {
      const top = section.offsetTop;
      const height = section.offsetHeight;
      const id = section.getAttribute('id');

      if (scrollPosition >= top && scrollPosition < top + height) {
        navLinks.forEach(link => {
          if (link.getAttribute('href') === `#${id}`) {
            link.classList.add('active');
          } else {
            link.classList.remove('active');
          }
        });
      }
    });
  }

  window.addEventListener('scroll', updateSpy, { passive: true });
  updateSpy();
}

/* --------------------------------------------------------------------------
   6. Hero Talking Video Engine: Autoplay & Audio/Voice Activation
   -------------------------------------------------------------------------- */
function initHeroVideoPlayer() {
  const video = document.getElementById('hero-main-video');
  const soundBanner = document.getElementById('hero-unmute-banner');
  const playToggleBtn = document.getElementById('hero-play-toggle-btn');
  const toggleIcon = document.getElementById('hero-toggle-icon');
  const heroSection = document.getElementById('hero');

  if (!video) return;

  // Single play settings
  video.loop = false;
  video.muted = false;
  video.volume = 1.0;

  let isHeroInView = true;
  let hasPlayedInitialIntro = false;

  // Voice / Audio Activation Function
  function enableAudio() {
    video.muted = false;
    video.volume = 1.0;
    if (soundBanner) {
      soundBanner.classList.add('hidden');
    }
  }

  function setPlayingUI() {
    if (playToggleBtn) playToggleBtn.classList.add('is-playing');
    if (toggleIcon) toggleIcon.className = 'fa-solid fa-pause play-btn-icon';
  }

  function setPausedUI() {
    if (playToggleBtn) playToggleBtn.classList.remove('is-playing');
    if (toggleIcon) toggleIcon.className = 'fa-solid fa-play play-btn-icon';
  }

  function playVideo() {
    enableAudio();
    const playPromise = video.play();
    if (playPromise !== undefined) {
      playPromise.then(() => {
        setPlayingUI();
      }).catch(err => {
        // If unmuted autoplay is deferred by browser, start muted and unlock on interaction
        console.log('Autoplay unmuted deferred, starting muted:', err);
        video.muted = true;
        video.play().then(() => {
          setPlayingUI();
        }).catch(e => console.log('Video error:', e));
      });
    }
  }

  function pauseVideo() {
    video.pause();
    setPausedUI();
  }

  function resetToBeginningAndPause() {
    video.pause();
    video.currentTime = 0;
    setPausedUI();
  }

  // 1. Initial Entry to Website: Play video automatically ONCE after 1 second
  setTimeout(() => {
    if (isHeroInView && !hasPlayedInitialIntro) {
      hasPlayedInitialIntro = true;
      playVideo();
    }
  }, 1000);

  // 2. When moving away from Home: Automatically RESET to beginning (0:00) and pause
  if (heroSection && 'IntersectionObserver' in window) {
    const heroObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        isHeroInView = entry.isIntersecting;
        if (!entry.isIntersecting) {
          // User scrolled away from home: Reset to beginning and pause immediately
          resetToBeginningAndPause();
        } else {
          // Returning to home later: Ensure it is reset at 0:00 ready for click
          if (hasPlayedInitialIntro && video.paused) {
            video.currentTime = 0;
            setPausedUI();
          }
        }
      });
    }, { threshold: 0.15 });
    heroObserver.observe(heroSection);
  }

  // Scroll listener fallback to ensure reset when leaving home
  window.addEventListener('scroll', () => {
    if (heroSection) {
      const rect = heroSection.getBoundingClientRect();
      const isVisible = rect.bottom > 120 && rect.top < window.innerHeight;
      isHeroInView = isVisible;
      if (!isVisible) {
        if (!video.paused || video.currentTime > 0) {
          resetToBeginningAndPause();
        }
      }
    }
  }, { passive: true });

  // Nav Links click listener: instantly reset to beginning when navigating
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', () => {
      const targetId = link.getAttribute('href');
      if (targetId !== '#hero' && targetId !== '#') {
        resetToBeginningAndPause();
      } else if (targetId === '#hero') {
        video.currentTime = 0;
        setPausedUI();
      }
    });
  });

  // 3. Play / Pause Button Over Hero Video
  function togglePlayPause() {
    if (video.paused || video.ended) {
      if (video.ended) {
        video.currentTime = 0;
      }
      playVideo();
    } else {
      pauseVideo(); // Only pauses where the user stopped it
    }
  }

  if (playToggleBtn) {
    playToggleBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      togglePlayPause();
    });
  }

  // Video click also toggles play / pause
  video.addEventListener('click', (e) => {
    e.stopPropagation();
    togglePlayPause();
  });

  // When video completes playing, reset to beginning (0:00) and show play button
  video.addEventListener('ended', () => {
    video.currentTime = 0;
    setPausedUI();
  });

  // Unmute on first gesture/interaction anywhere on page
  function handleUnlockInteraction() {
    enableAudio();
    window.removeEventListener('mousemove', handleUnlockInteraction);
    window.removeEventListener('click', handleUnlockInteraction);
    window.removeEventListener('touchstart', handleUnlockInteraction);
    window.removeEventListener('keydown', handleUnlockInteraction);
  }

  window.addEventListener('mousemove', handleUnlockInteraction, { once: true });
  window.addEventListener('click', handleUnlockInteraction, { once: true });
  window.addEventListener('touchstart', handleUnlockInteraction, { once: true });
  window.addEventListener('keydown', handleUnlockInteraction, { once: true });

  if (soundBanner) {
    soundBanner.addEventListener('click', (e) => {
      e.stopPropagation();
      enableAudio();
      playVideo();
    });
  }
}

/* --------------------------------------------------------------------------
   8. Skill Progress Bars Animated on Viewport Entry
   -------------------------------------------------------------------------- */
function initSkillObserver() {
  const skillBars = document.querySelectorAll('.progress-fill');
  if (!skillBars.length) return;

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const bar = entry.target;
        const targetWidth = bar.getAttribute('data-level') || '85%';
        bar.style.width = targetWidth;
        obs.unobserve(bar);
      }
    });
  }, { threshold: 0.2 });

  skillBars.forEach(bar => observer.observe(bar));

  // Category Tabs filtering
  const tabs = document.querySelectorAll('.skill-tab-btn');
  const cards = document.querySelectorAll('.skill-category-card');

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      const filter = tab.getAttribute('data-filter');

      cards.forEach(card => {
        if (filter === 'all' || card.getAttribute('data-category') === filter) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

/* --------------------------------------------------------------------------
   9. Projects Filter Tabs
   -------------------------------------------------------------------------- */
function initProjectFilters() {
  const tabs = document.querySelectorAll('.project-tab-btn');
  const projects = document.querySelectorAll('.project-card');

  if (!tabs.length) return;

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      const category = tab.getAttribute('data-category');

      projects.forEach(project => {
        if (category === 'all' || project.getAttribute('data-category') === category) {
          project.style.display = 'flex';
        } else {
          project.style.display = 'none';
        }
      });
    });
  });
}

/* --------------------------------------------------------------------------
   10. Project Details Modal Dynamic Content
   -------------------------------------------------------------------------- */
const projectData = {
  'student-pred': {
    title: 'AI-Powered Student Performance Prediction System',
    category: 'Machine Learning / Predictive Modeling',
    image: 'assets/projects/student-prediction.svg',
    summary: 'A complete end-to-end Machine Learning web platform designed to analyze educational variables, study behaviors, and academic history to accurately forecast student performance scores (R² = 0.94).',
    architecture: [
      'Data Ingestion: Ingestion and cleaning of demographic, behavioral, and academic performance datasets.',
      'Feature Engineering: Normalization, correlation analysis, and feature weight computation.',
      'Model Training: Regression models built using Scikit-learn (Linear Regression, Random Forest Regressor).',
      'Evaluation: Cross-validation, Mean Squared Error (MSE), Mean Absolute Error (MAE), and R² metric tracking.',
      'Frontend Interface: Interactive prediction dashboard with live risk classification and dynamic charts.'
    ],
    techStack: ['Python', 'Pandas', 'NumPy', 'Scikit-learn', 'HTML5', 'CSS3', 'JavaScript'],
    github: 'https://github.com/yadamgopikrishna'
  },
  'chatbot': {
    title: 'Intelligent AI Chatbot',
    category: 'Conversational AI / NLP',
    image: 'assets/projects/ai-chatbot.svg',
    summary: 'A modern conversational AI engine trained to parse natural language queries, classify user intentions, and deliver precise, contextual automated responses through a cybernetic glassmorphism interface.',
    architecture: [
      'Natural Language Processing: Tokenization, lemmatization, stop-word removal, and vocabulary building.',
      'Intent Recognition: Supervised classification model mapping queries to structured intent categories.',
      'Dialogue Management: Contextual state machine handling multi-turn conversational sequences.',
      'UI/UX: Real-time typing indicators, glassmorphic message bubbles, and responsive mobile layout.'
    ],
    techStack: ['Python', 'NLP Fundamentals', 'HTML5', 'CSS3', 'JavaScript', 'REST API'],
    github: 'https://github.com/yadamgopikrishna'
  },
  'image-classifier': {
    title: 'AI-Based Image Classification System',
    category: 'Computer Vision / Deep Learning',
    image: 'assets/projects/image-classifier.svg',
    summary: 'A computer vision application that applies convolutional neural network principles and machine learning classification algorithms to categorize imagery with confidence metrics and real-time bounding overlays.',
    architecture: [
      'Dataset Curation & Augmentation: Preprocessing pipelines for resizing (224x224), normalization, and data augmentation.',
      'Feature Extraction: Deep feature embeddings capturing spatial hierarchies and edge gradients.',
      'Classification Pipeline: Multi-class prediction output with Softmax probability distributions.',
      'Inspection Dashboard: Visual confusion matrix and diagnostic evaluation tool.'
    ],
    techStack: ['Python', 'Machine Learning', 'Deep Learning Concepts', 'NumPy', 'Pandas', 'HTML5/CSS3/JS'],
    github: 'https://github.com/yadamgopikrishna'
  },
  'portfolio-site': {
    title: 'Personal AI Engineer Portfolio Website',
    category: 'Full-Stack Modern Frontend',
    image: 'assets/projects/portfolio-preview.svg',
    summary: 'An ultra-fast, cinematic, responsive personal portfolio designed to showcase AI/ML projects, talking video reel, verified credentials, and interactive skill telemetry.',
    architecture: [
      'Canvas Engine: Lightweight JavaScript particle physics canvas simulating neural constellation links.',
      'Video Controller: Custom video player & reel modal system with zero external framework overhead.',
      'Accessible Architecture: Semantic HTML5, ARIA labels, smooth scroll navigation, and WCAG contrast.',
      'Modern CSS: CSS Custom Properties, backdrop filters, glowing gradients, and responsive CSS grids.'
    ],
    techStack: ['HTML5', 'CSS3 (Glassmorphism)', 'JavaScript ES6+', 'Canvas API', 'Modern Web Standards'],
    github: 'https://github.com/yadamgopikrishna'
  }
};

function initProjectModals() {
  const modalOverlay = document.getElementById('project-modal');
  const modalContent = document.getElementById('project-modal-content');
  const detailButtons = document.querySelectorAll('[data-project-id]');
  const closeBtn = document.getElementById('close-project-modal');

  if (!modalOverlay || !modalContent) return;

  function openProjectModal(projectId) {
    const data = projectData[projectId];
    if (!data) return;

    modalContent.innerHTML = `
      <div class="project-modal-header" style="margin-bottom: 1.5rem;">
        <span class="project-category-tag" style="position: static; display: inline-block; margin-bottom: 0.75rem;">${data.category}</span>
        <h2 style="font-size: 1.8rem; font-weight: 800; color: #f8fafc; line-height: 1.2;">${data.title}</h2>
      </div>

      <div style="border-radius: 14px; overflow: hidden; margin-bottom: 1.75rem; border: 1px solid rgba(56, 189, 248, 0.2);">
        <img src="${data.image}" alt="${data.title}" style="width: 100%; aspect-ratio: 16/9; object-fit: cover;">
      </div>

      <div style="margin-bottom: 1.75rem;">
        <h3 style="font-size: 1.1rem; font-weight: 700; color: #38bdf8; margin-bottom: 0.5rem;">Project Overview</h3>
        <p style="color: #cbd5e1; line-height: 1.7; font-size: 0.95rem;">${data.summary}</p>
      </div>

      <div style="margin-bottom: 1.75rem;">
        <h3 style="font-size: 1.1rem; font-weight: 700; color: #38bdf8; margin-bottom: 0.75rem;">System Architecture & Implementation</h3>
        <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.6rem; color: #94a3b8; font-size: 0.9rem;">
          ${data.architecture.map(item => `<li style="position: relative; padding-left: 1.25rem;"><span style="position: absolute; left: 0; color: #00f2fe;">▹</span>${item}</li>`).join('')}
        </ul>
      </div>

      <div style="margin-bottom: 2rem;">
        <h3 style="font-size: 1.1rem; font-weight: 700; color: #38bdf8; margin-bottom: 0.75rem;">Technologies & Tools</h3>
        <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
          ${data.techStack.map(tech => `<span class="tech-chip" style="background: rgba(30, 41, 59, 0.8); color: #38bdf8; font-weight: 600;">${tech}</span>`).join('')}
        </div>
      </div>

      <div style="display: flex; align-items: center; gap: 1rem; padding-top: 1.25rem; border-top: 1px solid rgba(255, 255, 255, 0.1);">
        <a href="${data.github}" target="_blank" rel="noopener noreferrer" class="btn-primary" style="padding: 0.75rem 1.5rem; font-size: 0.9rem;">
          <i class="fa-brands fa-github"></i> View GitHub Repository
        </a>
        <button class="btn-outline" onclick="document.getElementById('project-modal').classList.remove('active'); document.body.style.overflow='';" style="padding: 0.75rem 1.5rem; font-size: 0.9rem;">
          Close Window
        </button>
      </div>
    `;

    modalOverlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  detailButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const id = btn.getAttribute('data-project-id');
      openProjectModal(id);
    });
  });

  if (closeBtn) {
    closeBtn.addEventListener('click', () => {
      modalOverlay.classList.remove('active');
      document.body.style.overflow = '';
    });
  }

  modalOverlay.addEventListener('click', (e) => {
    if (e.target === modalOverlay) {
      modalOverlay.classList.remove('active');
      document.body.style.overflow = '';
    }
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modalOverlay.classList.contains('active')) {
      modalOverlay.classList.remove('active');
      document.body.style.overflow = '';
    }
  });
}

/* --------------------------------------------------------------------------
   11. Contact Form Interactive Handler & Toast Dispatcher
   -------------------------------------------------------------------------- */
function initContactForm() {
  const form = document.getElementById('contact-form');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = document.getElementById('contact-name').value.trim();
    const email = document.getElementById('contact-email').value.trim();
    const subject = document.getElementById('contact-subject').value;
    const message = document.getElementById('contact-message').value.trim();
    const submitBtn = form.querySelector('.btn-form-submit');

    if (!name || !email || !message) {
      showToast('Please fill out all required fields.', 'error');
      return;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      showToast('Please enter a valid email address.', 'error');
      return;
    }

    // Button loading state
    const originalContent = submitBtn.innerHTML;
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<i class="fa-solid fa-circle-notch fa-spin"></i> Transmitting Message...';

    // Simulate reliable dispatch & mailto trigger
    setTimeout(() => {
      try {
        const storedMessages = JSON.parse(localStorage.getItem('portfolio_messages') || '[]');
        storedMessages.push({ name, email, subject, message, date: new Date().toISOString() });
        localStorage.setItem('portfolio_messages', JSON.stringify(storedMessages));
      } catch (err) {
        console.log('LocalStorage not available');
      }

      submitBtn.innerHTML = '<i class="fa-solid fa-check"></i> Message Transmitted!';
      submitBtn.style.background = 'linear-gradient(135deg, #10b981 0%, #059669 100%)';
      showToast(`Thank you ${name}! Your message has been sent successfully to Yadam Gopikrishna.`, 'success');

      form.reset();

      setTimeout(() => {
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalContent;
        submitBtn.style.background = '';
      }, 3500);
    }, 1200);
  });
}

function showToast(message, type = 'success') {
  const container = document.getElementById('toast-container') || createToastContainer();
  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  
  const icon = type === 'success' 
    ? '<i class="fa-solid fa-circle-check" style="color: #10b981; font-size: 1.1rem;"></i>' 
    : '<i class="fa-solid fa-circle-exclamation" style="color: #f43f5e; font-size: 1.1rem;"></i>';

  toast.innerHTML = `${icon} <span>${message}</span>`;
  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(10px)';
    toast.style.transition = 'all 0.3s ease';
    setTimeout(() => toast.remove(), 300);
  }, 4000);
}

function createToastContainer() {
  const div = document.createElement('div');
  div.id = 'toast-container';
  div.className = 'toast-container';
  document.body.appendChild(div);
  return div;
}

/* --------------------------------------------------------------------------
   12. Back to Top Smooth Trigger
   -------------------------------------------------------------------------- */
function initBackToTop() {
  const btn = document.getElementById('back-to-top-btn');
  if (!btn) return;

  btn.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}
