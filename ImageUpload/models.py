from django.db import models

class MergeImageModel(models.Model):
    secret = models.CharField(max_length=100)
    secret_image = models.ImageField(upload_to='mergeimages/', max_length=250, null=True, default=None)
    cover = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='mergeimages/', max_length=250, null=True, default=None)
    
class ImageModel(models.Model):
    Unmerge = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Unmergeimages/', max_length=250, null=True, default=None)

    
class UnmergeImageModel(models.Model):
    unmerge_secret_img = models.CharField(max_length=100)
    secretimage = models.ImageField(upload_to='Unmergeimages/', max_length=250, null=True, default=None)
    unmerge_cover_img = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='Unmergeimages/', max_length=250, null=True, default=None)
    
class MergeTextModel(models.Model):
    secret = models.CharField(max_length=100)
    secret_text = models.ImageField(upload_to='MergeText/', max_length=250, null=True, default=None)
    cover = models.CharField(max_length=100)
    cover_text = models.ImageField(upload_to='MergeText/', max_length=250, null=True, default=None)
    
class UnmergeTextModel(models.Model):
    unmerge_secret_text = models.CharField(max_length=100)
    secrettext = models.ImageField(upload_to='UnmergeText/', max_length=250, null=True, default=None)
    unmerge_cover_text = models.CharField(max_length=100)
    cover_text = models.ImageField(upload_to='UnmergeText/', max_length=250, null=True, default=None)
    

class MergeAudioModel(models.Model):
    secret = models.CharField(max_length=100)
    secret_audio = models.ImageField(upload_to='MergeAudio/', max_length=250, null=True, default=None)
    cover = models.CharField(max_length=100)
    cover_audio = models.ImageField(upload_to='MergeAudio/', max_length=250, null=True, default=None)
    
class UnmergeAudioModel(models.Model):
    unmerge_secret_audio = models.CharField(max_length=100)
    secretaudio = models.ImageField(upload_to='UnmergeAudio/', max_length=250, null=True, default=None)
    unmerge_cover_audio = models.CharField(max_length=100)
    cover_audio = models.ImageField(upload_to='UnmergeAudio/', max_length=250, null=True, default=None)