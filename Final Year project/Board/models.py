from django.db import models
from django.contrib import admin

# Create your models here.My Models

class Name(models.Model):

    Firstname=models.CharField(max_length =30)
    Surname=models.CharField(max_length =30)
    
    def __unicode__(self):
        return self.Firstname + " " + self.Surname

class IndexNumber(models.Model):
    
    IDnum=models.CharField(max_length = 20)
    names = models.ForeignKey(Name) #link to Name class
	
    def __unicode__(self):
        return self.IDnum

class Course(models.Model):

    Course_name= models.CharField(max_length = 20)
    Course_index= models.CharField(max_length = 10)
    
    def __unicode__(self):
        return self.Course_name

class Grade(models.Model):
    gradelist= (
('4.00','A'),
('3.75','A-'),
('3.50','B+'),
('3.00','B'),
('2.50','C+'),
('2.00','C'),
('1.50','D'),
('1.00','E'),
('0.00','F'),
)
    course=models.ForeignKey(Course)
    Index = models.ForeignKey(IndexNumber)
    score = models.CharField(max_length=5, choices= gradelist)


 ##   def __unicode__(self):
  ##      return self.score
    
'''class Foo(models.Model):
YEAR_IN_SCHOOL_CHOICES = (
('FR', 'Freshman'),
('SO', 'Sophomore'),
('JR', 'Junior'),
('SR', 'Senior'),
('GR', 'Graduate'),
)
year_in_school = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES)'''


admin.site.register(Name)
admin.site.register(IndexNumber)
admin.site.register(Course)
admin.site.register(Grade)

