from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


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


class Quiz(models.Model):
    title = models.CharField(max_length=400)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    questions = models.ManyToManyField(Question, blank=True, related_name='quizes')
    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.CharField(max_length=512, blank=True)
    response = models.ForeignKey('Response', on_delete=models.CASCADE, related_name='answers')


class Response(models.Model):
    uid = models.PositiveIntegerField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='responses')

