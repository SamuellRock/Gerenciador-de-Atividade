from django.forms import ModelForm
from .models import Inscrever_na_Atividade
from .models import Atividade
from .models import Usuario_Externo
from .models import lista_precenca


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

class AtividadeForm(ModelForm):
    class Meta:
        model = Atividade
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'placeholder': field})


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


