from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext as _


class Photo(models.Model):
    title = models.CharField(_("title"), max_length=100)
    description = models.TextField(_("description"))
    image = models.ImageField(_("photo"),upload_to='photos')
    
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('photo')
        verbose_name_plural = _('photos')

admin.site.register(Photo)

    

