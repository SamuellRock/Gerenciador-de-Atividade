document.addEventListener("DOMContentLoaded", function() {
    const atividadeSelect = document.querySelector('select[name="nome_atividade"]');
    const horarioSelect = document.querySelector('#horarioAula');
    const responsavelSelect = document.querySelector('#responsavelAula');

    atividadeSelect.addEventListener('change', function() {
        const atividadeId = this.value;
        fetch(`/api/horarios/${atividadeId}/`)
            .then(response => response.json())
            .then(data => {
                console.log('Horarios:', data); // Log dos horários
                horarioSelect.innerHTML = data.horarios.map(horario => `<option value="${horario.hora}">${horario.hora}</option>`).join('');
                horarioSelect.dispatchEvent(new Event('change')); // Adicionado aqui
                responsavelSelect.innerHTML = '<option value="">Selecione o horário primeiro</option>';
            });
    });

    horarioSelect.addEventListener('change', function() {
        const atividadeId = atividadeSelect.value;
        const horario = this.value;
        console.log('Selecionado atividade ID:', atividadeId);
        console.log('Selecionado horário:', horario);
        fetch(`/api/responsaveis/${atividadeId}/${horario}/`)
            .then(response => response.json())
            .then(data => {
                console.log('Responsaveis:', data); // Log dos responsáveis
                responsavelSelect.innerHTML = `<option value="${data.id}">${data.first_name} ${data.last_name} (${data.email})</option>`;
            })
            .catch(error => console.error('Erro:', error));
    });
});

