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
    



class OpenRole(models.Model):

    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    summary = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title



class JobApplication(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

    role_title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    
    experience = models.CharField(max_length=100)
    linkedin_url = models.URLField()
    cover_note = models.TextField(
        blank=True,
        null=True
    )

    resume = models.FileField(
        upload_to='job_applications/'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    applied_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name} - {self.role_title}"





class LiveWebinar(models.Model):

    title = models.CharField(max_length=255, default="Future of Oracle Cloud Infrastructure")
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    speaker = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='webinars/'
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.speaker} - {self.date}"
    

class WebinarRegistration(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    linkedin_url = models.URLField()
    webinar_title = models.CharField(
        max_length=255
    )

    registration_status = models.CharField(
        max_length=20,
        choices=[
            ('Registered', 'Registered'),
            ('Attended', 'Attended'),
            ('Cancelled', 'Cancelled'),
        ],
        default='Registered'
    )

    registered_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = (
            'email',
            'webinar_title'
        )

    def __str__(self):
        return (
            f"{self.first_name} "
            f"{self.last_name}"
        )    
    


class VideoShowcase(models.Model):

    title = models.CharField(
        max_length=255
    )

    youtube_url = models.URLField()

    is_featured = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title    