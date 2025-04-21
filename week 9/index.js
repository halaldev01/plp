const body = document.body;
const toggleBtn = document.getElementById('themeToggle');

// Load saved theme from localStorage
function loadTheme() {
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme) {
    body.classList.add(savedTheme);
  } else {
    body.classList.add('light'); // Default to light mode
  }
}

// Toggle theme and store preference
function toggleTheme() {
  if (body.classList.contains('light')) {
    body.classList.replace('light', 'dark');
    localStorage.setItem('theme', 'dark');
  } else {
    body.classList.replace('dark', 'light');
    localStorage.setItem('theme', 'light');
  }

  // Trigger animation
  toggleBtn.classList.add('animate');
  setTimeout(() => toggleBtn.classList.remove('animate'), 400);
}

// Event listener
toggleBtn.addEventListener('click', toggleTheme);

// Initialize on page load
loadTheme();
