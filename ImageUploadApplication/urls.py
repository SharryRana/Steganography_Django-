"""
URL configuration for ImageUploadApplication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ImageUploadApplication import view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', view.home, name='home'),
    path('upload/', view.upload_image, name='upload_unmerge_image'),
    path('merge_upload/', view.upload_merge_image, name='upload_merge_image'),
    path('mergetextuploads/', view.upload_merge_text, name='upload_merge_text'),
    path('uploadunmergetext/', view.upload_unmerge_text, name='upload_unmerge_text'),
    path('mergeaudiouploads/', view.upload_merge_audio, name='upload_merge_audio'),
    path('uploadunmergeaudio/', view.upload_unmerge_audio, name='upload_unmerge_audio'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
