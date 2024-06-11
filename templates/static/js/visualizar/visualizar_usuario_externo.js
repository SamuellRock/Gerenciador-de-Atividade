// Função para carregar dados do usuário do banco de dados
function loadUserData() {
    // Simulação de chamada para obter os dados do usuário
    // Chamada real para o backend
    const userData = {
        beneficiaryName: "Maria da Silva",
        beneficiaryCpf: "123.456.789-00",
        beneficiaryDob: "2006-05-15",
        beneficiaryPhone: "11999999999",
        beneficiaryAddress: "Rua Exemplo, 123",
        beneficiaryCity: "São Paulo",
        beneficiaryState: "SP",
        guardianName: "João da Silva",
        guardianCpf: "987.654.321-00",
        guardianPhone: "11988888888",
        activities: [
            { name: "Aula de Matemática", date: "25/05/2025", time: "10:00" },
            { name: "Reunião Pedagógica", date: "26/05/2025", time: "14:00" },
            { name: "Workshop de Ciências", date: "27/05/2025", time: "09:00" }
        ]
    };

    // Preenchendo os dados no formulário
    document.getElementById('beneficiaryName').value = userData.beneficiaryName;
    document.getElementById('beneficiaryCpf').value = userData.beneficiaryCpf;
    document.getElementById('beneficiaryDob').value = userData.beneficiaryDob;
    document.getElementById('beneficiaryPhone').value = userData.beneficiaryPhone;
    document.getElementById('beneficiaryAddress').value = userData.beneficiaryAddress;
    document.getElementById('beneficiaryCity').value = userData.beneficiaryCity;
    document.getElementById('beneficiaryState').value = userData.beneficiaryState;

    // Verificando se a pessoa é menor de idade ao carregar a página
    const dob = new Date(userData.beneficiaryDob);
    const age = getAge(dob);
    if (age < 18) {
        document.getElementById('guardianFields').classList.remove('hidden');
        document.getElementById('guardianName').value = userData.guardianName;
        document.getElementById('guardianCpf').value = userData.guardianCpf;
        document.getElementById('guardianPhone').value = userData.guardianPhone;
    }

    // Preenchendo a lista de atividades
    const activityList = document.getElementById('activityList');
    userData.activities.forEach(activity => {
        const activityItem = document.createElement('li');
        activityItem.textContent = `${activity.name} - ${activity.date} - ${activity.time}`;
        activityList.appendChild(activityItem);
    });
}

// Função para calcular a idade
function getAge(dob) {
    const diff = Date.now() - dob.getTime();
    const ageDate = new Date(diff);
    return Math.abs(ageDate.getUTCFullYear() - 1970);
}

// Carregar os dados ao carregar a página
document.addEventListener('DOMContentLoaded', loadUserData);