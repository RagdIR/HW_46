from django.db import models

STATUS_CHOICES = [
    ('new', 'Новая'),
    ('in_progress', 'В процессе'),
    ('done', 'Сделано')
]


class Note(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Описание')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Новая")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')


    def __str__(self):
        return "{}. {}".format(self.pk, self.title)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
