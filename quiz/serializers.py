from rest_framework import serializers
from .models import Quiz, Question, Attempt

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'text', 'correct_answer')

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ('id', 'title', 'description', 'difficulty', 'questions')

class AttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attempt
        fields = ('id', 'user', 'quiz', 'score', 'created_at')
        read_only_fields = ('user', 'created_at')
