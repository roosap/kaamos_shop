from django.db import models
# from django.core.validators import MinValueValidator 
# from django import forms, template

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    max_count = 1

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = models.CharField(max_length=100, blank=True, null=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image"),
        PageChooserPanel("banner_cta"),
    ]

    class Meta:
        verbose_name = "KAAMOS STUDIO HOME PAGE"
        verbose_name_plural = "KAAMOS STUDIO HOME PAGES"

    # child_pages = ['kaamos_shop.ShopPage', 'kaamos_about.AboutPage']

# class ShopPage(Page):
#     child_pages = ['kaamos_shop.ProductPage']

# class AboutPage(Page):
#     pass

# class ProductPage(Page):
#     max_count = 1

#     description = models.CharField(max_length=1000, blank=False, null=True)
#     sku = models.IntegerField(blank=False, unique=True)
#     price = models.IntegerField(blank=False, default=10000, validators=[MinValueValidator(500)])
#     image = models.ForeignKey(
#         "wagtailimages.Image",
#         blank=False,
#         null=True,
#         on_delete=models.SET_NULL,
#         related_name="+",
#     )

#     content_panels = Page.content_panels + [
#         FieldPanel("description"),
#         FieldPanel('sku', widget=forms.NumberInput()), 
#         FieldPanel('price', widget=forms.NumberInput()),
#         ImageChooserPanel("image"),
#     ]