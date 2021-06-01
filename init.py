try:
    get_ipython().run_line_magic('load_ext', 'autotime')
    print('autotime loaded.')
except:
    print('autotime not loaded.')
    
try:
    get_ipython().run_line_magic('load_ext', 'watermark')
    print('autotime loaded.')
except:
    print('autotime not loaded.')
    
try:
    get_ipython().run_line_magic('load_ext', 'nb_black')
    print('black loaded.')
except:
    print('black not loaded.')
    
try:
    get_ipython().run_line_magic('load_ext', 'lab_black')
    print('black loaded.')
except:
    print('black not loaded.')

import warnings
warnings.filterwarnings('ignore')

#import cmaps
import h5py
import os, glob
import traceback
import numpy as np
import scipy as sp
import pandas as pd
import xarray as xr
import pickle as pkl
import geopandas as gpd
import matplotlib as mpl
from tqdm import tqdm
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib import ticker
import matplotlib.gridspec as gridspec


os.environ["PROJ_LIB"] = os.path.join(os.environ["CONDA_PREFIX"], "share", "proj")
from mpl_toolkits.basemap import Basemap, addcyclic, cm



from mpl_toolkits.axes_grid1 import make_axes_locatable

import string
alphabets = list(string.ascii_lowercase)

try:
    from StringIO import StringIO as io## for Python 2
except ImportError:
    from io import StringIO as io## for Python 3


#plt.subplot_tool()
mpl.rcParams.update(mpl.rcParamsDefault) 
mpl.rcParams['figure.figsize'] = (14, 5)  # A4 papersize portrait mode
mpl.rcParams['figure.titlesize'] = 25
mpl.rcParams['font.size'] = 20
#mpl.rc('lines', linewidth=2)
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.markersize'] = 3

mpl.rcParams['axes.titlesize'] = 24
mpl.rcParams['axes.labelsize'] = 24
mpl.rcParams['axes.labelpad'] = 10
#mpl.rcParams['axes.labelweight'] = 'bold'
#mpl.rc('font', weight='bold')
#mpl.rcParams['axes.titleweight'] = 'bold'
mpl.rcParams["xtick.top"] = "on"
mpl.rcParams["xtick.bottom"] = "on"
mpl.rcParams["xtick.major.size"] = 10
mpl.rcParams["ytick.major.size"] = 10
mpl.rcParams["ytick.minor.size"] = 6
mpl.rcParams["xtick.minor.size"] = 6
mpl.rcParams["xtick.labelsize"]  = 22
mpl.rcParams["ytick.labelsize"]  = 22
mpl.rcParams['xtick.direction']  = 'in'
mpl.rcParams['ytick.direction']  = 'in' 

mpl.rcParams['legend.fontsize']  = 10
mpl.rcParams['legend.labelspacing'] = 0.1

mpl.matplotlib_fname()
#mpl.rcParams.keys()

## Useful functions

def save_pickle(data, filename):
    with open(filename, "w") as df:
        pkl.dump(data, df)
        
        
def color_legend_texts(leg):
    """Color legend texts based on color of corresponding lines"""
    for line, txt in zip(leg.get_lines(), leg.get_texts()):
        txt.set_color(line.get_color())
    for item in leg.legendHandles:
        item.set_visible(False)
        
def legend_texts_sort(ax):
    handles, labels = ax.get_legend_handles_labels()
    # sort both labels and handles by labels
    labels, handles = zip(*sorted(zip(labels, handles), key=lambda t: len(str(t[0]))))
    #ax.legend(handles, labels)
    #leg=ax.legend(handles, labels, bbox_to_anchor=(0.7, 1.15),frameon=False,markerscale=0)
    return handles,labels
    
def sort_color_legend(ax1,ax2,kw):
    handles,labels=legend_texts_sort(ax1)
    leg=ax2.legend(handles, labels,frameon=False,markerscale=0,**kw)
    color_legend_texts(leg)
    return ax2
    
def color_legend(ax = None, props = {'weight':'bold', 'size':17}, loc=4, ncol =1):
    handles, labels  = ax.get_legend_handles_labels()
    leg = ax.legend(handles, labels, loc=loc, frameon=False, prop=props, ncol=ncol)
    color_legend_texts(leg)  
    
def logformat(y):
    # Find the number of decimal places required
    decimalplaces = int(np.maximum(-np.log10(y),0))     # =0 for numbers >=1
    # Insert that number into a format string
    formatstring = '{{:.{:1d}f}}'.format(decimalplaces)
    # Return the formatted tick label
    return formatstring.format(y)
    
def gen_fig(nrows,ncols,width=None,aspect=None,pad=None,kw=None,grid=None):
    if not width:
        width=10
    if not aspect:
        aspect=0.5
    if not pad:
        pad=dict(wspace=0, hspace=0,left=0.06, bottom=0.09, right=0.9, top=0.99)
    if not kw:
        kw=dict(sharey='row', sharex='col')
    fig, axes = plt.subplots(nrows,ncols,figsize=(width,width*aspect),gridspec_kw=grid, **kw)
    fig.subplots_adjust(**pad)
    return fig,axes 
    
def move(infile,outfile):
    command='mv'+' '+infile+' '+outfile
    subprocess.call(command,shell=True)

def copy(infile,outfile):
    command='cp'+' '+infile+' '+outfile
    subprocess.call(command,shell=True)
    
def make_dir(folder): 
    try:
        os.makedirs(folder)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def figsave(fig,filename,basefolder):  
    fig.savefig(basefolder+'eps/'+filename+'.eps')
    fig.savefig(basefolder+'pdf/'+filename+'.pdf')
    fig.savefig(basefolder+'png/'+filename+'.png')
    
def linestyle():
	linestyles = OrderedDict(
    		[('solid',               (0, ())),
	     	('loosely dotted',      (0, (1, 10))),
     		('dotted',              (0, (1, 5))),
     		('densely dotted',      (0, (1, 1))),

     		('loosely dashed',      (0, (5, 10))),
     		('dashed',              (0, (5, 5))),
     		('densely dashed',      (0, (5, 1))),

     		('loosely dashdotted',  (0, (3, 10, 1, 10))),
     		('dashdotted',          (0, (3, 5, 1, 5))),
     		('densely dashdotted',  (0, (3, 1, 1, 1))),

     		('loosely dashdotdotted', (0, (3, 10, 1, 10, 1, 10))),
     		('dashdotdotted',         (0, (3, 5, 1, 5, 1, 5))),
     		('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1)))])
