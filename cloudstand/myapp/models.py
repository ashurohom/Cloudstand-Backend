from django.db import models


class HeroSlider(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='hero_slider/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title