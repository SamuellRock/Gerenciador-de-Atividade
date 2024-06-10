document.getElementById('activityName').value = activityData.name;
document.getElementById('activityDescription').value = activityData.description;
document.getElementById('activityResponsible').value = activityData.responsible;
document.getElementById('activityLimit').value = activityData.limit;
document.getElementById('activityStatus').value = activityData.status;
document.getElementById('activityTimeStart').value = activityData.timeStart;
document.getElementById('activityTimeEnd').value = activityData.timeEnd;
document.getElementById('activityEnrollment').value = `${activityData.enrolled}/${activityData.limit}`;

// Preenchendo os dias do serviço
const daysContainer = document.getElementById('activityDaysContainer');
activityData.days.forEach(day => {
    const dayElement = document.createElement('div');
    dayElement.classList.add('activity-day');
    dayElement.textContent = day;
    daysContainer.appendChild(dayElement);
});

// Preenchendo os nomes e horários dos beneficiados
const namesList = document.getElementById('enrolledNamesList');
activityData.students.forEach(student => {
    const studentRow = document.createElement('tr');
    const studentName = document.createElement('td');
    const studentTime = document.createElement('td');
    studentName.textContent = student.name;
    studentTime.textContent = student.time;
    studentRow.appendChild(studentName);
    studentRow.appendChild(studentTime);
    namesList.appendChild(studentRow);
});
