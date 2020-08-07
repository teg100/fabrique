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
        return questions_query

    def create(self, validated_data):
        validated_data.pop('questions')
        questions = self.check_questions(self.initial_data.get('questions'))
        quiz = Quiz.objects.create(**validated_data)
        [quiz.questions.add(question) for question in questions]
        return quiz

    def update(self, instance, validated_data):
        validated_data.pop('questions')
        questions = self.check_questions(self.initial_data.get('questions'))
        Quiz.objects.filter(id=instance.id).update(**validated_data)
        instance.questions.set('')
        [instance.questions.add(question) for question in questions]
        instance.save()
        return instance


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'question', 'answer']


class ResponseSerializer(serializers.ModelSerializer):

    answers = AnswerSerializer(many=True)

    class Meta:
        model = Response
        fields = ['id', 'uid', 'quiz', 'answers']

    def create(self, validated_data):
        if not validated_data.get('answers'):
            raise serializers.ValidationError('Not answers in report')
        response = Response(uid=validated_data['uid'], quiz=validated_data['quiz'])
        response.save()
        for answer in validated_data.get('answers'):
            response.answers.add(Answer.objects.create(**answer, response=response))
        return response