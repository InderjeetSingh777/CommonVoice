from django import http
from django.views.generic.base import View
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import AudioFileMixin
from .serializers import AudioSpeakSerializer
class SpeakList(APIView):

    def get(self,request):
        SpeakAudios=AudioFileMixin.objects.all()
        serializer=AudioSpeakSerializer(SpeakAudios,many=True)
        return Response(serializer.data)

    def post(self):
        pass

class AudioFileCreateViewMixin(View):
    model = None
    create_field = None

    def create_object(self, audio_file):
        return self.model.objects.create(**{self.create_field: audio_file})

    def post(self, request):
        audio_file = request.FILES.get('audio_file', None)

        if audio_file is None:
            return http.HttpResponseBadRequest()

        result = self.create_object(audio_file)
        result.save()
        print(result.audio_file.url)
        return http.JsonResponse({
            'id': result.pk,
            'url': result.audio_file.url,
        }, status=201)
