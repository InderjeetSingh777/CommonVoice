from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from .views import AudioFileAPICreateView, AudioFileCRUDCreateView,fetch,AudioFileListView,index,updateYes,updateNo

urlpatterns = [
    url(r'^audio-files/$',
        AudioFileAPICreateView.as_view(create_field='audio_file'),
        name='audio-file-api-create'),
    url(r'^audio-files/new$',
        AudioFileCRUDCreateView.as_view(),
        name='audio-file-crud-create'),
    url(r'^dataset/$',fetch,name='fetch'),
    url(r'^list/$',AudioFileListView.as_view(),name='list'),
    url(r'^$',index,name='index'),
    url(r'^updateYes/(?P<pk>\d+)/$',updateYes,name='updateYes'),
    url(r'^updateNo/(?P<pk>\d+)/$',updateNo,name='updateNo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
