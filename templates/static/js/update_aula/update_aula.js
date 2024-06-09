document.getElementById('addDayBtn').addEventListener('click', function () {
    const activityDay = document.createElement('div');
    activityDay.classList.add('activity-day');
    activityDay.innerHTML = `
        <div class="form-group">
            <label for="activityDay">Dia da Semana da Aula:</label>
            <select name="dia_atividade[]" required>
                <option value="Segunda-feira">Segunda-feira</option>
                <option value="Terça-feira">Terça-feira</option>
                <option value="Quarta-feira">Quarta-feira</option>
                <option value="Quinta-feira">Quinta-feira</option>
                <option value="Sexta-feira">Sexta-feira</option>
                <option value="Sábado">Sábado</option>
                <option value="Domingo">Domingo</option>
            </select>
        </div>
    `;
    document.getElementById('activityDaysContainer').appendChild(activityDay);
});

// Função para exibir notificações
function showNotification(message) {
    const notification = document.getElementById('notification');
    notification.innerText = message;
    notification.style.display = 'block';
    setTimeout(() => {
        notification.style.display = 'none';
    }, 3000);
}

// Exibir a confirmação de salvar alterações
document.getElementById('saveChangesBtn').addEventListener('click', function () {
    document.getElementById('saveConfirmation').style.display = 'block';
});

// Confirmar salvar alterações e enviar o formulário
document.getElementById('confirmSaveBtn').addEventListener('click', function () {
    const form = document.getElementById('activityForm');
    form.submit();
    document.getElementById('saveConfirmation').style.display = 'none';
});

// Cancelar salvar alterações
document.getElementById('cancelSaveBtn').addEventListener('click', function () {
    document.getElementById('saveConfirmation').style.display = 'none';
});

// Exibir a confirmação de finalizar aulas
document.getElementById('finalizeBtn').addEventListener('click', function () {
    document.getElementById('finalizeConfirmation').style.display = 'block';
});

// Confirmar finalizar aulas
document.getElementById('confirmFinalizeBtn').addEventListener('click', function () {
    finalizeClasses();
    document.getElementById('finalizeConfirmation').style.display = 'none';
});

// Cancelar finalizar aulas
document.getElementById('cancelFinalizeBtn').addEventListener('click', function () {
    document.getElementById('finalizeConfirmation').style.display = 'none';
});
