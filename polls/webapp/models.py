from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=300, verbose_name='Вопрос')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Choice(models.Model):
    text = models.TextField(max_length=500, verbose_name='Вариант ответа')
    poll = models.ForeignKey('webapp.Poll', related_name='choices', on_delete=models.CASCADE, verbose_name='Опрос')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответов'
