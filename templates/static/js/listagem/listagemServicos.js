function toggleDropdown(event, dropdownId) {
    event.preventDefault();
    var dropdown = document.getElementById(dropdownId);
    dropdown.style.display = dropdown.style.display === 'none' || dropdown.style.display === '' ? 'block' : 'none';
}

function openModal() {
    document.getElementById("deleteModal").style.display = "block";
}

function closeModal() {
    document.getElementById("deleteModal").style.display = "none";
}

function confirmDeletion() {
    closeModal();
    showNotification();
    //adicionar o código para deletar o item
}

function showNotification() {
    var notification = document.getElementById("notification");
    notification.className = "notification show";
    setTimeout(function() {
        notification.className = notification.className.replace("show", "");
    }, 3000);
}

function openExternalModal(url, modalClass) {
    var modal = document.getElementById("externalModal");
    var modalContent = document.getElementById("externalModalContent");
    var iframe = document.getElementById("externalModalIframe");

    modalContent.className = "modal-content " + modalClass;
    iframe.src = url;
    modal.style.display = "block";
}

function closeExternalModal() {
    var modal = document.getElementById("externalModal");
    var iframe = document.getElementById("externalModalIframe");

    iframe.src = "";
    modal.style.display = "none";
}

// Simulação de carregamento de dados do usuário
document.addEventListener("DOMContentLoaded", function() {
    // Exemplo de dados do usuário, que seriam carregados dinamicamente
    var userProfile = {
        name: "Samuel",
        picture: "D:/DocumentosHD/PROJETO WEB3/img/perfil.jpg" // Caminho da imagem
    };

    document.getElementById("profile-name").textContent = userProfile.name;
    document.getElementById("profile-picture").src = userProfile.picture;
});
document.getElementById('search-button').addEventListener('click', function() {
    var input = document.getElementById('search-input').value.toLowerCase();
    var rows = document.querySelectorAll('.box');

    rows.forEach(row => {
        var cells = row.querySelectorAll('h3, h5');
        var match = false;
        cells.forEach(cell => {
            if (cell.textContent.toLowerCase().includes(input)) {
                match = true;
            }
        });
        if (match) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
});