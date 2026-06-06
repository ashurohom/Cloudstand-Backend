from django.db import models
# from rich.json import args


class HeroSlider(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(
        upload_to='hero_slider/',
        help_text='Recommended image size: 1672 × 941 pixels'
    )
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

    key_responsibilities = models.TextField(
        blank=True,
        help_text="Use '.' (Dot) to separate each responsibility."
    )

    requirements = models.TextField(
        blank=True,
        help_text="Use '.' (Dot) to separate each requirement."
    )

    preferred = models.TextField(
        blank=True,
        help_text="Use '.' (Dot) to separate each preferred skill."
    )

    additional_advantage = models.TextField(
        blank=True,
        help_text="Use '.' (Dot) to separate each additional advantage."
    )

    benefits = models.TextField(
        blank=True,
        help_text="Use '.' (Dot) to separate each benefit."
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

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
    speaker = models.CharField(
        max_length=255,
        help_text='For multiple speakers, separate names with a comma (,). Example: Dhananjay G, KARINA PAWAR'
    )
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
    




class TeamCloudStand(models.Model):

    image = models.ImageField(
        upload_to='team_cloudstand/',
    )

    is_hero_image = models.BooleanField(
        default=False,
        help_text='Check this option to display this image in the Hero Section.'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"Team Image {self.id}"
    
    def save(self, *args, **kwargs):

        if self.is_hero_image:
            TeamCloudStand.objects.update(
                is_hero_image=False
            )

        super().save(*args, **kwargs)