from django.db import models
import datetime

class WebApp(models.Model):
    pc = models.CharField(max_length=1000)

    def __str__(self):
        return self.pc