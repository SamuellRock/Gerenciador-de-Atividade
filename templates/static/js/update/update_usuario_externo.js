document.addEventListener('DOMContentLoaded', function() {
    // Simulação de dados existentes
    const existingData = {
        beneficiaryName: "Maria da Silva",
        beneficiaryCpf: "123.456.789-00",
        beneficiaryDob: "2006-05-15",
        beneficiaryPhone: "11999999999",
        beneficiaryAddress: "Rua Exemplo, 123",
        beneficiaryCity: "São Paulo",
        beneficiaryState: "SP",
        guardianName: "João da Silva",
        guardianCpf: "987.654.321-00",
        guardianPhone: "11988888888"
    };

    // Preenchendo os campos com os dados existentes
    document.getElementById('beneficiaryName').value = existingData.beneficiaryName;
    document.getElementById('beneficiaryCpf').value = existingData.beneficiaryCpf;
    document.getElementById('beneficiaryDob').value = existingData.beneficiaryDob;
    document.getElementById('beneficiaryPhone').value = existingData.beneficiaryPhone;
    document.getElementById('beneficiaryAddress').value = existingData.beneficiaryAddress;
    document.getElementById('beneficiaryCity').value = existingData.beneficiaryCity;
    document.getElementById('beneficiaryState').value = existingData.beneficiaryState;

    const dob = new Date(existingData.beneficiaryDob);
    const age = getAge(dob);
    if (age < 18) {
        document.getElementById('guardianFields').classList.remove('hidden');
        document.getElementById('guardianName').value = existingData.guardianName;
        document.getElementById('guardianCpf').value = existingData.guardianCpf;
        document.getElementById('guardianPhone').value = existingData.guardianPhone;
    }

    document.getElementById('beneficiaryDob').addEventListener('change', function() {
        const dob = new Date(this.value);
        const age = getAge(dob);
        if (age < 18) {
            document.getElementById('guardianFields').classList.remove('hidden');
        } else {
            document.getElementById('guardianFields').classList.add('hidden');
        }
    });

    function getAge(dob) {
        const diff = Date.now() - dob.getTime();
        const ageDate = new Date(diff);
        return Math.abs(ageDate.getUTCFullYear() - 1970);
    }

    document.getElementById('saveChangesBtn').addEventListener('click', function() {
        document.getElementById('saveConfirmation').style.display = 'block';
    });

    document.getElementById('confirmSaveBtn').addEventListener('click', function() {
        saveChanges();
        document.getElementById('saveConfirmation').style.display = 'none';
    });

    document.getElementById('cancelSaveBtn').addEventListener('click', function() {
        document.getElementById('saveConfirmation').style.display = 'none';
    });

    function saveChanges() {
        const formData = new FormData(document.getElementById('beneficiaryForm'));
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });
        console.log(data);
        showNotification('Alterações salvas com sucesso!');
        // Aqui você pode enviar os dados para o backend usando fetch ou AJAX
    }

    function showNotification(message) {
        const notification = document.getElementById('notification');
        notification.innerText = message;
        notification.style.display = 'block';
        setTimeout(() => {
            notification.style.display = 'none';
        }, 3000);
    }
});