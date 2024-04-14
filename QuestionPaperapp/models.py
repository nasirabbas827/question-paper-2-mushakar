from django.db import models

class StudyProgram(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    description = models.TextField()
    credits = models.PositiveIntegerField()
    study_program = models.ForeignKey(StudyProgram, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='course_pictures/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

class Exam(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    study_program = models.ForeignKey(StudyProgram, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Paper(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Question(models.Model):
    DifficultyLevelChoices = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Difficult', 'Difficult'),
    ]

    QuestionID = models.AutoField(primary_key=True)
    QuestionText = models.TextField()
    Option1 = models.CharField(max_length=255)
    Option2 = models.CharField(max_length=255)
    Option3 = models.CharField(max_length=255)
    Option4 = models.CharField(max_length=255)
    CorrectOption = models.CharField(max_length=255)
    DifficultyLevel = models.CharField(max_length=10, choices=DifficultyLevelChoices)
    Weightage = models.IntegerField()
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    CourseID = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.QuestionText



class Student(models.Model):
    student_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=100, default='student')
    password = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.TextField()
    date_enrolled = models.DateField()
    study_program = models.ForeignKey(StudyProgram, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.email})"



from django.db import models

class PaperSubmission(models.Model):
    STATUS_CHOICES = [
        ('Submitted', 'Submitted'),
        ('Not Submitted', 'Not Submitted'),
        ('Marked', 'Marked'),
        ('Pass', 'Pass'),
        ('Fail', 'Fail'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    uploaded_file = models.FileField(upload_to='paper_submissions/')
    marks_obtained = models.PositiveIntegerField(null=True, blank=True)
    total_marks = models.PositiveIntegerField(null=True, blank=True)
    comment = models.TextField(blank=True)
    submission_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Submitted')

    def __str__(self):
        return f"{self.student.name}'s submission for {self.exam.name}"

class Notification(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title