from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm


@login_required
def image_create(request):
    if request.method == 'POST':
        # форма отправлена
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # данные валидны
            data = form.cleaned_data
            # создаём новый объект
            new_item = form.save(commit=False)
            # добавляем текущего пользователя к объекту
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successfully')
            # перенаправлю пользователя на страницу сохр. изображения
            return redirect(new_item.get_absolute_url())
    else:
        # заполняем форму из GET запроса
        form = ImageCreateForm(data=request.GET)
    return render(request, 'images/image/create.html', {'section': 'images', 'form': form})