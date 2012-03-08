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
    NodeFormSet = inlineformset_factory(Frame, Node, extra=2)
    node_formset = NodeFormSet(instance=frame)
    
    return render(request, 'members.html', {
        'frame': frame,
        'formset': node_formset,
    })

def loads(request, uuid=None):
    return render(request, 'loads.html')

def svg(request, uuid=None, width=None, height=None):
    import cStringIO
    import numpy as np
    import matplotlib
    matplotlib.use('Svg')
    matplotlib.rcParams['axes.linewidth'] = 0.5
    import matplotlib.pyplot as plt
    
    fig = plt.figure(frameon=False)
    
    ax = fig.add_subplot(111)
    #ax.plot(10 * np.random.rand(50), '-o', ms=8, lw=1, alpha=0.7, mfc='orange')
    ax.plot([0,0], [0,10], 'ko-', color='black', ms=8, lw=1.5, alpha=0.7, mfc='orange')
    ax.plot([0,10], [10,6], 'ko-', ms=8, lw=1.5, alpha=0.7, mfc='orange')
    ax.plot([10,10], [6,0], 'ko-', ms=8, lw=1.5, alpha=0.7, mfc='orange')
    ax.grid(True)
    ax.axis('equal')
    #ax.axis('scaled')
    #ax.axis(ax.axis())
    
    # Add a little padding the the axis
    ax.axis(np.asarray(ax.axis()) + [-1,1,-1,1])
    
    imgdata = cStringIO.StringIO()
    fig.set_size_inches(12,8)
    fig.savefig(imgdata, transparent=False)
    
    return HttpResponse(imgdata.getvalue(), mimetype='image/svg+xml')
    imgdata.close()