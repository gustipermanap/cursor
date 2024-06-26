from django.db import models

# Create your models here.
class Site(models.Model):
    site_name = models.CharField(max_length=255)
    page_title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.site_name} - {self.page_title}"

