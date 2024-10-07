from django.contrib.auth.models import User
from django.db.models.fields import forms


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(
            label='Password',
            widget=forms.PasswordInput(
                attrs={
                    'name': 'password',
                    'id': 'id_password',
                    'class': 'input',
                    'v-model': 'password'
                }
            ),
    )
    password_confirm = forms.CharField(
            label='Confirm Password',
            widget=forms.PasswordInput(
                attrs={
                    'name': 'password_confirm',
                    'id': 'id_password_confirm',
                    'class': 'input',
                    'v-model': 'password_confirm'
                }
            ),
    )

    class Meta:
        model = User
        fields = ['username']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm:
            self.add_error('password_confirm', 'Passwords do not match')

        return cleaned_data
