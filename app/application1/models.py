from django.db import models


class HEADMAN(models.Model):
    Hrealy = models.DateField('Действительно до')
    Hitem = models.CharField('Предмет',max_length=25)
    Hexercise = models.TextField('Задание')
    Hdata = models.DateField('Дата публикации')

    def __str__(self):
        return self.Hitem

    class Meta:
        verbose_name = 'Домашняя работа'
        verbose_name_plural = 'Домашняя работа'



class TEACHER(models.Model):
    Trealy = models.DateField('Действительно до')
    Tmessage = models.TextField('Сообщение')
    Tdata = models.DateField('Дата публикации')

    def __str__(self):
        return self.Tmessage

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

