from django.forms import ModelForm
from .models import Inscrever_na_Atividade
from .models import Atividade
from .models import Usuario_Externo
from .models import lista_precenca
from .models import Servico
from .models import DiaAtividade
from django import forms
from datetime import timedelta, datetime, date
from django.core.exceptions import ValidationError


#Cadastro usuario externo
class Usuario_ExternoForm(ModelForm):
    class Meta:
        model = Usuario_Externo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            #self.fields[field].widget.attrs.update({'placeholder': field})

        self.fields['telefone'].widget.attrs.update({'id': 'beneficiaryPhone'})
        self.fields['cpf'].widget.attrs.update({'id': 'beneficiaryCpf'})
        self.fields['nascimento'].widget = forms.DateInput(attrs={'type': 'date', 'id': 'beneficiaryDob'})
        self.fields['nome'].widget.attrs.update({'id': 'beneficiaryName'})
        self.fields['endereco'].widget.attrs.update({'id': 'beneficiaryAddress'})
        self.fields['estado'].widget.attrs.update({'id': 'beneficiaryAddress'})
        self.fields['cidade'].widget.attrs.update({'id': 'beneficiaryAddress'})
        self.fields['responsavel_nome'].widget.attrs.update({'id': 'guardianName'})
        self.fields['responsavel_cpf'].widget.attrs.update({'id': 'guardianCpf'})


# Cadastro Atividade

class AtividadeForm(ModelForm):
    class Meta:
        model = Atividade
        exclude = ['slug']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'placeholder': field})

        self.fields['nome_atividade'].widget.attrs.update({'id': 'activityName'})
        self.fields['descricao'].widget.attrs.update({'id': 'activityDescription'})
        self.fields['responsavel'].widget.attrs.update({'id': 'activityResponsible'})
        self.fields['limite_alunos'].widget.attrs.update({'id': 'activityLimit'})
        self.fields['hora_atividade'].widget.attrs.update({'id': 'activityTime'})
        self.fields['hora_atividade'].widget = forms.DateInput(attrs={'type': 'time'})
        self.fields['dia_atividade'].widget.attrs.update({'id': 'activityDay'})


        self.fields['responsavel'].label_from_instance = lambda obj: "{:<30}{:<30}{:>30}".format(obj.first_name,
                                                                                                   obj.last_name,
                                                                                                   obj.email)

    #Ver se a atividade esta cadastrada em certo horario
    def clean(self):
        cleaned_data = super().clean()
        responsavel = cleaned_data.get('responsavel')
        hora_atividade = cleaned_data.get('hora_atividade')
        dias_atividade = cleaned_data.get('dia_atividade')

        if responsavel and hora_atividade and dias_atividade:
            for dia in dias_atividade:
                outras_atividades = Atividade.objects.filter(responsavel=responsavel, dia_atividade=dia)

                for atividade in outras_atividades:
                    if abs(atividade.hora_atividade.hour - hora_atividade.hour) < 5:
                        raise ValidationError('Deve haver um intervalo de 5 horas entre as atividades do mesmo responsável no mesmo dia.')

        return cleaned_data


class ServicoAtividadeForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome_servico'].widget.attrs.update({'id': 'activityName'})
        self.fields['descricao'].widget.attrs.update({'id': 'activityDescription'})
        self.fields['responsavel'].widget.attrs.update({'id': 'activityResponsible'})
        self.fields['dia_atividade'].widget.attrs.update({'id': 'activityDay'})
        self.fields['hora_inicio'].widget.attrs.update({'id': 'activityTime'})
        self.fields['hora_fim_atividade'].widget.attrs.update({'id': 'activityTime'})
        self.fields['hora_inicio'].widget = forms.DateInput(attrs={'type': 'time'})
        self.fields['hora_fim_atividade'].widget = forms.DateInput(attrs={'type': 'time'})
        self.fields['dia_atividade'].widget = forms.DateInput(attrs={'type': 'date'})

        #TODO TYPE TIME

        for field in self.fields:
            self.fields[field].widget.attrs.update({'placeholder': field})




# Inscrever Atividade
class Inscrever_na_AtividadeForm(forms.ModelForm):
    class Meta:
        model = Inscrever_na_Atividade
        fields = '__all__'

    atividades_do_responsavel = forms.CharField(
        label='Atividades do Responsável',
        required=False,
        widget=forms.Select(attrs={'readonly': 'readonly', 'class': 'form-control'})
    )
    horas_das_atividades = forms.CharField(
        label='Horas das Atividades',
        required=False,
        widget=forms.Select(attrs={'readonly': 'readonly', 'class': 'form-control'})
    )
    email_do_responsavel = forms.EmailField(
        label='Email do Responsável',
        required=False,
        widget=forms.EmailInput(attrs={'readonly': 'readonly', 'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'placeholder': field})

        self.fields['atividade'].label_from_instance = lambda obj: f"{obj.responsavel.first_name} {obj.responsavel.last_name} / {obj.responsavel.email}"



# Lista_Precenca
class Lista_PrecencaForm(ModelForm):
    class Meta:
        model = lista_precenca
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['aluno'].widget.attrs.update({'class': 'form-control'})


