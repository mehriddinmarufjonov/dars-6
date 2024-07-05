from django.db import models

class Construction(models.Model):
    area = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.area}'
    
    
class Organization(models.Model):
    Construction = models.ForeignKey(Construction, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description  = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
    

class Building(models.Model):
    Organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    construction = models.ForeignKey(Construction, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    floor = models.IntegerField()
    lift = models.BooleanField()


    def __str__(self):
        return f'{self.name}'