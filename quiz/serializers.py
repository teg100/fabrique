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


    def get_object_or_none(self, cls,  id_):
        try:
            return cls.objects.get(id=id_)
        except cls.DoesNotExist:
            return None

    def check_questions(self, questions):
        questions_query = []
        for q in questions:
            question = self.get_object_or_none(Question, q.get('id'))
            if question:
                questions_query.append(question)
            else:
                raise serializers.ValidationError({'questions': f'question with id={q.get("id")} does not exist'})

    def create(self, validated_data):
        validated_data.pop('questions')
        questions = self.check_questions(self.initial_data.get('questions'))
        quiz = Quiz.objects.create(**validated_data)
        [quiz.questions.add(question) for question in questions]
        return quiz

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'question', 'text']


class ResponseSerializer(serializers.ModelSerializer):

    answers = AnswerSerializer(many=True)

    class Meta:
        model = Response
        fields = ['id', 'uid', 'quiz', 'answers']

