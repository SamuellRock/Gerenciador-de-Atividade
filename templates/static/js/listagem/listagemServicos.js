function toggleDropdown(event, dropdownId) {
    event.preventDefault();
    var dropdown = document.getElementById(dropdownId);
    dropdown.style.display = dropdown.style.display === 'none' || dropdown.style.display === '' ? 'block' : 'none';
}

function openModal(button) {
    console.log("openModal called"); // Log de depuração
    console.log("Button:", button); // Log de depuração
    var id = button.getAttribute("data-id");
    console.log("ID:", id); // Log de depuração
    document.getElementById("deleteModal").style.display = "block";
    var confirmButton = document.getElementById("confirmDeleteButton");
    confirmButton.setAttribute("data-id", id);
}

function closeModal() {
    document.getElementById("deleteModal").style.display = "none";
}

function confirmDeletion() {
    var confirmButton = document.getElementById("confirmDeleteButton");
    var id = confirmButton.getAttribute("data-id");
    var url = `/deletar_servico/${id}/`;

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(response => {
        if (response.ok) {
            closeModal();
            showNotification();
            var row = document.querySelector(`button[data-id='${id}']`).closest('tr');
            row.parentNode.removeChild(row);
        } else {
            alert('Erro ao deletar o serviço.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
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

document.addEventListener("DOMContentLoaded", function() {
    var userProfile = {
        name: "Samuel",
        picture: "D:/DocumentosHD/PROJETO WEB3/img/perfil.jpg"
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
window.addEventListener('load', function() {
            if (window.location.search.includes('pesquisa')) {
                var url = new URL(window.location);
                url.searchParams.delete('pesquisa');
                window.history.replaceState({}, document.title, url.toString());
            }
});