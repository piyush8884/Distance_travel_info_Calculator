from django.db import models
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    subject=models.CharField(max_length=255)
    desc=models.CharField(max_length=355)
    date=models.DateField()#(widget=forms.Textarea, required=True
    def __str__(self):
        return self.name
# Create your models here.
