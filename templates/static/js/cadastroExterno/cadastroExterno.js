function formatarTelefone(telefone) {
            // Remove caracteres não numéricos
            let valor = telefone.value.replace(/\D/g, '');

            // Adiciona parênteses e traço conforme o comprimento do valor
            if (valor.length <= 2) {
                valor = valor.replace(/(\d{0,2})/, '($1');
            } else if (valor.length <= 6) {
                valor = valor.replace(/(\d{0,2})(\d{0,4})/, '($1) $2');
            } else if (valor.length <= 10) {
                valor = valor.replace(/(\d{0,2})(\d{0,4})(\d{0,4})/, '($1) $2-$3');
            } else {
                valor = valor.replace(/(\d{0,2})(\d{0,5})(\d{0,4})/, '($1) $2-$3');
            }

            // Atualiza o valor do input
            telefone.value = valor;
        }

function formatarCPF(cpf) {
        // Remove caracteres não numéricos
        let valor = cpf.value.replace(/\D/g, "");

        // Adiciona pontos e traço conforme o comprimento do valor
        if (valor.length > 3 && valor.length <= 6) {
          valor = valor.replace(/(\d{3})(\d)/, "$1.$2");
        } else if (valor.length > 6 && valor.length <= 9) {
          valor = valor.replace(/(\d{3})(\d{3})(\d)/, "$1.$2.$3");
        } else if (valor.length > 9) {
          valor = valor.replace(
            /(\d{3})(\d{3})(\d{3})(\d{1,2})/,
            "$1.$2.$3-$4"
          );
        }

        cpf.value = valor;
      }

function formatarData(data) {
            let valor = data.value.replace(/\D/g, '');

            if (valor.length <= 2) {
                valor = valor.replace(/(\d{0,2})/, '$1');
            } else if (valor.length <= 4) {
                valor = valor.replace(/(\d{0,2})(\d{0,2})/, '$1/$2');
            } else if (valor.length <= 8) {
                valor = valor.replace(/(\d{0,2})(\d{0,2})(\d{0,4})/, '$1/$2/$3');
            }

            data.value = valor;
        }
