    function toggleDropdown(event, dropdownId) {
        event.preventDefault();
        var dropdown = document.getElementById(dropdownId);
        dropdown.style.display = dropdown.style.display === 'none' || dropdown.style.display === '' ? 'block' : 'none';
    }

    document.addEventListener("DOMContentLoaded", function() {
        // Exemplo de dados do usuário, que seriam carregados dinamicamente
        var userProfile = {
            name: "Samuel",
            picture: "D:/DocumentosHD/PROJETO WEB3/img/perfil.jpg" // Caminho da imagem
        };

        document.getElementById("profile-name").textContent = userProfile.name;
        document.getElementById("profile-picture").src = userProfile.picture;

        // Atualizar data atual
        var currentDate = new Date();
        var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
        document.getElementById("current-date").textContent = currentDate.toLocaleDateString('pt-BR', options);

        // Carregar dados das aulas e serviços do banco de dados
        carregarNomes();
        carregarAulas();
        carregarServicos();
        carregarHorarios();
        carregarResponsaveis();
    });

    function carregarNomes() {
        // Esta função deve fazer uma chamada ao backend para obter os nomes
        var nomes = [
            { id: 1, nome: "João" },
            { id: 2, nome: "Maria" }
        ];

        var nomeAulaSelect = document.getElementById("nomeAula");
        var nomeServicoSelect = document.getElementById("nomeServico");
        nomes.forEach(function(nome) {
            var option = document.createElement("option");
            option.value = nome.id;
            option.textContent = nome.nome;
            nomeAulaSelect.appendChild(option);
            nomeServicoSelect.appendChild(option);
        });
    }

    function carregarAulas() {
        // Esta função deve fazer uma chamada ao backend para obter os dados das aulas
        var aulas = [
            { id: 1, nome: "Aula de Matemática" },
            { id: 2, nome: "Aula de Português" }
        ];

        var aulaSelect = document.getElementById("aula");
        aulas.forEach(function(aula) {
            var option = document.createElement("option");
            option.value = aula.id;
            option.textContent = aula.nome;
            aulaSelect.appendChild(option);
        });
    }

    function carregarServicos() {
        // Esta função deve fazer uma chamada ao backend para obter os dados dos serviços
        var servicos = [
            { id: 1, nome: "Serviço de Psicologia" },
            { id: 2, nome: "Serviço de Orientação Vocacional" }
        ];

        var servicoSelect = document.getElementById("servico");
        servicos.forEach(function(servico) {
            var option = document.createElement("option");
            option.value = servico.id;
            option.textContent = servico.nome;
            servicoSelect.appendChild(option);
        });
    }

    function carregarHorarios() {
        // Esta função deve fazer uma chamada ao backend para obter os horários
        var horarios = [
            { id: 1, horario: "08:00" },
            { id: 2, horario: "09:00" }
        ];

        var horarioAulaSelect = document.getElementById("horarioAula");
        var horarioServicoSelect = document.getElementById("horarioServico");
        horarios.forEach(function(horario) {
            var option = document.createElement("option");
            option.value = horario.id;
            option.textContent = horario.horario;
            horarioAulaSelect.appendChild(option);
            horarioServicoSelect.appendChild(option);
        });
    }

    function carregarResponsaveis() {
        // Esta função deve fazer uma chamada ao backend para obter os responsáveis
        var responsaveis = [
            { id: 1, nome: "Prof. João" },
            { id: 2, nome: "Prof. Maria" }
        ];

        var responsavelAulaSelect = document.getElementById("responsavelAula");
        var responsavelServicoSelect = document.getElementById("responsavelServico");
        responsaveis.forEach(function(responsavel) {
            var option = document.createElement("option");
            option.value = responsavel.id;
            option.textContent = responsavel.nome;
            responsavelAulaSelect.appendChild(option);
            responsavelServicoSelect.appendChild(option);
        });
    }

    function mostrarNotificacao() {
        var notificacao = document.getElementById('notification');
        notificacao.style.display = 'block';

        setTimeout(function() {
            notificacao.style.display = 'none';
        }, 3000);
    }

    function inscrever() {
        // Aqui você pode adicionar o código para enviar os dados para o backend
        mostrarNotificacao();
    }


