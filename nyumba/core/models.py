from django.db import models

# Create your models here.
CATEGORY_CHOICES=[
    ("BS","bedsitter"),
    ("V","villa"),
    ("M","mansion"),
    ("B","Bungalow")
]
class Houses(models.Model):
    category=models.CharField(max_length=24,choices=CATEGORY_CHOICES)
    description=models.TextField()
    rental_price=models.IntegerField()
    buying_price=models.IntegerField()
    location=models.CharField(max_length=20)
    image_1=models.ImageField(upload_to="houses")#uploads to media folder but under a folder for houses
    image_2=models.ImageField(upload_to="houses")
    image_3=models.ImageField(upload_to="houses")
    uploaded=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category + "---->" + self.location
    
    class Meta:
        verbose_name_plural="Houses" #hii ni ya kutoa extra s kwa the name yenye ni default
    



