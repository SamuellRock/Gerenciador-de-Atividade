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
                const formattedDate = new Date(data.dia_atividade).toLocaleDateString('en-US', {year: 'numeric', month: '2-digit', day: '2-digit'}).split('/').join('-');
                diaServicoInput.value = formattedDate;
            });
    });

    horarioServicoSelect.addEventListener('change', function() {
        const servicoId = servicoSelect.value;
        const horario = this.value;
        const formattedHorario = new Date().toLocaleTimeString('en-US', {hour12: false, hour: '2-digit', minute: '2-digit'});
        console.log('Serviço selecionado ID:', servicoId);
        console.log('Horário selecionado:', horario);
        fetch(`/api/responsaveis_servico/${servicoId}/${formattedHorario}/`)
            .then(response => response.json())
            .then(data => {
                console.log('Responsáveis do serviço:', data);
                responsavelServicoSelect.innerHTML = `<option value="${data.id}">${data.first_name} ${data.last_name} (${data.email})</option>`;
            })
            .catch(error => console.error('Erro:', error));
    });

    // Função para preencher os campos de data e hora
    function inscrever() {
        const today = new Date();
        const formattedDate = today.toISOString().slice(0, 10);
        const formattedTime = today.toTimeString().slice(0, 5);
        diaServicoInput.value = formattedDate;
        document.getElementById("id_hora_servico").value = formattedTime;
    }

    // Chame a função inscrever quando necessário
    // Exemplo:
    // document.getElementById("botaoInscrever").addEventListener("click", inscrever);
});
