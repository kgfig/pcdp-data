from django.test import TestCase
from pcdpdata.models import Project, Assessment

class ProjectModelTest(TestCase):

    def test_save_and_retrieve_project(self):
        project = Project(name='CTAPS')
        project.save()
        saved = Project.objects.first()
        self.assertEqual(project, saved)

class AssessmentModelTest(TestCase):

    def testa_save_and_retrieve_assessment(self):
        ctaps = Project(name='CTAPS')
        ctaps.save()

        assessment = Assessment(title='Quiz 1A', original_id=1, type=3)
        assessment.project = ctaps
        assessment.save()
        
        saved = Assessment.objects.first()
        self.assertEqual(assessment, saved)
        self.assertEqual(ctaps, saved.project)
