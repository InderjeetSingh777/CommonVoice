from rest_framework import serializers
from .models import AudioFile,Signup
class AudioSerializer(serializers.ModelSerializer):

	class Meta:
		model = AudioFile
		fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = Signup
		fields = '__all__'