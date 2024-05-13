from .models import Users
from django.contrib.auth import forms



class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Users


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Users


class UserFormTemplate(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Users
        exclude = ['user_permissions', 'groups', 'password', 'is_superuser', 'is_staff','last_login', 'date_joined']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'placeholder': field})

        self.fields['grupo_de_acesso'].widget.attrs.update({'name': 'valor'})


class PasswordChangeFormTemplate(forms.PasswordChangeForm):
    class Meta(forms.PasswordChangeForm):
        model = Users
        exclude = ['old_password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        # Remove the old_password field dynamically
        del self.fields['old_password']

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
