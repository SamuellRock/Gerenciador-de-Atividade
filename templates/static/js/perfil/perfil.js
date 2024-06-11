function toggleDropdown(event, dropdownId) {
    event.preventDefault();
    var dropdown = document.getElementById(dropdownId);
    dropdown.style.display = dropdown.style.display === 'none' || dropdown.style.display === '' ? 'block' : 'none';
}

// document.addEventListener("DOMContentLoaded", function () {
//     var userProfile = {
//         name: "Elias",
//         email: "samuel@example.com",
//         picture: "img/perfil.jpg"
//     };

//     document.getElementById("profile-name").textContent = userProfile.name;
//     document.getElementById("profile-thumbnail").src = userProfile.picture;
// });

function changeProfilePicture(event) {
    const file = event.target.files[0];
    if (file) {
        const formData = new FormData();
        formData.append('profile-picture', file);

        fetch('/upload-profile-picture', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById("profile-picture").src = data.filepath;
                document.getElementById("profile-thumbnail").src = data.filepath;
            } else {
                alert('Erro ao fazer upload da imagem');
            }
        })
        .catch(error => {
            console.error('Erro:', error);
        });
    }
}

document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById("editModal");
    var modalIframe = document.getElementById("modalIframe");
    var editButton = document.querySelector(".edit-button");
    var closeModal = document.getElementsByClassName("close")[0];

    editButton.onclick = function(event) {
        event.preventDefault();
        modalIframe.src = editButton.getAttribute("data-url");
        modal.style.display = "block";
    };

    closeModal.onclick = function() {
        modal.style.display = "none";
        modalIframe.src = ""; 
    };

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
            modalIframe.src = ""; 
        }
    };
});