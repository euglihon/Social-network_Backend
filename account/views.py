from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required  # функция выполняется только авторизованным юзером
def dashboard(request):
    # загрузка главной страницы, если юзер залогинен
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

'''
ручная обработка логированрия
def user_login(request):
    if request.method == 'POST':
        # если форма отправлена
        form = LoginForm(request.POST)

        if form.is_valid():
            # если форма валидна
            data = form.cleaned_data
            user_name = data['username']
            user_password = data['password']
            # если такого юзера нет вернется user = None
            user = authenticate(request, username=user_name, password=user_password)

            if user is not None:
                # если юзер аутентифицирован
                if user.is_active:
                    # если юзер активен
                    # авторизируем юзера на сайте и сохр. в сессии
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                elif not user.is_active:
                    # если юзер не активен
                    return HttpResponse('Disabled lol')

            elif user is None:
                # если юзер не аутентифицирован
                return HttpResponse('Invalid login')
        else:
            # если форма не валидна
            return render(request, 'account/login.html', {'form': form})

    else:
        # если форма не отправлена
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})
'''