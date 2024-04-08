import os
from django.core.files import File
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from PIL import Image as PILImage
import uuid
from django.conf import settings

from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from ImageUploadApplication import settings

from ImageUpload.models import ImageModel, MergeAudioModel, MergeTextModel, UnmergeAudioModel, UnmergeImageModel, UnmergeTextModel
from ImageUpload.models import MergeImageModel

def is_image(file):
    try:
        img = PILImage.open(file)
        img.verify()
        return True
    except Exception as e:
        return False

def home(request):
    return render(request, 'index.html')


def merge_text_files(file1, file2):
    # Read content of both files
    with open(file1, 'r') as f1:
        content1 = f1.read()
    with open(file2, 'r') as f2:
        content2 = f2.read()
    
    # Merge content of both files
    merged_content = content1.strip() + ' ' + content2.strip()
    return merged_content

def upload_merge_text(request):
    if request.method == 'POST':
        secretfile = request.FILES.get('secretimg')
        coverfile = request.FILES.get('coverimg')

        # Save the uploaded files to a temporary location
        secretfile_path = os.path.join(settings.MEDIA_ROOT, 'UnMergedTextFile', secretfile.name)
        coverfile_path = os.path.join(settings.MEDIA_ROOT, 'UnMergedTextFile', coverfile.name)
        with open(secretfile_path, 'wb') as f:
            f.write(secretfile.read())
        with open(coverfile_path, 'wb') as f:
            f.write(coverfile.read())

        # Merge the text files
        merged_content = merge_text_files(secretfile_path, coverfile_path)

        # Generate a unique filename for the merged text file
        unique_filename = str(uuid.uuid4()) + '.txt'

        # Save the merged content to a new file
        merged_text_path = os.path.join(settings.MEDIA_ROOT, 'mergedtextfile', unique_filename)
        with open(merged_text_path, 'w') as f:
            f.write(merged_content)

        # Construct the URL for the merged text file
        merged_text_url = os.path.join(settings.MEDIA_URL, 'mergedtextfile', unique_filename)

        context = {'merged_text_url': merged_text_url}

        # Return the path of the merged file to render in the template
        return render(request, 'downloadmergetextfile.html', context)
    return render(request, 'index.html')


def upload_merge_image(request):
    if request.method == 'POST':
        secretimage = request.FILES.get('secretimg')
        secret = request.POST.get('secret')
        coverimage = request.FILES.get('coverimg')
        cover = request.POST.get('cover')
        
        # Check if both files are images
        if is_image(secretimage) and is_image(coverimage):
            # Open the images
            secret_img = Image.open(secretimage)
            cover_img = Image.open(coverimage)
            
            # Resize the images to the same dimensions
            width, height = 500, 500  # Adjust dimensions as needed
            secret_img = secret_img.resize((width, height))
            cover_img = cover_img.resize((width, height))
            
            # Create a new blank image with the required dimensions
            merged_image = Image.new('RGB', (width * 2, height))
            
            # Paste the secret image on the left side and cover image on the right side
            merged_image.paste(secret_img, (0, 0))
            merged_image.paste(cover_img, (width, 0))
            
            # Generate a unique filename for the merged image
            unique_filename = str(uuid.uuid4()) + '.jpg'
            merged_image_path = os.path.join(settings.MEDIA_ROOT, 'mergedimages', unique_filename)
            
            # Save the merged image to the media directory with the unique filename
            merged_image.save(merged_image_path)
            
            # Pass the URL of the merged image to the template
            merged_image_url = os.path.join(settings.MEDIA_URL, 'mergedimages', unique_filename)
            context = {'merged_image_url': merged_image_url}
            
            image_obj = MergeImageModel.objects.create(secret=secret, secret_image=merged_image_url, cover=cover, cover_image=merged_image_url)
            
            # Render the template with the merged image URL
            return render(request, 'downloadmergeimagefile.html', context)
        else:
            messages.error(request, 'Please upload valid image files.')
            return redirect('home')
    else:
        return redirect('home')


# def upload_merge_image(request):
#     if request.method == 'POST':
#         secretimage = request.FILES.get('secretimg')
#         secret = request.POST.get('secret')
#         coverimage = request.FILES.get('coverimg')
#         cover = request.POST.get('cover')
        
