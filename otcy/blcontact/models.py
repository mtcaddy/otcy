from django.db import models

from django.forms import ModelForm
# Create your models here.
TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class AuthorForm(ModelForm):
    class Meta:
        model = Client
        fields = ['first_name','last_name', 'title', 'birth_date']
