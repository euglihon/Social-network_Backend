from django import forms
from .models import Image

from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        # скрываем поле url от пользователей для работы через JS
        widgets = {'url': forms.HiddenInput, }

        # автоматический !!!clean!!! метод, вызывается когда обращаемся к .is_valid()
        def clean_url(self):
            # проверка ссылки из скрытого инпута (должна оканчиваться на jpg или  jpeg)
            url = self.cleaned_data['url']
            valid_extensions = ['jpg', 'jpeg']
            extensions = url.rsplit('.', 1)[1].lower()
            if extensions not in valid_extensions:
                raise forms.ValidationError('The given URL does not match valid image extensions')
            return url

        # переопределяем метод save только в случае ImageCreateForm
        def save(self, force_insert=False, force_update=False, commit=True):
            # создаём объект
            image = super(ImageCreateForm, self).save(commit=False)
            # получаем урл изображения
            image_url = self.cleaned_data['url']
            # генерируем название изображения
            image_name = f'{slugify(image.title)}.{image_url.rsplit(".", 1)[1].lower()}'

            # скачиваем файл изображения
            response = request.urlopen(image_url)
            # сохраняем объект с изображением но не сохраняем в бд
            image.image.save(image_name, ContentFile(response.read()), save=False)

            # сохраняем объект в базу данных только если commit=True
            if commit:
                image.save()
            return image