#coding: utf-8

from django.forms import ModelForm

from frame.structure.models import Frame, Node, Element


class FrameForm(ModelForm):
    class Meta:
        model = Frame
        exclude = ('uuid',)

class ElementForm(ModelForm):
    class Meta:
        model = Element

class NodeForm(ModelForm):
    class Meta:
        model = Node

