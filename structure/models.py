#coding: utf-8
from django.db import models

from frame.structure.fields import UUIDField

class Frame(models.Model):
    uuid = UUIDField(auto=True)
    name = models.CharField(u'name', max_length=255)
    created_at = models.DateField(u'created', auto_now_add=True)
    updated_at = models.DateField(u'updated', auto_now=True)

class Node(models.Model):
    frame = models.ForeignKey(Frame)
    x = models.DecimalField('X-cordinate', max_digits=6, decimal_places=3)
    y = models.DecimalField('Y-cordinate', max_digits=6, decimal_places=3)
    support_x = models.BooleanField(default=False)
    support_y = models.BooleanField(default=False)
    support_moment = models.BooleanField(default=False)

class Element(models.Model):
    frame = models.ForeignKey(Frame)
    start_node = models.ForeignKey(Node, related_name='start')
    end_node = models.ForeignKey(Node, related_name='end')
