function toggleDropdown(event, dropdownId) {
    event.preventDefault();
    var dropdown = document.getElementById(dropdownId);
    dropdown.style.display = dropdown.style.display === 'none' || dropdown.style.display === '' ? 'block' : 'none';
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