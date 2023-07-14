from django.db import models
from filer.fields.image import FilerImageField

class Slider(models.Model):

	my_order = models.PositiveIntegerField(
		default=0,
		blank=False,
		null=False
	)

	class Meta:
		ordering = ['my_order']

	def __str__(self) -> str:
		return f'slider with id {self.id}'

## Create your models here.
class Image(models.Model):
    
	slider = models.ForeignKey(
		Slider,
		on_delete=models.CASCADE,
		null=True
	)
	image = FilerImageField(
		on_delete=models.CASCADE,
		related_name="image"
	)
	my_order = models.PositiveIntegerField(
		default=0,
		blank=False,
		null=False
	)

	class Meta:
		ordering = ['my_order']

	def __str__(self) -> str:
		return str(self.image)