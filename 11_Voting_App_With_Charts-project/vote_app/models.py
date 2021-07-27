from django.db import models

class VoteTitle(models.Model):
  question = models.CharField(max_length=1000)
  date = models.DateTimeField(auto_now_add=False)
  
  class Meta:
    verbose_name_plural = "Questions"
  
  def __str__(self):
    return self.question

class Vote(models.Model):
  choice = models.CharField(max_length=100)
  votes=models.PositiveIntegerField(default=0)
  question=models.ForeignKey(VoteTitle, on_delete=models.CASCADE, related_name="question_ref")
  
  def __str__(self):
    return self.choice