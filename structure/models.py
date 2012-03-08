#coding: utf-8

from django.db import models
from frame.structure.utils import get_random_string

class Frame(models.Model):
    uuid = models.CharField(u'uuid', max_length=6)
    name = models.CharField(u'name', max_length=255)
    created_at = models.DateField(u'created', auto_now_add=True)
    updated_at = models.DateField(u'updated', auto_now=True)
    
    def save(self):
        if not self.uuid:
            self.uuid = get_random_string(length=6)
        super(Frame, self).save()

class Node(models.Model):
    frame = models.ForeignKey(Frame)
    x = models.DecimalField('X-cordinate', max_digits=6, decimal_places=3)
    y = models.DecimalField('Y-cordinate', max_digits=6, decimal_places=3)
    constraint_x = models.BooleanField(default=False)
    constraint_y = models.BooleanField(default=False)
    constraint_rotation = models.BooleanField(default=False)

class Element(models.Model):
    frame = models.ForeignKey(Frame)
    start_node = models.ForeignKey(Node, related_name='start')
    end_node = models.ForeignKey(Node, related_name='end')
