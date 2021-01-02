from django.db import models

import task.constants as cts


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    status = models.CharField(
        max_length=16, choices=cts.STATUS_CHOICES, default=cts.TODO
    )
