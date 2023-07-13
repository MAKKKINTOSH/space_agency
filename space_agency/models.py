from django.db import models
from filer.fields.image import FilerImageField

## Create your models here.
class Image(models.Model):
    
	image = FilerImageField(
		on_delete=models.CASCADE,
		related_name="image"
	)
	def __str__(self) -> str:
		return str(self.image)