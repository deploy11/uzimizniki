from django.db import models
import uuid
# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    login = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    invitedBy = models.CharField(max_length=500)
    hand_left = models.CharField(max_length=500,default='.')
    hand_right = models.CharField(max_length=500,default='.')
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
    

class Kitoblar(models.Model):
    toplam = models.CharField(max_length=500)
    kitoblar = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.toplam

class Haridlar(models.Model):
    toplam = models.ForeignKey(Kitoblar,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user},{self.toplam} ni tanladi'