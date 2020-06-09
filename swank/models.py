from django.db import models

# Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    favorite = models.CharField(max_length=255, null=True, blank=True)

class SiteModel(models.Model):
    name = models.CharField(max_length=100)
    SITE_CHOICES = [
        ('blog', 'ブログサイト'),
        ('promo', 'プロモーションサイト'),
        ('portfo', 'ポートフォリオサイト'),
        ('ecsite', 'ECサイト'),
        ('corp', 'コーポレートサイト'),
        ('recru', 'リクルートサイト'),
        ('landing', 'ランディングページ'),
    ]
    sitekind = models.CharField(max_length=20, choices=SITE_CHOICES, default='blog')
    siteurl = models.URLField(max_length=100)
    gooduser = models.CharField(max_length=255, null=True, blank=True)
    postuser = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='')

class Comment(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    site = models.ForeignKey(SiteModel, on_delete=models.CASCADE)
    comment = models.TextField()