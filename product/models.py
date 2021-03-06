from django.db import models
from django.core.validators import MinValueValidator 
from django import forms
from decimal import Decimal

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

class ProductIndexPage(Page):
    subpage_types = ['product.ProductPage']

class ProductPage(Page):

    description = models.CharField(max_length=1000, blank=False, null=True)
    sku = models.IntegerField(blank=False, unique=True)
    price = models.DecimalField(blank=False, default=100, max_digits=10, decimal_places=2, validators=[MinValueValidator(5)])
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