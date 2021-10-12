from django.db import models

from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel

from modelcluster.fields import ParentalKey


class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )

class ContactPage(AbstractEmailForm):

    template = "contact/contact_page.html"
    landing_page_template = "contact/contact_page_landing.html"

    intro = RichTextField(blank=False, null=True)
    thank_you_text = RichTextField(blank=False, null=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro', classname="full"),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address'),
                FieldPanel('to_address'),
            ]),
            FieldPanel("subject"),
        ], heading="Email Settings"),
    ]

    subpage_types = []