from django.contrib.auth.models import User
from django.db import models

class Faculty(models.Model):
    Name=models.CharField(max_length=30)
    Department=models.CharField( max_length=50)
    Designation=models.CharField(max_length=50)
    Email = models.EmailField(max_length=254,default="null")
    def __str__(self):
        return self.Name
        
class JournalPublication(models.Model):
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE ,related_name="JournalPublication")
    Paper_title=models.CharField(max_length=70)
    Year = models.DateField()
    Co_Author = models.CharField(max_length=30, blank=True, null=True)
    Volume = models.IntegerField()
    Publisher = models.CharField(max_length=50)
    Indexing=models.IntegerField()
    def __str__(self):
        return self.Paper_title

class BookPublication(models.Model):
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE ,related_name="BookPublication")
    Book_title=models.CharField(max_length=70)
    # chapters or book + chapter namess to be added
    Year = models.DateField()
    Co_Author = models.CharField(max_length=30 ,blank=True, null=True)
    Edition = models.IntegerField()
    Publisher = models.CharField(max_length=50)
    def __str__(self):
        return self.Book_title

class ConfrencePublication(models.Model):
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE ,related_name="ConfrencePublication")
    Organizer=models.CharField(max_length=70)
    Year = models.DateField()
    Co_Author = models.CharField(max_length=30 ,blank=True, null=True)
    Proceeding=models.IntegerField()
    # national international
    def __str__(self):
        return self.Organizer
