from django.db import models

# Create your models here.
class Travels(models.Model):
    date = models.DateField()
    time = models.TimeField()
    to = models.CharField(max_length=50)
    driver = models.ForeignKey('login.User', on_delete=models.CASCADE)
    free_seat = models.IntegerField(default=0)
    # create a string representation of the user model
    def __str__(self):
        return self.person.username + ' ' + self.to + ' ' + str(self.date) + ' ' + str(self.time)
    
