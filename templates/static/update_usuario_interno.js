document.addEventListener('DOMContentLoaded', function() {
    const apiUrl = 'URL_DA_SUA_API';
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            // Preencher o formulário com os dados obtidos
            document.getElementById('nome').value = data.nome;
            document.getElementById('userType').value = data.userType;
            document.getElementById('funcao').value = data.funcao;
            document.getElementById('email').value = data.email;
            document.getElementById('userPerfil').value = data.userPerfil;
        })

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
        // Enviar os dados para o backend 
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