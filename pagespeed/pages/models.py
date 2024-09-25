from django.db import models

class Page(models.Model):
  url1 = models.CharField(max_length=255)
  url2 = models.CharField(max_length=255)
  joined_date = models.DateTimeField(auto_now_add=True, blank=True)

  def __str__(self):
    return f"{self.url1} vs {self.url2}"