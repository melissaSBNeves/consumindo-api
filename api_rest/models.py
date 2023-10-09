from django.db import models

class User(models.Model):
    user_name = models.CharField(verbose_name="Nome completo:", max_length=255, null=False, blank=False,default='')
    user_email = models.EmailField(verbose_name="Email: ", null=False, blank=False, default='')
    user_age = models.IntegerField(verbose_name="Idade",null=False, default=0)


    def __str__(self):
        return f'Nickname: {self.user_nickname} | E-mail: {self.user_email}'
    
