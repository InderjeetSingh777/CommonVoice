from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models


class AudioFile(models.Model):
    audio_file = models.FileField()
    description=models.CharField(max_length=50)
    yesCount=models.IntegerField()
    noCount=models.IntegerField()
    language=models.CharField(max_length=20)

    def __str__(self):
    	return self.description

class Signup(models.Model):
	Name = models.CharField(max_length=50)
	Age =models.IntegerField()
	Gender = models.CharField(max_length=8)
	college = models.CharField(max_length=50)
	current_location = models.CharField(max_length=50)
	district=models.CharField(max_length=50)
	mother_tongue= models.CharField(max_length=50)
	secondary_language=models.CharField(max_length=50)
	image=models.ImageField()

	def __str__(self):
		return self.Name


