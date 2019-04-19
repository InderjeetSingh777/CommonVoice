from rest_framework import serializers
from .models import AudioFileMixin
class AudioSpeakSerializer(serializers.ModelSerializer):

	class Meta:
		model = AudioFileMixin
		fields = '__all__'
