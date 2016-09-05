from rest_framework import serializers
from .models import Project, Assessment, Question, Choice, User

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('content', 'correct', 'letter')

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Question
        fields = ('content', 'points', 'choices')
        depth = 1

class AssessmentSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Assessment
        fields = ('title', 'type', 'questions')
        depth = 1

class User(serializers.ModelSerializer):
    answers = ChoiceSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ('surname', 'firstname', 'username', 'email', 'answers')
        depth = 1
