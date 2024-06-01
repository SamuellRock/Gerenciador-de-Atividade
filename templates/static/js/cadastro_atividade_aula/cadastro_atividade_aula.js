document.addEventListener('DOMContentLoaded', function () {
    const addDayBtn = document.getElementById('addDayBtn');
    const activityDaysContainer = document.getElementById('activityDaysContainer');

    addDayBtn.addEventListener('click', function () {
        const activityDay = document.createElement('div');
        activityDay.classList.add('activity-day');
        activityDay.innerHTML = `
            <div class="form-group">
                <label for="activityDay">Dia da Semana da Aula:</label>
                <select id="activityDay" name="dia_atividade" required>
                    <option value="1">Segunda-feira</option>
                    <option value="2">Terça-feira</option>
                    <option value="3">Quarta-feira</option>
                    <option value="4">Quinta-feira</option>
                    <option value="5">Sexta-feira</option>
                    <option value="6">Sábado</option>
                    <option value="7">Domingo</option>
                </select>
            </div>
        `;
        activityDaysContainer.appendChild(activityDay);
    });
});