#coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.forms.models import inlineformset_factory

from frame.structure.models import Frame, Node, Element
from frame.structure.forms import FrameForm

def home(request):
    return render(request, 'home.html')

def new_frame(request):
    form = FrameForm(request.POST or None)
    if request.POST and form.is_valid():
        frame = form.save()
        return redirect('frame', uuid=frame.uuid)
        
    return render(request, 'new.html', {
        'form': form
    })

def frame(request, uuid):
    frame = get_object_or_404(Frame, uuid=uuid)
    
    return render(request, 'frame.html', {
        'frame': frame
    })

def members(request, uuid):
    frame = get_object_or_404(Frame, uuid=uuid)
    
    # Node formset
    NodeFormSet = inlineformset_factory(Frame, Node, extra=1)
    node_formset = NodeFormSet(request.POST or None, instance=frame, prefix='nodes')
    
    # Element formset
    ElementFormSet = inlineformset_factory(Frame, Element, extra=1)
    element_formset = ElementFormSet(request.POST or None, instance=frame, prefix='elements')
    
    if request.POST:
        if node_formset.is_valid():
            node_formset.save()
        if element_formset.is_valid():
            element_formset.save()
    
    return render(request, 'members.html', {
        'frame': frame,
        'node_formset': node_formset,
        'element_formset': element_formset
    })

def loads(request, uuid):
    frame = get_object_or_404(Frame, uuid=uuid)
    
    return render(request, 'loads.html')

def svg(request, uuid, format='svg'):
    frame = get_object_or_404(Frame, uuid=uuid)
    
    # Rendering format
    if format.lower() == 'agg':
        mimetype = 'image/png'
    else:
        mimetype = 'image/svg+xml'
    
    import cStringIO
    import numpy as np
    import matplotlib
    matplotlib.use(format)
    matplotlib.rcParams['axes.linewidth'] = 0.5
    import matplotlib.pyplot as plt
    
    fig = plt.figure(frameon=False)
    
    ax = fig.add_subplot(111)
    #ax.plot(10 * np.random.rand(50), '-o', ms=8, lw=1, alpha=0.7, mfc='orange')
    # Draw elements
    elements = Element.objects.filter(frame=frame)
    
    for element in elements:
        ax.plot([element.start_node.x, element.end_node.x], [element.start_node.y, element.end_node.y], 'ko-', color='black', ms=8, lw=1.5, alpha=0.7, mfc='orange')
    
    #ax.plot([0,0], [0,10], 'ko-', color='black', ms=8, lw=1.5, alpha=0.7, mfc='orange')
    #ax.plot([0,10], [10,6], 'ko-', ms=8, lw=1.5, alpha=0.7, mfc='orange')
    #ax.plot([10,10], [6,0], 'ko-', ms=8, lw=1.5, alpha=0.7, mfc='orange')
    ax.grid(True)
    ax.axis('equal')
    #ax.axis('scaled')
    #ax.axis(ax.axis())
    
    # Add a little padding the the axis
    ax.axis(np.asarray(ax.axis()) + [-1,1,-1,1])
    
    imgdata = cStringIO.StringIO()
    fig.set_size_inches(24,13.5)
    fig.savefig(imgdata, transparent=False)
    
    return HttpResponse(imgdata.getvalue(), mimetype=mimetype)
    imgdata.close()