#python to interface to Shiny (an R library)
#why? get inspired here: http://shiny.rstudio.com/gallery/
#author - David Foor, 2014 Caltech

#This an example of how to pass data to the R environment for plotitng in a
#shiny app. This design generates some random data, plots it with matplotlib and
#then passes it to R for plotting with the shiny app.   This design doesn't
#spass data from the R environment back to the python envionment, but that is
#pretty syimple. 

#This design was created because shiny has some pretty neat vis stuff

#In addition to this script, the R environment includes the shiny applicances
#in server.R and ui.R  (included in this gist).

#Important Notes:
#1) if you get an error "error in library(shiny)" you should launch R
#   seperately and issue a install.packages("shiny") so that it can be installed
#   (install with admin privledges, I think) 
#
#2) rpy2 has to be installed. The best way is from a precompiled binary
#   available here (http://www.lfd.uci.edu/~gohlke/pythonlibs/#rpy2), if
#   you're on a windows machine.

import os
import rpy2.robjects as ro
import rpy2.rinterface as ri
import numpy as np
import matplotlib.pyplot as plt

#references for r interface usage from here:
#http://rpy.sourceforge.net/rpy2/doc-2.2/html/rinterface.html

#initialize the embedded r 
ri.initr()
r=ro.r

#generate some random data
mu, sigma = 0, 0.1 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)

#plot the random data using matplotlib (for comparison to the shiny app)
count, bins, ignored = plt.hist(s, 30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
plt.show(block=False)

#pass the series to R
ro.globalenv["dataseries"] = ro.FloatVector(s)

#call teh shiny app, and return when the user presses a button
#gist on how to exit cleanly: https://gist.github.com/trestletech/5948876
ro.r('''
        library(shiny)
        runApp()
        quit()
        ''' )

#end the embedded interface
ri.endr(0)

