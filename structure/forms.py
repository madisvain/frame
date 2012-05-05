#coding: utf-8

from django.forms import ModelForm

from frame.structure.models import Frame, Node, Element


#class FrameForm(ModelForm):
#    class Meta:
#        model = Frame
#        exclude = ('uuid',)

class ElementForm(ModelForm):
    class Meta:
        model = Element
    
    def __init__(self, frame, *args, **kwargs):
        super(ElementForm, self ).__init__(*args, **kwargs)
        self.fields['start_node'].queryset = Node.objects.filter(frame=frame)
        self.fields['end_node'].queryset = Node.objects.filter(frame=frame)


class NodeForm(ModelForm):
    class Meta:
        model = Node

