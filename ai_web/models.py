from django.db import models
class Article(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(default='')
    year = models.PositiveIntegerField(default=2023)
    imgThumb = models.ImageField(upload_to="images", null=True, blank=True)


    def __str__(self):
        return self.title



    def title_with_year(self):
        return "[{}] {}".format(self.year, self.title)
# Create your models here.
