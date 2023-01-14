from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category = models.CharField(("Kategori"), max_length=50)

    
    def __str__(self):
        return self.category
    
class Tagname(models.Model):
    tagname = models.CharField(("Teg"), max_length=50)

    def __str__(self):
        return self.tagname
    
class Post(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE)
    tagname = models.ManyToManyField(Tagname, verbose_name=("Tag name"))
    title = models.CharField(("Başlık"), max_length=50)
    text = models.TextField(("İçerik Yazısı"))
    image = models.FileField(("Post Resmi"), upload_to='', max_length=100)
    date_now = models.DateField(("Tarih"), auto_now_add=True)
    date_time = models.TimeField(("Saat"), auto_now_add=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name=("Yorum Yapılan Post"), on_delete=models.CASCADE)
    user = models.CharField(("Yorum Yapan"), max_length=50)
    email = models.EmailField(("Email"), max_length=254, null=True)
    title = models.CharField(("Yorum Başlığı"), max_length=50)
    text = models.TextField(("Yorum"), max_length=200)
    date_now = models.DateTimeField(("Yorum Zamanı"), auto_now_add=True)

    def __str__(self):
        return self.title
    
class Contacts(models.Model):
    user = models.CharField(("Yorum Yapan"), max_length=50)
    email = models.EmailField(("Email"), max_length=254, null=True)
    title = models.CharField(("Yorum Başlığı"), max_length=50)
    text = models.TextField(("Yorum"), max_length=200)
    date_now = models.DateTimeField(("Yorum Zamanı"), auto_now_add=True)

    def __str__(self):
        return self.user
