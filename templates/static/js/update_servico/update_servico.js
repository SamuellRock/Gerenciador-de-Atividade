document.addEventListener('DOMContentLoaded', function () {
    // Função para exibir notificações
    function showNotification(message) {
        const notification = document.getElementById('notification');
        notification.innerText = message;
        notification.style.display = 'block';
        setTimeout(() => {
            notification.style.display = 'none';
        }, 3000);
    }

    // Função para gerar horários
    function generateTimeSlots() {
        const startTime = document.getElementById('timeIntervalStart').value;
        const endTime = document.getElementById('timeIntervalEnd').value;
        const durationField = document.getElementById('timeSlotDuration');
        const durationHour = parseInt(durationField.value.split(':')[0]);
        const durationMinute = parseInt(durationField.value.split(':')[1]);
        const duration = durationHour * 60 + durationMinute;

        if (startTime && endTime && duration > 0) {
            const start = new Date(`1970-01-01T${startTime}:00`);
            const end = new Date(`1970-01-01T${endTime}:00`);
            const container = document.getElementById('timeSlotsContainer');
            container.innerHTML = '';

            let currentTime = start;
            while (currentTime < end) {
                const nextTime = new Date(currentTime.getTime() + duration * 60000);
                if (nextTime <= end) {
                    const timeSlot = document.createElement('div');
                    timeSlot.textContent = `${currentTime.toTimeString().substr(0, 5)} - ${nextTime.toTimeString().substr(0, 5)}`;
                    container.appendChild(timeSlot);
                }
                currentTime = nextTime;
            }
        } else {
            showNotification('Por favor, preencha todos os campos e insira uma duração válida.');
        }
    }

    // Exibir a confirmação de salvar alterações
    document.getElementById('saveChangesBtn').addEventListener('click', function () {
        document.getElementById('saveConfirmation').style.display = 'block';
    });

    // Confirmar salvar alterações
    document.getElementById('confirmSaveBtn').addEventListener('click', function () {
        showNotification('Alterações salvas com sucesso!');
        const form = document.getElementById('activityForm');
        form.submit();
        document.getElementById('saveConfirmation').style.display = 'none';
    });

    // Cancelar salvar alterações
    document.getElementById('cancelSaveBtn').addEventListener('click', function () {
        document.getElementById('saveConfirmation').style.display = 'none';
    });

    // Exibir a confirmação de finalizar serviço
    document.getElementById('finalizeBtn').addEventListener('click', function () {
        document.getElementById('finalizeConfirmation').style.display = 'block';
    });

    // Confirmar finalizar serviço
    document.getElementById('confirmFinalizeBtn').addEventListener('click', function () {
        showNotification('Serviço finalizado com sucesso!');
        document.getElementById('finalizeConfirmation').style.display = 'none';
    });

    // Cancelar finalizar serviço
    document.getElementById('cancelFinalizeBtn').addEventListener('click', function () {
        document.getElementById('finalizeConfirmation').style.display = 'none';
    });

    document.getElementById('generateTimeSlotsBtn').addEventListener('click', generateTimeSlots);
});
