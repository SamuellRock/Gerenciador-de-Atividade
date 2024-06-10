
// Preenchendo os dados no formulário
document.getElementById('activityName').value = activityData.name;
document.getElementById('activityDescription').value = activityData.description;
document.getElementById('activityResponsible').value = activityData.responsible;
document.getElementById('activityLimit').value = activityData.limit;
document.getElementById('activityStatus').value = activityData.status;
document.getElementById('activityTime').value = activityData.time;
document.getElementById('activityEnrollment').value = `${activityData.enrolled}/${activityData.limit}`;

// Preenchendo os dias da aula
const daysContainer = document.getElementById('activityDaysContainer');
activityData.days.forEach(day => {
    const dayElement = document.createElement('div');
    dayElement.classList.add('activity-day');
    dayElement.textContent = day;
    daysContainer.appendChild(dayElement);
});

// Preenchendo os nomes dos alunos
const namesList = document.getElementById('enrolledNamesList');
activityData.students.forEach(student => {
    const studentElement = document.createElement('li');
    studentElement.textContent = student;
    namesList.appendChild(studentElement);
});


