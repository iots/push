from django.db import models

# Create your models here.

class PushModel(models.Model):
    push_message = models.CharField(verbose_name='推送消息',max_length=100)
    push_url = models.URLField(verbose_name='推送URL')

    def __str__(self):
        return self.push_message
