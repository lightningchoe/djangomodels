from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50, null=False)
    user = models.CharField(max_length=10, null=False)
    content = models.TextField()
    view_count = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add = True)