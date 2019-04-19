from django.db import models


class AudioFileMixin(models.Model):
	text=models.CharField(max_length=100)
	audio_file=models.FileField()

	def __str__(self):
		return self.text