#         image_obj = MergeImageModel.objects.create(secret=secret, secret_image=secretimage, cover=cover, cover_image=coverimage)
#         messages.success(request, 'The Merge Image has been saved successfully.')
#         return render(request, 'downloadmergeimagefile.html', {'image_obj': image_obj})

def upload_image(request):
    if request.method == 'POST':
        secretimage = request.FILES.get('secretimg')
        secret = request.POST.get('secret')
        coverimage = request.FILES.get('coverimg')
        cover = request.POST.get('cover')
        if secretimage and coverimage and is_image(secretimage) and is_image(coverimage):
            image_obj = UnmergeImageModel.objects.create(unmerge_secret_img=secret, secretimage=secretimage, unmerge_cover_img=cover, cover_image=coverimage)
            messages.success(request, 'The UnmergeImage has been saved successfully.')
            return render(request, 'downloadumergeimagefile.html', {'image_obj': image_obj})
        else:
            messages.error(request, 'Invalid image file.')
    return redirect('home')


# def upload_merge_text(request):
#     if request.method == 'POST':
#         secretimage = request.FILES.get('secretimg')
#         secret = request.POST.get('secret')
#         coverimage = request.FILES.get('coverimg')
#         cover = request.POST.get('cover')
#         image_obj = MergeTextModel.objects.create(secret=secret, secret_text=secretimage, cover=cover, cover_text=coverimage)
#         messages.success(request, 'The Merge Text file has been saved successfully.')
#     return render(request, 'downloadmergetextfile.html', {'image_obj': image_obj})

def upload_unmerge_text(request):
    if request.method == 'POST':
        secretimage = request.FILES.get('secretimg')
        secret = request.POST.get('secret')
        coverimage = request.FILES.get('coverimg')
        cover = request.POST.get('cover')
        image_obj = UnmergeTextModel.objects.create(unmerge_secret_text=secret, secrettext=secretimage, unmerge_cover_text=cover, cover_text=coverimage)
        messages.success(request, 'The Unmerge Text file has been saved successfully.')
        return render(request, 'downloadunmergetextfile.html', {'image_obj': image_obj})


def upload_merge_audio(request):
    if request.method == 'POST':
        secretimage = request.FILES.get('secretimg')
        secret = request.POST.get('secret')
        coverimage = request.FILES.get('coverimg')
        cover = request.POST.get('cover')
        
        
    return render(request, 'downloadmergemusic.html')

import os
import uuid
from django.conf import settings
from django.shortcuts import render
from pydub import AudioSegment

def upload_unmerge_audio(request):
    if request.method == 'POST':
        # Get the uploaded file
        uploaded_file = request.FILES['audio_file']
        
        # Generate a unique filename
        unique_filename = str(uuid.uuid4()) + '.mp3'
        merged_audio_url = os.path.join(settings.MEDIA_URL, 'uploadunmergeaudio', unique_filename)
        
        # Load the audio file using Pydub
        audio = AudioSegment.from_file(uploaded_file)

        # Duration of the audio in milliseconds
        audio_duration = len(audio)

        # Define the start and end times for slicing (in milliseconds)
        start_time_1 = 0
        end_time_1 = audio_duration // 2  # Half of the duration
        start_time_2 = end_time_1
        end_time_2 = audio_duration

        # Slice the audio
        sliced_audio_1 = audio[start_time_1:end_time_1]
        sliced_audio_2 = audio[start_time_2:end_time_2]

        # Export the sliced audio to new files
        sliced_audio_path_1 = 'sliced_audio_1.mp3'
        sliced_audio_path_2 = 'sliced_audio_2.mp3'
        sliced_audio_1.export(os.path.join(settings.MEDIA_ROOT, 'uploadunmergeaudio', sliced_audio_path_1), format="mp3")
        sliced_audio_2.export(os.path.join(settings.MEDIA_ROOT, 'uploadunmergeaudio', sliced_audio_path_2), format="mp3")

        # Pass the URLs of the sliced audio files to the template context
        context = {
            'part1_url': os.path.join(settings.MEDIA_URL, 'uploadunmergeaudio', sliced_audio_path_1),
            'part2_url': os.path.join(settings.MEDIA_URL, 'uploadunmergeaudio', sliced_audio_path_2),
        }

        # Render the template with the context
        return render(request, 'downloadunmergemusic.html', context)

    # If the request method is not POST, render an empty form
    return render(request, 'upload_audio_unmerge.html')


