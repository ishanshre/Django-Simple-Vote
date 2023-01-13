from django.db import models
from django.urls import reverse
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.question_text
    
    def get_absolute_url(self):
        return reverse("core:detail", args=[self.id])

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    choice_text = models.CharField(max_length=500)
    votes = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.choice_text