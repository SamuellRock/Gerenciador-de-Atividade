document.addEventListener('DOMContentLoaded', function () {
    const addTimeBtn = document.getElementById('addTimeBtn');
    const activityTimesContainer = document.getElementById('activityTimesContainer');

    addTimeBtn.addEventListener('click', function () {
        const activityTime = document.createElement('div');
        activityTime.classList.add('activity-time');
        activityTime.innerHTML = `
            <div class="form-group">
                <label for="activityTime">Hora da Atividade:</label>
                <input type="time" class="activityTime" name="activityTime[]" required>
            </div>
        `;
        activityTimesContainer.appendChild(activityTime);
    });
});