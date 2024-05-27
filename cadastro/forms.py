from django.forms import ModelForm
from .models import Inscrever_na_Atividade
from .models import Atividade
from .models import Usuario_Externo
from .models import lista_precenca
from .models import Tipo_Atividade
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
        self.fields['responsavel'].label_from_instance = lambda obj: "{:<30}{:<30}{:>30}".format(obj.first_name,
                                                                                                   obj.last_name,
                                                                                                   obj.email)

    def clean(self):
            cleaned_data = super().clean()
            responsavel = cleaned_data.get('responsavel')
            dia_atividade = cleaned_data.get('dia_atividade')
            hora_atividade = cleaned_data.get('hora_atividade')

            if responsavel and dia_atividade and hora_atividade:
                atividades = Atividade.objects.filter(responsavel=responsavel, dia_atividade=dia_atividade)

                for atividade in atividades:
                    diferenca_tempo = abs(datetime.combine(date.today(), hora_atividade) - datetime.combine(date.today(), atividade.hora_atividade))
                    if diferenca_tempo < timedelta(hours=5):
                        raise ValidationError("O responsável já tem uma atividade no mesmo dia com menos de 4 horas de diferença.")



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


