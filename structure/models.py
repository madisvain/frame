#coding: utf-8
from django.db import models

from frame.structure.fields import UUIDField

class Frame(models.Model):
    uuid = UUIDField(auto=True)
    created_at = models.DateField('created', auto_now_add=True)
    updated_at = models.DateField('updated', auto_now=True)

class Node(models.Model):
    frame = models.ForeignKey(Frame)
    x = models.DecimalField('X-cordinate', max_digits=6, decimal_places=3)
    y = models.DecimalField('Y-cordinate', max_digits=6, decimal_places=3)

class Element(models.Model):
    frame = models.ForeignKey(Frame)
    start_node = models.ForeignKey(Node, related_name='start')
    end_node = models.ForeignKey(Node, related_name='end')

class Support(models.Model):
    pass
