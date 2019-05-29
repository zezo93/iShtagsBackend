from django.db import models
from django.utils.translation import ugettext_lazy as _
from users.models import User


# Create your models here.
class Category(models.Model):
    title = models.CharField(_('name'), max_length=225, unique=True, blank=False)
    created_at = models.DateTimeField(_('date created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('dated updated'), auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('category')
        verbose_name_plural = _('category')

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(_('name'), max_length=225, unique=True, blank=False)
    category = models.ManyToManyField(Category, related_name="Tag_Category", blank=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=None)
    created_at = models.DateTimeField(_('date created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('date updated'), auto_now=True)

    class Meta:
        db_table = 'tags'
        verbose_name = _('tag')
        verbose_name_plural = _('tags')

    def __str__(self):
        return self.name
