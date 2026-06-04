from django.db import models


class HeroSlider(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='hero_slider/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class ContactInquiry(models.Model):

    name = models.CharField(max_length=255)

    email = models.EmailField()

    company = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    phone = models.CharField(max_length=20)

    service_interested = models.CharField(max_length=255)

    message = models.TextField()

    is_contacted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name    