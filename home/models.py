from django.db import models

import _mysql


# class TestUser(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#
#     def __str__(self):
#         return self.name
#
#
# class TestUserInfo(models.Model):
#     the_user = models.ForeignKey(TestUser, on_delete=models.CASCADE)
#     mail = models.CharField(max_length=50)
#     address = models.CharField(max_length=100)
#     location = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.mail


# original DB
# class Products(models.Model):
#     p_title = models.CharField(50)
#     p_net = models.CharField(50)
#     p_launch = models.CharField(50)
#     p_body = models.CharField(50)
#     p_display = models.CharField(50)
#     p_platf = models.CharField(50)
#     p_memory = models.CharField(50)
#     p_camera = models.CharField(50)
#     p_sound = models.CharField(50)
#     p_comms = models.CharField(50)
#     p_features = models.CharField(50)
#     p_battery = models.CharField(50)
#     p_misc = models.CharField(50)
#     p_amount = models.CharField(50)
#     p_category = models.CharField(50)
#     p_bname = models.CharField(50)
#
#     def __str__(self):
#         return self.p_title
#
#
# class ProductImages(models.Model):
#     p_id = models.ForeignKey(Products, on_delete=models.CASCADE)
#     p_image1 = models.TextField()
#     p_image2 = models.TextField()
#     p_image3 = models.TextField()
#
#     def __str__(self):
#         return self.p_id
#
#
# class ProductSite(models.Model):
#     p_id = models.ForeignKey(Products, on_delete=models.CASCADE)
#     p_site = models.TextField()
#
#     def __str__(self):
#         return self.p_id
#
#
# class Review(models.Model):
#     p_id = models.ForeignKey(Products, on_delete=models.CASCADE)
#     comments = models.TextField()
#     rating = models.FloatField()
#
#     def __str__(self):
#         return self.p_id


class ProductsTesting(models.Model):
    p_title = models.CharField(max_length=50)
    p_net = models.CharField(max_length=50)
    p_launch = models.CharField(max_length=50)
    p_body = models.CharField(max_length=50)
    p_display = models.CharField(max_length=50)
    p_platf = models.CharField(max_length=50)
    p_memory = models.CharField(max_length=50)
    p_camera = models.CharField(max_length=50)
    p_sound = models.CharField(max_length=50)
    p_comms = models.CharField(max_length=50)
    p_features = models.TextField()
    p_battery = models.CharField(max_length=50)
    p_misc = models.CharField(max_length=50)
    p_amount = models.CharField(max_length=50)
    p_category = models.TextField()
    p_bname = models.TextField()

    def __str__(self):
        return self.p_title


class ProductImagesTesting(models.Model):
    p_id = models.ForeignKey(ProductsTesting, on_delete=models.CASCADE)
    p_image1 = models.TextField()
    p_image2 = models.TextField()
    p_image3 = models.TextField()

    def __str__(self):
        return self.p_id


class ProductSiteTesting(models.Model):
    p_id = models.ForeignKey(ProductsTesting, on_delete=models.CASCADE)
    p_site = models.TextField()

    def __str__(self):
        return self.p_id


class ReviewTesting(models.Model):
    p_id = models.ForeignKey(ProductsTesting, on_delete=models.CASCADE)
    comments = models.TextField()
    rating = models.FloatField()

    def __str__(self):
        return self.p_id

