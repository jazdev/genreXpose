import os
import sys
import timeit
import numpy as np
from pydub import AudioSegment
from matplotlib import pylab

###################################################
#    Don't modify below this line
###################################################
config = {}
execfile("config.cfg", config)

GENRE_DIR = config["GENRE_DIR"]
TEST_DIR = config["TEST_DIR"]
GENRE_LIST = config["GENRE_LIST"]

if GENRE_DIR is None or GENRE_DIR is "":
    print "Please set GENRE_DIR in config.cfg"
    sys.exit(1)

elif TEST_DIR is None or TEST_DIR is "":
    print "Please set TEST_DIR in config.cfg" 
    sys.exit(1)    

elif GENRE_LIST is None or len(GENRE_LIST)==0:
    print "Please set GENRE_LIST in config.cfg" 
    sys.exit(1)

else:
    print "Variables defined in config.cfg :"
    print "GENRE_DIR ==> ", GENRE_DIR
    print "TEST_DIR ==> ", TEST_DIR
    print "GENRE_LIST ==> "," || ".join(x for x in GENRE_LIST)

    
DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")

CHART_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "graphs")

MODEL_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "saved_model")


for d in [DATA_DIR, CHART_DIR, MODEL_DIR]:
    if not os.path.exists(d):
        os.mkdir(d)


def convert_any_to_wav(filename):
    """
        Converts the input file to the WAV format.
    """
    pass


def convert_dataset_to_wav(file_name):
    """
        Converts all files of the GTZAN dataset
        to the WAV (uncompressed) format.
    """
    start = timeit.default_timer()
    rootdir = GENRE_DIR
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            path = subdir+'/'+file
            if path.endswith("au"):
                song = AudioSegment.from_file(path,"mp3")
                song = song[:30000]
                song.export(path[:-3]+"wav",format='wav')

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            path = subdir+'/'+file
            if not path.endswith("wav"):
                os.remove(path)

    stop = timeit.default_timer()
    print "Conversion time = ", (stop - start) 


def plot_confusion_matrix(cm, genre_list, name, title):
    """
        Plots confusion matrices.
    """
    pylab.clf()
    pylab.matshow(cm, fignum=False, cmap='Blues', vmin=0, vmax=1.0)
    ax = pylab.axes()
    ax.set_xticks(range(len(genre_list)))
    ax.set_xticklabels(genre_list)
    ax.xaxis.set_ticks_position("bottom")
    ax.set_yticks(range(len(genre_list)))
    ax.set_yticklabels(genre_list)
    pylab.title(title)
    pylab.colorbar()
    pylab.grid(False)
    pylab.xlabel('Predicted class', fontsize = 20)
    pylab.ylabel('True class', fontsize = 20)
    pylab.grid(False)
    #pylab.show()
    pylab.savefig(os.path.join(CHART_DIR, "confusion_matrix_%s.png" % name), bbox_inches="tight")


def plot_roc_curves(auc_score, name, tpr, fpr, label=None):
    """
        Plots ROC cuurves.
    """
    pylab.clf()
    pylab.figure(num=None, figsize=(5, 4))
    pylab.grid(True)
    pylab.plot([0, 1], [0, 1], 'k--')
    pylab.plot(fpr, tpr)
    pylab.fill_between(fpr, tpr, alpha=0.5)
    pylab.xlim([0.0, 1.0])
    pylab.ylim([0.0, 1.0])
    pylab.xlabel('False Positive Rate')
    pylab.ylabel('True Positive Rate')
    pylab.title('ROC curve (AUC = %0.2f) / %s' %(auc_score, label), verticalalignment="bottom")
    pylab.legend(loc="lower right")
    filename = name.replace(" ", "_")
    pylab.savefig(os.path.join(CHART_DIR, "roc_" + filename + ".png"), bbox_inches="tight")
