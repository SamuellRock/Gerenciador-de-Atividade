document.addEventListener("DOMContentLoaded", function() {
    const servicoSelect = document.querySelector('#servico');
    const horarioServicoSelect = document.querySelector('#horarioServico');
    const responsavelServicoSelect = document.querySelector('#responsavelServico');
    const diaServicoInput = document.querySelector('#Dia');

    servicoSelect.addEventListener('change', function() {
        const servicoId = this.value;
        fetch(`/api/horarios_servico/${servicoId}/`)
            .then(response => response.json())
            .then(data => {
                console.log('Horários do serviço:', data);
                horarioServicoSelect.innerHTML = data.horarios.map(horario => `<option value="${horario}">${horario}</option>`).join('');
                horarioServicoSelect.dispatchEvent(new Event('change'));
                responsavelServicoSelect.innerHTML = '<option value="">Selecione o horário primeiro</option>';
            });

        fetch(`/api/dia_atividade/${servicoId}/`)
            .then(response => response.json())
            .then(data => {
                console.log('Dia do serviço:', data);
                // Formatei a data para o formato ISO (YYYY-MM-DD) esperado pelo input de tipo "date"
                const formattedDate = new Date(data.dia_atividade).toISOString().split('T')[0];
                diaServicoInput.value = formattedDate;
            });
    });

    horarioServicoSelect.addEventListener('change', function() {
        const servicoId = servicoSelect.value;
        const horario = this.value;
        fetch(`/api/responsaveis_servico/${servicoId}/${horario}/`)
            .then(response => response.json())
            .then(data => {
                console.log('Responsáveis do serviço:', data);
                responsavelServicoSelect.innerHTML = `<option value="${data.id}">${data.first_name} ${data.last_name} (${data.email})</option>`;
            })
            .catch(error => console.error('Erro:', error));
    });

    function inscrever() {
        // Função inscrever é simplificada ou opcional, pois os campos já estão sendo preenchidos corretamente
    }
});
