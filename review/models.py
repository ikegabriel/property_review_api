from django.db import models
from django.contrib.auth import get_user_model

# from users.views import User
User = get_user_model()


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    property_address = models.CharField(max_length=500)
    property_image = models.ImageField(upload_to='review/images/property_image%y%m%d', blank=True, null=True)
    property_video = models.FileField(upload_to='review/videos/property_video%y%m%d', default='non', null=True)
    apartment_review = models.TextField()
    image1 = models.ImageField(upload_to='review/images/image1%y%m%d', blank=True, null=True)
    amenities_review = models.TextField()
    image2 = models.ImageField(upload_to='review/images/image2%y%m%d', blank=True, null=True)
    landlord_review = models.TextField()
    image3 = models.ImageField(upload_to='review/images/image3%y%m%d', blank=True, null=True)
    country = models.CharField(max_length=500)
    state = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
    helpful = models.ManyToManyField(User, blank=True, related_name='helpful_count')

    def __str__(self):
        return "{} by {}".format(self.property_address, self.author)

    def helpful_count(self):
        return self.helpful.count()

class TestReview(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='review/images/test', blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    date = models.DateField(auto_now_add=True, null=True)