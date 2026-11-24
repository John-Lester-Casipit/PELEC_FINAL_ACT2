from django.db import models

class UserProfile(models.Model):
    full_name = models.CharField(max_length=120, default="John Lester Casipit")
    bio = models.CharField(max_length=255, default="BSIT-3B Student | Aspiring Full-Stack Developer")
    course = models.CharField(max_length=120, default="Bachelor of Science in Information Technology")
    location = models.CharField(max_length=120, default="Lucena City, Philippines")
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.full_name