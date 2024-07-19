from django.db import models

class Mainsection(models.Model):
    Description = models.CharField(max_length=200)
    showcaseimg = models.ImageField(upload_to='showcaseimage/')

    def __str__(self):
        return self.Description
    
class subsection(models.Model):
    Name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='profileimage/', null=True, blank=True)
    personalsummary = models.CharField(max_length=500)
    featuredskills = models.ImageField(upload_to='skillicon/', null=True, blank=True)

    def __str__(self):
        return self.Name
    
class Portfolio(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField(blank=True)

    def __str__(self):
        return self.name
    
class portfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name='img', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='Portfolio/sampleimages')
