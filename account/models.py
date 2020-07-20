from django.db import models
from django.conf import settings


# расширение функционала базового класса User
class Profile(models.Model):
    # связь one-to-one с базовым классом
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    data_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)  # Pillow

    def __str__(self):
        return f'Profile for user{self.user.username}'