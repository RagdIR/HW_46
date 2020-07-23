from django.db import models

STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

class Note(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Название')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    status = models.CharField(max_length=20, default='new', verbose_name="Не проверено")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')


    def __str__(self):
        return "{}. {}".format(self.pk, self.title)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
