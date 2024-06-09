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
                timeSlot.classList.add('time-slot');
                timeSlot.textContent = `${currentTime.toTimeString().substr(0, 5)} - ${nextTime.toTimeString().substr(0, 5)}`;
                container.appendChild(timeSlot);
            }
            currentTime = nextTime;
        }
    } else {
        console.error('Por favor, preencha todos os campos e insira uma duração válida.');
    }
}

const generateTimeSlotsBtn = document.getElementById('generateTimeSlotsBtn');

if (generateTimeSlotsBtn) {
    generateTimeSlotsBtn.addEventListener('click', generateTimeSlots);
} else {
    console.error('Botão para gerar horários não encontrado.');
}
