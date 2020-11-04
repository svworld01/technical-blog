from django.db import models
from django.contrib.auth.models import User
from myproject.utils import unique_slug_generator
from django.db.models.signals import pre_save
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
STATUS_CHOICES = ( 
   ('draft', 'Draft'), 
   ('published', 'Published'), 
)
CATEGORY_CHOICES = (
   ('programming', 'Programming'),
   ('ds', 'Data Structure'),
   ('algo', 'Algorithm'),
   ('tech', 'Tech Update'),
   ('life', 'Life Learning')
)
class Post(models.Model):
   title = models.CharField(max_length = 250, unique = True) 
   slug = models.SlugField(max_length=500, null=True, blank=True, unique=True)
   excert = models.TextField()
   content =RichTextUploadingField()
   cover = models.ImageField(upload_to='pics')
   published_at = models.DateTimeField(auto_now_add = True) 
   updated = models.DateTimeField(auto_now = True) 
   status = models.CharField(max_length = 10, choices = STATUS_CHOICES, default ='draft')
   category = models.CharField(max_length = 50, choices = CATEGORY_CHOICES, default ='ds')
   author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

   class Meta:
      ordering = ('-published_at',)

   def __str__(self):
       return self.title

def slug_generator(sender, instance, *args, **kwargs):
   if not instance.slug:
      instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Post)