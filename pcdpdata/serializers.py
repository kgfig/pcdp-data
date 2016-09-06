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
        fields = ('id', 'content', 'points', 'choices')
        depth = 1

class UserSerializer(serializers.ModelSerializer):
    answers = ChoiceSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'surname', 'firstname', 'username', 'email', 'answers')
        depth = 1

class AssessmentSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Assessment
        fields = ('id', 'title', 'type', 'questions')
        depth = 1

class ProjectSerializer(serializers.ModelSerializer):
    assessment_list = AssessmentSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'assessment_list')
        depth = 1

