from django.db import models


class Category(models.Model):
    name_uz = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True)


class Product(models.Model):
    name_uz = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description_uz = models.CharField(max_length=100, null=True, blank=True)
    description_en = models.CharField(max_length=100, null=True, blank=True)
    description_ru = models.CharField(max_length=100, null=True, blank=True)


class Blog(models.Model):
    name_uz = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True)
    date = models.DateField(auto_now_add=True)
    description_uz = models.CharField(max_length=100, null=True, blank=True)
    description_en = models.CharField(max_length=100, null=True, blank=True)
    description_ru = models.CharField(max_length=100, null=True, blank=True)


