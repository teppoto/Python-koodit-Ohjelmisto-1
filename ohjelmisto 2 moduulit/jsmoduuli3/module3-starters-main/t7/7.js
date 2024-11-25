// Ensure the script runs only after the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
  // Select the elements
  const trigger = document.getElementById('trigger');
  const target = document.getElementById('target');

  // Event listener for mouseover (hover starts)
  trigger.addEventListener('mouseover', () => {
    target.src = 'img/picB.jpg'; // Change image to picB.jpg
  });

  // Event listener for mouseout (hover ends)
  trigger.addEventListener('mouseout', () => {
    target.src = 'img/picA.jpg'; // Change image back to picA.jpg
  });
});