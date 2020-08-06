from rest_framework import serializers
from .models import *


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['url', 'id', 'text', 'type', 'choises']


class QuizSerializers(serializers.HyperlinkedModelSerializer):

    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ['url', 'id', 'title', 'start_date', 'end_date', 'description',
                  'is_active', 'questions']

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'question', 'text']


class ResponseSerializer(serializers.ModelSerializer):

    answers = AnswerSerializer(many=True)

    class Meta:
        model = Response
        fields = ['id', 'uid', 'quiz', 'answers']

