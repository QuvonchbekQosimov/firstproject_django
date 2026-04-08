from django.db import models

class Category(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Article(models.Model):
    objects = None
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)
    @property

    def get_image(self):
        try:
            return self.image.url
        except:
            return ''


    def __str__(self):
        return self.title