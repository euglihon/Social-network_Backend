from django import forms
from django.contrib.auth.models import User
from .models import Profile

# форма регистрации нового пользователя
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


# форма для редактирования модели User (встроенной в Джанго)
class UserEditProfile(forms.ModelForm):
    # базовые поля формы
    class Meta:
        model = User
        fields = ('first_name', 'email')


# форма для редактирования модели Profile (расширяющей модель User)
class ProfileEditProfile(forms.ModelForm):
    # базовые поля формы
    class Meta:
        model = Profile
        fields = ('data_of_birth', 'photo')


# форма смены пароля
class UserEditPassword(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', )

    # доп поля формы
    old_password = forms.CharField(label='Old password', widget=forms.PasswordInput)
    new_password = forms.CharField(label='New password', widget=forms.PasswordInput)
