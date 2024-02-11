from PIL import Image
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Courses(models.Model):
    slug = models.SlugField('Slug', unique=True)
    title = models.CharField('Title', max_length=100)
    desc = models.TextField('Description')
    img = models.ImageField('Image', default='course-default.png', upload_to='course_img')

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.img.path)
        if img.height > 300 or img.width > 300:
            resize = (300, 300)
            img.thumbnail(resize)
            img.save(self.img.path)

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    text = models.TextField('Text')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name='Course')

