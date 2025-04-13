// Form Validation
const form = document.getElementById('registrationForm');

form.addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent form from submitting

  const name = document.getElementById('name').value.trim();
  const email = document.getElementById('email').value.trim();
  const password = document.getElementById('password').value.trim();

  if (name === '' || email === '' || password === '') {
    alert('Please fill in all fields.');
    return;
  }

  if (!email.includes('@')) {
    alert('Please enter a valid email.');
    return;
  }

  if (password.length < 6) {
    alert('Password must be at least 6 characters.');
    return;
  }

  alert('Form is valid! 🎉');
});

// Interactive Element
const button = document.getElementById('showMessageBtn');
const message = document.getElementById('message');

button.addEventListener('click', function() {
  message.classList.toggle('hidden'); // Show or hide the message
});
