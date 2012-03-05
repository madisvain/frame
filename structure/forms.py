#coding: utf-8

from django.forms import ModelForm
from frame.structure.models import Frame, Node, Element


class Frame(ModelForm):
    class Meta:
        model = Frame

class ElementForm(ModelForm):
    class Meta:
        model = Element

class NodeForm(ModelForm):
    class Meta:
        model = Node

