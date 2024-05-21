from django.forms import ModelForm
from .models import Inscrever_na_Atividade
from .models import Atividade
from .models import Usuario_Externo
from .models import lista_precenca
from .models import Tipo_Atividade


                                    #Cadastro usuario externo
class Usuario_ExternoForm(ModelForm):
    class Meta:
        model = Usuario_Externo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'placeholder': field})

        self.fields['telefone'].widget.attrs.update({'id': 'telefone', 'oninput': 'formatarTelefone(this)'})
        self.fields['cpf'].widget.attrs.update({'id': 'cpf', 'oninput': 'formatarCPF(this)'})
        self.fields['responsavel_cpf'].widget.attrs.update({'id': 'responsavel_cpf', 'oninput': 'formatarCPF(this)'})
        self.fields['nascimento'].widget.attrs.update({'id': 'data_nascimento', 'maxlength': '10', 'oninput':'formatarData(this)'})


                                    # Cadastro Atividade

class AtividadeForm(ModelForm):
    class Meta:
        model = Atividade
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'placeholder': field})

        #Display para aparecer o nome no choice
        choices = list()
        for tipo_atividade in Tipo_Atividade.objects.all():
            # Usar o valor do campo tipo_atividade para as escolhas
            choices.append((tipo_atividade.id, tipo_atividade.get_tipo_atividade_display()))

        self.fields['tipo_atividade'].choices = choices

        #instacia o first_name e o last_name para aparecer no dysplay
        self.fields['responsavel'].label_from_instance = lambda obj: "{:<30}{:<30}/{:>30}".format(obj.first_name,
                                                                                                   obj.last_name,
                                                                                                   obj.email)


class Inscrever_na_AtividadeForm(ModelForm):
    class Meta:
        model = Inscrever_na_Atividade
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'placeholder': field})


class Lista_PrecencaForm(ModelForm):
    class Meta:
        model = lista_precenca
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['aluno'].widget.attrs.update({'class': 'form-control'})


