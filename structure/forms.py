#coding: utf-8

from django.forms import ModelForm
from frame.structure.models import Node, Joint


class Frame(ModelForm):
    class Meta:
        model = Frame

class NodeForm(ModelForm):
    class Meta:
        model = Node

