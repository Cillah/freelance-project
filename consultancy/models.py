from django.db import models

# Create your models here.
class Training(models.Model):
  training_topic = models.CharField(max_length=200)
  training_poster = models.ImageField(max_length=200,null=True,upload_to="training_poster")
  speaker = models.CharField(max_length=200)
  speaker_image = models.ImageField(max_length=200,null=True,upload_to="training_speaker")
  date = models.DateField()
  timings = models.CharField(max_length=200)
  remarks = models.CharField(max_length=200,null=True)

  def __str__(self) -> str:
    #returns the training topic name as object.
    return self.training_topic