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
    p_name = models.CharField(max_length=50)
    technology = models.CharField(max_length=50)
    # announced = models.CharField(max_length=50)
    dimensions = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    sim = models.CharField(max_length=50)
    disp_type = models.CharField(max_length=50)
    disp_size = models.CharField(max_length=50)
    disp_resolution = models.CharField(max_length=50)
    disp_multitouch = models.CharField(max_length=50)
    os = models.CharField(max_length=25)
    chipset = models.CharField(max_length=50)
    cpu = models.CharField(max_length=50)
    gpu = models.CharField(max_length=50)
    card_slot = models.CharField(max_length=50)
    internal_memory = models.CharField(max_length=50)
    wlan = models.CharField(max_length=50)
    bluetooth = models.CharField(max_length=50)
    usb = models.CharField(max_length=80)
    battery = models.CharField(max_length=50)
    colors = models.CharField(max_length=50)
    price = models.IntegerField()
    p_image = models.FileField()
    shop_link = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.p_name


# class ProductImagesTesting(models.Model):
#     p_id = models.ForeignKey(ProductsTesting, on_delete=models.CASCADE)
#     p_image1 = models.FileField()
#     p_image2 = models.FileField()
#     p_image3 = models.FileField()
#
#     def __str__(self):
#         return str(self.p_id)


class ProductSiteTesting(models.Model):
    p_id = models.ForeignKey(ProductsTesting, on_delete=models.CASCADE)
    p_site = models.TextField()

    def __str__(self):
        return self.p_id


class ReviewTesting(models.Model):
    p_id = models.ForeignKey(ProductsTesting, on_delete=models.CASCADE)
    comments = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.email
