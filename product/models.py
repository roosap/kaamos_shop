from django.db import models
from django.core.validators import MinValueValidator 
from django import forms

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

class ProductIndexPage(Page):
    pass

class ProductPage(Page):

    description = models.CharField(max_length=1000, blank=False, null=True)
    sku = models.IntegerField(blank=False, unique=True)
    price = models.IntegerField(blank=False, default=10000, validators=[MinValueValidator(500)])
    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    search_fields = Page.search_fields + [
        index.SearchField('description'),
        index.SearchField('sku'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel('sku', widget=forms.NumberInput()), 
        FieldPanel('price', widget=forms.NumberInput()),
        ImageChooserPanel("image"),
    ]