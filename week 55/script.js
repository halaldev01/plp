// Change text dynamically
const changeTextButton = document.getElementById('change-text-btn');
const introText = document.getElementById('intro-text');

changeTextButton.addEventListener('click', () => {
  introText.textContent = "You've changed the paragraph text!";
  introText.style.color = "green"; // Modify CSS style
});

// Add a new element
const addElementButton = document.getElementById('add-element-btn');
const container = document.getElementById('container');

addElementButton.addEventListener('click', () => {
  const newElement = document.createElement('p');
  newElement.textContent = "I'm a new paragraph added to the container!";
  newElement.style.color = "purple";
  container.appendChild(newElement);
});

// Remove the last element
const removeElementButton = document.getElementById('remove-element-btn');

removeElementButton.addEventListener('click', () => {
  if (container.lastChild) {
    container.removeChild(container.lastChild);
  }
});
