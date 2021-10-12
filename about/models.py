from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class AboutPage(Page):
    about_text = RichTextField(blank=False, null=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('about_text', classname="full"),
        ImageChooserPanel("image"),
    ]

    subpage_types = []