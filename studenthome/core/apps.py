from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CoreConfig(AppConfig):
    name = 'studenthome.core'
    verbose_name = _('StudentHome Core Application')
