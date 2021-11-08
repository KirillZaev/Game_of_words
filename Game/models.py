from django.db import models
from django.urls import reverse


class Word(models.Model):
    # модель для слова, которое будет относиться к одной из тем
    topic_choices = (
        ("PL", "Растения"),
        ("AN", "Животные"),
        ("TW", "Города"),
        ("NM", "Имена")
    )
    word = models.CharField("Слово", max_length=100)
    topic = models.CharField("Тема", max_length=2, choices=topic_choices)
    first = models.CharField("Первая буква", max_length=1, blank=True)
    last = models.CharField("Последняя буква", max_length=1, blank=True)

    def __str__(self):
        return self.word.title()

    def get_absolute_url(self):
        return reverse('instruction')
