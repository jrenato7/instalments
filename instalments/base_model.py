#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

__author__ = '@elinaldosoft'


class TimeStamp(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado em')

    class Meta:
        abstract = True


class TimeStampUser(TimeStamp):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, 
        verbose_name=_('Criado por'), editable=False, null=True, 
        blank=True)
    update_by = models.ForeignKey(User, on_delete=models.SET_NULL, 
        verbose_name=_('Editado por'), blank=True, null=True, 
        editable=False, related_name='+')

    class Meta:
        abstract = True
