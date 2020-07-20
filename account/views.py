from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import UserRegisterForm, UserEditProfile, ProfileEditProfile, UserEditPassword
from .models import Profile
from django.contrib.auth.models import User


@login_required  # функция выполняется только авторизованным юзером
def dashboard(request):
    # загрузка главной страницы, если юзер залогинен
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def register(request):
    # Обработка регистрации пользователей
    user_form = UserRegisterForm(request.POST)
    if user_form.is_valid():
        # Если форма валидна создаём нового пользователя но не отправляем в БД
        new_user = user_form.save(commit=False)
        # На базе получ. поля сетаем пароль юзеру
        new_user.set_password(user_form.cleaned_data['password'])
        # Отправляем юзера в БД
        new_user.save()
        # Создаём пустой расширенный профиль пользователя (для послед. ввода доп. данных)
        Profile.objects.create(user=new_user)

        return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        # если форма не отправлена
        user_form = UserRegisterForm()
    return render(request, 'account/register.html', {'user_form': user_form})


# Обработка редактирования профиля пользователя
@login_required
def edit_profile(request):
    # если форма отправлена
    if request.method == 'POST':
        user_form = UserEditProfile(instance=request.user, data=request.POST)
        profile_form = ProfileEditProfile(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

    # если форма не отправлна
    else:
        user_form = UserEditProfile(instance=request.user)
        profile_form = ProfileEditProfile(instance=request.user.profile)

    return render(request, 'account/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})


# Обработка смены пароля
@login_required
def password_change(request):
    if request.method == 'POST':
        password_form = UserEditPassword(instance=request.user, data=request.POST)

        if password_form.is_valid():
            instanse = password_form.save(commit=False)
            instanse.user = request.user
            if instanse.check_password(password_form.cleaned_data['old_password']):
                instanse.set_password(password_form.cleaned_data['new_password'])
                instanse.save()
                return render(request, 'account/dashboard.html')

    else:
        password_form = UserEditPassword(instance=request.user)

    return render(request, 'account/edit_password.html', {'password_form': password_form})
