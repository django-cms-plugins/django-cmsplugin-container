#-*- coding: utf-8 -*-
from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from fields import MultiSelectField
import defaults


class Container(CMSPlugin):
    """
    A plugin that has sub Column classes
    """
    name = models.CharField(_('Name'), max_length=50, null=True)
    width = models.CharField(_('Width'), choices=defaults.CONTAINER_WIDTH_CHOICES,
        default=defaults.CONTAINER_WIDTH_CHOICES[0][0], max_length=50,
        help_text=_('Width of container'))
    classes = MultiSelectField(max_length=250, blank=True, choices=defaults.CONTAINER_CLASS_CHOICES)

    def __unicode__(self):
        return _(u"%s columns") % self.cmsplugin_set.all().count()


class Grid(CMSPlugin):
    """
    A Column for the MultiColumns Plugin
    """

    width = models.CharField(_('Width'), choices=defaults.CONTAINER_WIDTH_CHOICES,
        default=defaults.CONTAINER_WIDTH_CHOICES[0][0], max_length=50,
        help_text=_('Column width'))
    classes = MultiSelectField(max_length=250, blank=True, choices=defaults.CONTAINER_CLASS_CHOICES)

    def __unicode__(self):
        return u"%s" % self.get_width_display()
