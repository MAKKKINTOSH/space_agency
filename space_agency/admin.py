from django.contrib import admin
from .models import Slider, Image
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin, SortableStackedInline


class SLiderImageInline(SortableStackedInline):

	model = Image
	list_display = ['image', 'image_preview']
	extra = 1

	def image_preview(self, obj):
    		return mark_safe(f'<img src="{obj.image.url}">')
	

@admin.register(Slider)
class SliderAdmin(SortableAdminMixin, admin.ModelAdmin):

	list_display = ['id', 'my_order']
	inlines = [SLiderImageInline]