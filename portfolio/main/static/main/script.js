const images = document.querySelectorAll('.grid .image-grille');
const modal = document.querySelector('.modal');
const modalContent = document.querySelector('.modal-content');

// Sélectionne les éléments de contenu de la fenêtre modale
const modalTitle = document.querySelector('#modal-title');
const modalImage = document.querySelector('#modal-image');
const modalLink = document.querySelector('#modal-link');
const modalDescription = document.querySelector('#modal-description');

// Ajoute un gestionnaire d'événements à chaque image
images.forEach(image => {
  image.addEventListener('click', () => {
    const title = image.dataset.title;
    const imageSrc = image.src;
    const link = image.dataset.link;
    const description = image.dataset.description;
    showModal(title, imageSrc, link, description);
  });
});

// Fonction pour fermer la fenêtre modale
function hideModal() {
  modal.style.display = 'none';
}

// Fonction pour afficher la fenêtre modale
function showModal(title, imageSrc, link, description) {
  modal.style.display = 'block';
  modalTitle.textContent = title;
  modalImage.src = imageSrc;
  modalLink.href = link;
  modalDescription.textContent = description;
}

// Fonction pour fermer la fenêtre modale en cliquant à l'extérieur de la fenêtre modale
window.addEventListener('touchend', (event) => {
    if (event.target == modal) {
      hideModal();
    }
});

window.addEventListener('click', (event) => {
if (event.target == modal) {
    hideModal();
}
});