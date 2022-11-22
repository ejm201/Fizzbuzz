from django.db import models

# Create your models here.
class Fizzbuzz(models.Model):
    fizzbuzz_id = models.AutoField(primary_key=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    user_agent =  models.TextField(blank=True)
    message = models.TextField(blank=False)
 
class Meta:
    ordering = ["fizzbuzz_id"]

def __str__(self) -> str:
        return f"{self.fizzbuzz_id} | {self.creation_date} | {self.useragent} | {self.message}"