from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PagesConfig(AppConfig):
    name = 'studenthome.pages'
    verbose_name = _('StudentHome Pages')
