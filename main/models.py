from ckeditor.fields import RichTextField
from django.db import models
from solo.models import SingletonModel

class EarningHeader(SingletonModel):
    first_header = RichTextField(config_name='awesome_ckeditor',null=True, blank=True)
    second_header = RichTextField(config_name='awesome_ckeditor',null=True, blank=True)
    third_header = RichTextField(config_name='awesome_ckeditor',null=True, blank=True)
    fourth_header = RichTextField(config_name='awesome_ckeditor',null=True, blank=True)
    fifth_header = RichTextField(config_name='awesome_ckeditor',null=True, blank=True)
    sixth_header = RichTextField(config_name='awesome_ckeditor',null=True, blank=True)
    seventh_header = RichTextField(config_name='awesome_ckeditor',null=True, blank=True)
    eight_header = RichTextField(config_name='awesome_ckeditor',null=True, blank=True)
    nine_header = RichTextField(config_name='awesome_ckeditor',null=True, blank=True)

    class Meta:
        pass
