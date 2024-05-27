document.addEventListener('DOMContentLoaded', function() {
    var responsavelSelect = document.getElementById('responsavel-select');
    var atividadeSelect = document.getElementById('atividade-select');
    var horaAtividadeInput = document.getElementById('hora-atividade');
    var dataAtividadeInput = document.getElementById('data-atividade');

    responsavelSelect.addEventListener('change', function() {
        var responsavelId = this.value;
        if (responsavelId) {
            fetch('/get_responsavel_data/?responsavel_id=' + responsavelId)
                .then(response => response.json())
                .then(data => {
                    atividadeSelect.innerHTML = '';
                    horaAtividadeInput.value = '';
                    dataAtividadeInput.value = '';

                    atividadeSelect.appendChild(new Option('Selecione uma atividade', ''));

                    data.atividades_do_responsavel.forEach(function(atividade) {
                        var option = document.createElement('option');
                        option.value = atividade.id;
                        option.text = atividade.nome_atividade;
                        option.setAttribute('data-hora', atividade.hora_atividade);
                        option.setAttribute('data-dia', atividade.dia_atividade);
                        atividadeSelect.appendChild(option);
                    });

                    if (data.email_do_responsavel) {
                        document.getElementById('id_email_do_responsavel').value = data.email_do_responsavel;
                    }
                })
                .catch(error => console.error('Error:', error));
        } else {
            atividadeSelect.innerHTML = '';
            horaAtividadeInput.value = '';
            dataAtividadeInput.value = '';
        }
    });

    atividadeSelect.addEventListener('change', function() {
        var selectedOption = this.options[this.selectedIndex];
        if (selectedOption) {
            horaAtividadeInput.value = selectedOption.getAttribute('data-hora');
            dataAtividadeInput.value = selectedOption.getAttribute('data-dia');
        } else {
            horaAtividadeInput.value = '';
            dataAtividadeInput.value = '';
        }
    });
});
