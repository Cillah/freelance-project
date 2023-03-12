from django.db import models
import uuid

# Create your models here.
class Training(models.Model):
  id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
  training_topic = models.CharField(max_length=200)
  training_poster = models.ImageField(max_length=200,null=True,upload_to="training_poster")
  speaker = models.CharField(max_length=200)
  speaker_image = models.ImageField(max_length=200,null=True,upload_to="training_speaker")
  date = models.DateField()
  timings = models.CharField(max_length=200)
  remarks = models.CharField(max_length=1000,null=True,blank=True)

  def __str__(self) -> str:
    #returns the training topic name as object.
    return self.training_topic

  @property
  def getSpeakerImage(self):
    """
      Function to retrieve the url of the speaker image
    """
    try:
      url = self.speaker_image.url
    except:
      url = ""
    return url

  @property
  def getTrainingPoster(self):
    """
      Function to retrieve the url of the training poster
    """
    try:
      url = self.training_poster.url
    except:
      url = ""
    return url