from django.test import TestCase, Client

# Create your tests here.
from .models import Student

class modelTest(TestCase):
    def Create_Data(self, student_number=int(234566), first_name="ayanda", last_name="msomi", field_of_study="IT", gpa=2.6):
        return Student.objects.create(student_number=student_number, first_name=first_name, last_name=last_name, field_of_study=field_of_study, gpa=gpa)
    
    def test_Data(self):
        d = self.Create_Data()
        self.assertTrue(isinstance(d, Student))


c = Client()
response = c.post('/login/', {'username': 'ayanda', 'password': 'sdfghjhgfd!'})
response.status_code, 200
response = c.get
       

