from django.views.generic import CreateView,ListView
from audio_recorder.views import AudioFileCreateViewMixin
from .models import AudioFile
from .forms import AudioFileForm
from django.shortcuts import render
from django.db.models import F
from django.shortcuts import get_list_or_404, get_object_or_404
import random
from django.core.urlresolvers import reverse,reverse_lazy
from django.http import HttpResponseRedirect,HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import AudioFile,Signup
from .serializers import AudioSerializer,UserSerializer

class AudioList(APIView):

	def get(self,request):
		Audios=AudioFile.objects.all()
		serializer=AudioSerializer(Audios,many=True)
		return Response(serializer.data)

	def post(self,request):
		print('hello')
		print(request)
		serializer=AudioSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):

	def get(self,request):
		Users=Signup.objects.all()
		serializer=UserSerializer(Users,many=True)
		return Response(serializer.data)

	def post(self,request):
		serializer=UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
		



class AudioFileAPICreateView(AudioFileCreateViewMixin):
    model = AudioFile


class AudioFileCRUDCreateView(CreateView):
    model = AudioFile
    form_class = AudioFileForm
class AudioFileListView(ListView):
	model=AudioFile
	context_object_name = 'my_list'
	template_name = 'audio_files/list.html'

def fetch(request):
	obj=AudioFile.objects.all()
	count=obj.count
	n = random.randint(1,5) # returns a random integer
	obj=AudioFile.objects.filter(id=n)
	print(n)
	context = {
		'file':obj,
	}
	return render(request,"audio_files/files.html",context=context)
def index(request):
	return render(request,"index.html",{})

def updateYes(request, pk):
    obj = AudioFile.objects.get(pk=pk)
    obj.yesCount=F('yesCount')+1
    obj.save()
    return HttpResponseRedirect('/dataset/')

def updateNo(request, pk):
    obj = AudioFile.objects.get(pk=pk)
    obj.noCount=F('noCount')+1
    obj.save()
    return HttpResponseRedirect('/dataset/') 