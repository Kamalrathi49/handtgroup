from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

ACTIVE_CHOICES = (
    ('true', 'TRUE'),
    ('false', 'FALSE')
)

class our_service(models.Model):
    icon = models.FileField(upload_to="icons/")
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=700)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class subscription(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class our_address(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    telephone = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email


class planning_stag(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=700)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.title


class our_project(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=200)
    architects = models.CharField(max_length=500)
    location = models.CharField(max_length=200)
    area = models.CharField(max_length=100)
    manufactures = models.CharField(max_length=200)
    project_year = models.CharField(max_length=50)
    description = models.TextField(max_length=700)
    image1 = models.ImageField(upload_to="project_images/")
    image2 = models.ImageField(upload_to="project_images/")
    image3 = models.ImageField(upload_to="project_images/")
    is_active = models.BooleanField(default=True)


    def save(self):
        super().save()
        img1 = Image.open(self.image1.path)
        img2 = Image.open(self.image1.path)
        img3 = Image.open(self.image1.path)

        if img1.height > 300 or img1.width > 300 or img2.height > 300 or img2.width > 300 or  img3.height > 300 or img3.width > 300:
            filter_img1 = img1.resize((680,1000))
            filter_img1.save(self.image1.path)
            filter_img2 = img2.resize((680,1000))
            filter_img2.save(self.image2.path)
            filter_img3 = img3.resize((680,1000))
            filter_img3.save(self.image3.path)

            print(":::::::::::SUCESS::::::::::")

    def __str__(self):
        return self.title

class public_review(models.Model):
    RATING_CHOICES = (
    ('one', 'ONE'),
    ('two', 'TWO'),
    ('three', 'THREE'),
    ('four', 'FOUR'),
    ('five', 'FIVE'),
    )
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=700)
    image = models.ImageField(upload_to="review_profile_pic/")
    rating = models.CharField(max_length=10, choices=RATING_CHOICES, default='one')
    role = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class propertys(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=200)
    description = models.TextField(max_length=700)
    image = models.ImageField(upload_to="property_images/")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class our_partner(models.Model):
    partner_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="partner_logo/")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.partner_name


class our_team(models.Model):
    name = models.CharField(max_length=99)
    role = models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)

class top_image(models.Model):
    service_name = models.CharField(max_length=99)
    title = models.CharField(max_length=99)
    description = models.CharField(max_length=99)
    image = models.ImageField(upload_to="top-image/")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
