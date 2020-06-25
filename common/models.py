#encoding=utf-8

from django.db import models
from common.model_fields import DecField, IdField


class BaseModelManager(models.Manager):
    def all_to_dict(self):
        queryset = self.get_queryset()
        return [obj.to_dict() for obj in queryset.all()]


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "%s(%s)" % (self.__class__.__name__, self.id)

