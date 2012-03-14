#coding: utf-8

from django.db import models
from frame.structure.utils import get_random_string


class Frame(models.Model):
    uuid = models.CharField(u'uuid', max_length=6)
    name = models.CharField(u'name', max_length=255)
    created_at = models.DateField(u'created', auto_now_add=True)
    updated_at = models.DateField(u'updated', auto_now=True)
    
    def nodes(self):
        return Node.objects.filter(frame=self).count()
    
    def elements(self):
        return Element.objects.filter(frame=self).count()
    
    def save(self):
        if not self.uuid:
            self.uuid = get_random_string(length=6)
        super(Frame, self).save()


class Node(models.Model):
    frame = models.ForeignKey(Frame)
    x = models.DecimalField('X-cordinate', max_digits=6, decimal_places=3)
    y = models.DecimalField('Y-cordinate', max_digits=6, decimal_places=3)
    constraint_x = models.BooleanField(default=False, blank=True)
    constraint_y = models.BooleanField(default=False, blank=True)
    constraint_rotation = models.BooleanField(default=False, blank=True)
    
    def __unicode__(self):
        return '%d, %d' % (self.x, self.y)


class Element(models.Model):
    frame = models.ForeignKey(Frame)
    start_node = models.ForeignKey(Node, related_name='start')
    end_node = models.ForeignKey(Node, related_name='end')
    length = models.DecimalField('length', max_digits=6, decimal_places=3, blank=True)
    cosa = models.DecimalField('length', max_digits=6, decimal_places=5, blank=True)
    cosb = models.DecimalField('length', max_digits=6, decimal_places=5, blank=True)

    def __unicode__(self):
        return '%s - %s' % (self.start_node, self.end_node)

    def save(self):
        import numpy as np
        from decimal import Decimal
        
        # Element length
        self.length = np.sqrt(np.square(self.end_node.y - self.start_node.y) + np.square(self.end_node.x - self.start_node.x)).quantize(Decimal('.001'))
        
        # Element cosins
        self.cosa = ((self.end_node.x - self.start_node.x) / self.length).quantize(Decimal('.00001'))
        self.cosb = ((self.end_node.y - self.start_node.y) / self.length).quantize(Decimal('.00001'))
        
        super(Element, self).save()


class Load(models.Model):
    frame = models.ForeignKey(Frame)
    element = models.ForeignKey(Element)
    x = models.DecimalField('X-cordinate', max_digits=6, decimal_places=3)
    load = models.DecimalField('X-cordinate', max_digits=6, decimal_places=2)
    
    def __unicode__(self):
        return '%s - %s' % (self.element, self.load)

class Distributed(models.Model):
    frame = models.ForeignKey(Frame)
    element = models.ForeignKey(Element)
    #x = models.DecimalField('X-cordinate', max_digits=6, decimal_places=3)
    load = models.DecimalField('X-cordinate', max_digits=6, decimal_places=2)
    
    def __unicode__(self):
        return '%s - %s' % (self.element, self.load)