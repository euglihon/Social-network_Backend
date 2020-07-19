from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):
    # базовые поля формы
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    # доп поля формы
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    # функция сверки первого и второго поля
    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Passwords dont math')
        return data['password']