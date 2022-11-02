from django.db import models

# Create your models here.


class Cloth(models.Model):
    question_text = models.CharField(max_length=200)
    is_used = models.BooleanField(default=True, help_text='中古ならTrue')
    votes = models.IntegerField(default=0)
    answer = models.CharField(max_length=300)
    ans1 = models.CharField(max_length=300)
    ans2 = models.CharField(max_length=300)


class Cloth2(models.Model):
    question_text = models.CharField(max_length=200)
    is_used = models.BooleanField(default=True, help_text='中古ならTrue')
    votes = models.IntegerField(default=0)
    answer = models.CharField(max_length=300)
    ans1 = models.CharField(max_length=300)
    ans2 = models.CharField(max_length=300)


class Cloth3(models.Model):
    question_text = models.CharField(max_length=200)
    is_used = models.BooleanField(default=True, help_text='中古ならTrue')
    votes = models.IntegerField(default=0)
    answer = models.CharField(max_length=300)
    ans1 = models.CharField(max_length=300)
    ans2 = models.CharField(max_length=300)
    images = models.ImageField(upload_to='')
