from django.forms import ModelForm, DateInput, Select, DateTimeInput
from .models import Inscrever_Aula
from .models import Inscrever_Servico
from .models import Atividade
from .models import Usuario_Externo
from .models import Servico
from django import forms
from django.core.exceptions import ValidationError
from django.forms import TimeInput


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
        self.fields['nome'].widget.attrs.update({'id': 'beneficiaryName'})
        self.fields['endereco'].widget.attrs.update({'id': 'beneficiaryAddress'})
        self.fields['estado'].widget.attrs.update({'id': 'beneficiaryAddress'})
        self.fields['cidade'].widget.attrs.update({'id': 'beneficiaryAddress'})
        self.fields['responsavel_nome'].widget.attrs.update({'id': 'guardianName'})
        self.fields['responsavel_cpf'].widget.attrs.update({'id': 'guardianCpf'})


# Cadastro Atividade

class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        exclude = ['slug']

        #isso ja converte direto o input
        widgets = {
            'hora_atividade': TimeInput(format='%H:%M', attrs={'type': 'time', 'id': 'activityTime'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initial_hora_atividade = self.instance.hora_atividade if self.instance.pk else None
        self.initial_responsavel = self.instance.responsavel if self.instance.pk else None
        self.initial_dia_atividade = self.instance.dia_atividade.all() if self.instance.pk else []

        self.fields['nome_atividade'].widget.attrs.update({'id': 'activityName'})
        self.fields['descricao'].widget.attrs.update({'id': 'activityDescription'})
        self.fields['responsavel'].widget.attrs.update({'id': 'activityResponsible'})
        self.fields['limite_alunos'].widget.attrs.update({'id': 'activityLimit'})
        self.fields['dia_atividade'].widget.attrs.update({'id': 'activityDay'})

        self.fields['responsavel'].label_from_instance = lambda obj: "{:<30}{:<30}{:>30}".format(obj.first_name,
                                                                                                   obj.last_name,
                                                                                                   obj.email)

    def clean(self):
        cleaned_data = super().clean()
        responsavel = cleaned_data.get('responsavel')
        hora_atividade = cleaned_data.get('hora_atividade')
        dias_atividade = cleaned_data.get('dia_atividade')

        if responsavel and hora_atividade and dias_atividade:
            for dia in dias_atividade:
                outras_atividades = Atividade.objects.filter(responsavel=responsavel, dia_atividade=dia)

                for atividade in outras_atividades:
                    if self.instance.pk and atividade.pk == self.instance.pk:
                        continue
                    if abs(atividade.hora_atividade.hour - hora_atividade.hour) < 5:
                        raise ValidationError('Deve haver um intervalo de 5 horas entre as atividades do mesmo responsável no mesmo dia.')

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            self.save_m2m()
        else:
            instance.save()
        return instance


class ServicoAtividadeForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'
        widgets = {
            'hora_inicio': TimeInput(format='%H:%M', attrs={'type': 'time', 'id': 'timeIntervalStart'}),
            'hora_fim_atividade': TimeInput(format='%H:%M', attrs={'type': 'time', 'id': 'timeIntervalEnd'}),
            'dia_atividade': DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'id': 'activityDay'}),
            'hora_intervalo': DateInput(format='%H:%M', attrs={'type': 'time', 'id': 'timeSlotDuration'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome_servico'].widget.attrs.update({'id': 'activityName'})
        self.fields['descricao'].widget.attrs.update({'id': 'activityDescription'})
        self.fields['responsavel'].widget.attrs.update({'id': 'activityResponsible'})
        self.fields['responsavel'].label_from_instance = lambda obj: "{:<30}{:<30}{:>30}".format(obj.first_name, obj.last_name, obj.email)

        self.fields['responsavel'].label_from_instance = lambda obj: "{:<30}{:<30}{:>30}".format(obj.first_name, obj.last_name, obj.email)


# Inscrever Atividade

class Inscrever_AulaForm(forms.ModelForm):
    class Meta:
        model = Inscrever_Aula
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome_aluno'].widget.attrs.update({'id': 'nomeAula'})
        self.fields['nome_atividade'].widget.attrs.update({'id': 'aula'})


class Inscrever_ServicoForm(forms.ModelForm):
    class Meta:
        model = Inscrever_Servico
        fields = '__all__'

    widgets = {
        'hora_servico': TimeInput(format='%H:%M', attrs={'type': 'time', 'id': 'horarioServico'}),
        'dia_servico': DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'id': 'horarioServico'}),

    }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['aluno'].widget.attrs.update({'id': 'nomeServico'})
        self.fields['servico_atividade'].widget.attrs.update({'id': 'servico'})
        self.fields['responsavel'].widget.attrs.update({'id': 'responsavelServico'})



