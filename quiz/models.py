from django.db import models


class Question(models.Model):

    TEXT = 'text'
    RADIO = 'radio'
    SELECT = 'multiple'

    QUESTION_TYPE = (
        (TEXT, 'text'),
        (RADIO, 'one answer'),
        (SELECT, 'multi answer')
    )

    text = models.CharField(max_length=512)
    type = models.CharField(max_length=40, choices=QUESTION_TYPE)
    choises = models.TextField(blank=True)

    def __str__(self):
        return self.text
