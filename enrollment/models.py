from django.db import models

class Student(models.Model):
    # Basic Info
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    course = models.CharField(max_length=50, default="BSIT")
    year_level = models.CharField(max_length=20, default="3rd Year")
    
    # Personal Info
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    birth_date = models.DateField()
    
    # Background Info
    previous_school = models.CharField(max_length=100)
    guardian_name = models.CharField(max_length=100)
    guardian_contact = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.student_id} - {self.last_name}, {self.first_name}"