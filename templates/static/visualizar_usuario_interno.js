// Função para carregar dados do usuário do banco de dados
function loadUserData() {
    // Simulação de chamada para obter os dados do usuário
    // Chamada real para o backend
    const userData = {
        nome: "Glenda Rangel",
        userType: "Funcionário",
        funcao: "Coordenador",
        email: "glenda.rangel@hotmail.com",
        userPerfil: "Administrador",
        activities: [
            { name: "Aula de Matemática", date: "25/05/2025", time: "10:00" },
            { name: "Reunião Pedagógica", date: "26/05/2025", time: "14:00" },
            { name: "Workshop de Ciências", date: "27/05/2025", time: "09:00" }
        ]
    };

    // Preenchendo os dados no formulário
    document.getElementById('nome').value = userData.nome;
    document.getElementById('userType').value = userData.userType;
    document.getElementById('funcao').value = userData.funcao;
    document.getElementById('email').value = userData.email;
    document.getElementById('userPerfil').value = userData.userPerfil;

    // Preenchendo a lista de atividades
    const activityList = document.getElementById('activityList');
    userData.activities.forEach(activity => {
        const activityItem = document.createElement('li');
        activityItem.textContent = `${activity.name} - ${activity.date} - ${activity.time}`;
        activityList.appendChild(activityItem);
    });
}

// Carregar os dados ao carregar a página
document.addEventListener('DOMContentLoaded', loadUserData);