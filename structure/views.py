#coding: utf-8

import cStringIO
import numpy as np
import matplotlib
matplotlib.use('Svg')
matplotlib.rcParams['axes.linewidth'] = 0.5
import matplotlib.pyplot as plt

from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return render(request, 'members.html')

def supports(request):
    return render(request, 'members.html')

def loads(request):
    return render(request, 'members.html')

def svg(request, width=None, height=None):
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