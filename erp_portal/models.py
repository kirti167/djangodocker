from django.db import models
from django.contrib.auth.models import User

Roles = (
    ('teacher', 'TEACHER'),
    ('student', 'STUDENT'),
    ('hod','HOD'),
)

sex_choice = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    
)

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=None, null=True)
    role = models.CharField(max_length=50, choices=Roles)

    def __str__(self):
        return self.user.username

COURSE_CHOICES = (
    ('bba', 'BBA'),
    ('bca','BCA'),
    ('mba','MBA'),
    ('mca','MCA'),
    ('cse','CSE'),
    ('it','IT'),
    ('mech','MECH'),
    ('ele','ELE'),
)


class application(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    dob = models.DateField()
    email = models.EmailField(max_length=50)
    contact = models.CharField(max_length=10)
    gender = models.CharField(max_length=6)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    tenth = models.CharField(max_length=2)
    twelth = models.CharField(max_length=2)
    course = models.CharField(max_length=6, choices=COURSE_CHOICES, default='B.Tech')
    def __str__(self):
        return self.firstname


class Dept(models.Model):
    id = models.CharField(primary_key='True', max_length=100)
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class Class(models.Model):
    # courses = models.ManyToManyField(Course, default=1)
    id = models.CharField(primary_key='True', max_length=100)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    sem = models.IntegerField()
    feedues=models.IntegerField(default=0)
    
   

    class Meta:
        verbose_name_plural = 'classes'

    def __str__(self):
        d = Dept.objects.get(name=self.dept)
        return '%s : %d ' % (d.name, self.sem)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, default=1)
    USN = models.CharField(primary_key='True', max_length=100)
    name = models.CharField(max_length=200)
    sex = models.CharField(max_length=50, choices=sex_choice, default='Male')
    DOB = models.DateField(default='1998-01-01')
    image = models.ImageField(upload_to='profile_image', default='default.jpg')

    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    id = models.CharField(primary_key=True, max_length=100)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=50, choices=sex_choice, default='Male')
    DOB = models.DateField(default='1980-01-01')
    post=models.CharField(max_length=50,default='null')
    image = models.ImageField(upload_to='profile_image', default='default.jpg')
    qualification=models.CharField(max_length=20,default="B.Tech")
    #weeklyload=models.IntegerField(default="1")

    def __str__(self):
        return self.name

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    id = models.CharField(primary_key=True, max_length=100)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=50, choices=sex_choice, default='Male')
    DOB = models.DateField(default='1980-01-01')
    post=models.CharField(max_length=50,default='null')
    image = models.ImageField(upload_to='profile_image', default='default.jpg')
    qualification=models.CharField(max_length=20,default="B.Tech")
    def __str__(self):
        return self.name
        
class Subject(models.Model):
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    id = models.CharField(primary_key='True', max_length=50)
    name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=50, default='X')
    #weeklylec=models.IntegerField(default='1')
    
    def __str__(self):
        return self.name


class Assign(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    subj = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    

    class Meta:
        unique_together = (('subj', 'class_id', 'teacher'),)

    def __str__(self):
        cl = Class.objects.get(id=self.class_id_id)
        cr = Subject.objects.get(id=self.subj_id)
        te = Teacher.objects.get(id=self.teacher_id)
        return '%s : %s : %s'"semester" % (te.name, cr.name, cl)

class SubjectAssign(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    subj = models.ForeignKey(Subject, on_delete=models.CASCADE)
    #type=models.CharField(max_length=10,default="Theory",choices=subject_type)

    class Meta:
        unique_together = (( 'class_id','subj'),)
    def __str__(self):
        sname = Class.objects.get(id=self.class_id_id)
        cname = Subject.objects.get(id=self.subj_id)
        return '%s sem: %s ' % (sname, cname.shortname)

#Attndance
class SessionYearModel(models.Model):
    id=models.AutoField(primary_key=True)
    session_start_year=models.DateField()
    session_end_year=models.DateField()
    
class Attendance(models.Model):
    id=models.AutoField(primary_key=True)
    subject_id=models.ForeignKey(Subject,on_delete=models.DO_NOTHING)
    attendance_date=models.DateField()
    # session_year_id=models.ForeignKey(SessionYearModel,on_delete=models.CASCADE)

class AttendanceReport(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    attendance_id=models.ForeignKey(Attendance,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)

class StudentResult(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(Subject,on_delete=models.CASCADE)
    subject_exam_marks=models.FloatField(default=0)
    subject_assignment_marks=models.FloatField(default=0)

class StudentLeaveApp(models.Model):

    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    to_teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    status = models.CharField(max_length=100,null=True)


class AppStatus(models.Model):

    leaveApp = models.ForeignKey(StudentLeaveApp,on_delete=models.CASCADE)
    status = models.CharField(max_length=100,null=True)
    
class TeachLeaveApp(models.Model):

    user = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    to_admin = models.ForeignKey(Admin,on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    status = models.CharField(max_length=100,null=True)

class Fees(models.Model):
    user = models.OneToOneField(Student,on_delete=models.CASCADE)
    
    paid=models.BooleanField(default=False)
    order_id = models.CharField(max_length=100, blank=True)
    paymentid=models.CharField(max_length=100,default=0,blank=True)
    method=models.CharField(max_length=100,default=0,blank=True)
    created_at=models.IntegerField(default=0)
    email=models.CharField(max_length=100,default=0,blank=True)
    contact=models.CharField(max_length=100,default=0,blank=True)
    def __str__(self):
        user=self.user
        paid=self.paid
        if paid:
            return str(user)+" :Paid"
        else:
            return str(user)+" :Not Paid"

        


# Create your models here.
