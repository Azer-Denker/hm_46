from django.db import models

STATUS_CHOICES = [
    ('new', 'Новый'),
    ('moderated', 'В разработке'),
    ('rejected', 'Сделаные')
]


class Article(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    text_full = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Текст_Полный')
    author = models.CharField(max_length=40, null=False, blank=False, default='Unknown', verbose_name='Автор')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='new', verbose_name='Модерация')
    data = models.DateField(auto_now_add=False, default=None, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')


    def __str__(self):
        return "{}. {}".format(self.pk, self.title)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
