from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Document(models.Model):

    title = models.CharField(max_length=200, unique=True)
    doc_type = models.CharField(max_length=50)
    doc_file = models.FileField(upload_to='document_files', blank=True)
    pages = models.PositiveIntegerField()
    authors = models.CharField(max_length=50,blank=True)

    def __str__(self):

        return  f'Title : {self .title}\n'+\
                f'Type : {self.doc_type}\n'+\
                f'Pages : {self.pages}\n'+\
                f'Authors : {self.authors}\n'
