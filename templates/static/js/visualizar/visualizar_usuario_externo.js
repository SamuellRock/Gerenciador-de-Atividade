// Função para carregar dados do usuário do banco de dados

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


// Função para calcular a idade
function getAge(dob) {
    const diff = Date.now() - dob.getTime();
    const ageDate = new Date(diff);
    return Math.abs(ageDate.getUTCFullYear() - 1970);
}

// Carregar os dados ao carregar a página
document.addEventListener('DOMContentLoaded', loadUserData);