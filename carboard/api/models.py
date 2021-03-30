from django.db import models

# Create your models here.
# before sending data to clients, we need to serialize it - JSON as endpoint

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=75)
    date = models.DateTimeField(auto_now_add=True)

class Details(models.Model):
    modelList = [
        ("Abarth", "Abarth"), ("Alfa Romeo", "Alfa Romeo"), ("Aston Martin", "Aston Martin"), ("Audi", "Audi"),
        ("Bentley", "Bentley"),
        ("BMW", "BMW"), ("Bugatti", "Bugatti"), ("Cadillac", "Cadillac"), ("Chevrolet", "Chevrolet"),
        ("Other", "Other"),  # other option for exceptions to list
        ("Citroen", "Citroen"), ("Dacia", "Dacia"), ("Daewoo", "Daewoo")
    ]
    carMake = models.CharField(max_length=50, choices=modelList)
    carModel = models.CharField(max_length=50)  # draw from our predefined model list
    carPaint = models.CharField(max_length=50)
    carVin = models.CharField(max_length=17)  # Always 17 characters max
    carMileage = models.IntegerField()


    def __str__(self):
        return self.title
