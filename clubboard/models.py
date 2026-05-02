from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Club(models.Model):
    authors = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)
    title = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    days = models.TextField(max_length = 100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    sponsor = models.CharField(max_length = 50)
    description =  models.CharField(max_length = 100)
    interest = models.IntegerField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Post(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='posts')
    authors = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text   

    @property
    def published_replies(self):
        return self.replies.filter(published_date__lte=timezone.now()).order_by('created_date')

class reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replies')
    authors =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text