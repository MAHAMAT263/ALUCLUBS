const menuToggle = document.getElementById('menuToggle');
const menu = document.getElementById('menu');

// Toggle the active class on menuToggle
menuToggle.addEventListener('click', () => {
 menuToggle.classList.toggle('active');
});

// Close the menu when an anchor tag is clicked
const anchorTags = document.querySelectorAll('#menu a');
anchorTags.forEach(anchor => {
 anchor.addEventListener('click', () => {
   menuToggle.querySelector('input').checked = false;
   menuToggle.classList.remove('active');
 });
});

// Close the menu when scrolling
window.addEventListener('scroll', () => {
  menuToggle.querySelector('input').checked = false;
  menuToggle.classList.remove('active');
});

// Close the menu when touching the screen (except for the hamburger space)
document.addEventListener('touchstart', (event) => {
  const touchX = event.touches[0].clientX;
  const touchY = event.touches[0].clientY;

  const rect = menuToggle.getBoundingClientRect();

  // Check if the touch is outside the hamburger area
  if (
    touchX < rect.left ||
    touchX > rect.right ||
    touchY < rect.top ||
    touchY > rect.bottom
  ) {
    menuToggle.querySelector('input').checked = false;
    menuToggle.classList.remove('active');
  }
});

document.addEventListener("DOMContentLoaded", function() {
    const descriptions = document.querySelectorAll('.card-text');
    descriptions.forEach(desc => {
        const lineHeight = parseInt(window.getComputedStyle(desc).lineHeight, 10);
        const maxHeight = lineHeight * 5; // 5 lines
        if (desc.scrollHeight > maxHeight) {
            const originalText = desc.innerText;
            let truncatedText = '';
            const words = originalText.split(' ');

            for (let i = 0; i < words.length; i++) {
                truncatedText += words[i] + ' ';
                desc.innerText = truncatedText.trim() + '...';
                if (desc.scrollHeight > maxHeight) {
                    desc.innerText = truncatedText.trim() + '...';
                    break;
                }
            }
        }
    });
});