<h1>Python :arrow_right: R :arrow_right: Shiny

[![coolapps!](https://github.jpl.nasa.gov/github-enterprise-assets/0000/0630/0000/1394/c9f2aa10-52af-11e4-9ef4-b4d84c43f58b.png)](http://shiny.rstudio.com/gallery/)

<h2>An Interface Example

This is an example on how to pass data from the python environment to R and on to [Shiny](http://shiny.rstudio.com/).

Shiny is a rather neat data visualization interface, which you can use to blow socks off management. Shiny exists as a library within the [R](http://www.r-project.org/) framework, which is an general-purpose scientific software environment (similar to matlab or octave).

There's not a lot of great resources on the web on how to interface to Shiny through python, but there exists a path, so I hope this is at least enough to reduce the pain that I experienced while trying to figure it out.

Half the battle alone is getting rpy2 installed. For this, there are [precompiled binaries available](http://www.lfd.uci.edu/~gohlke/pythonlibs/#rpy2) that you can download and install after you've installed [R](http://cran.rstudio.com/)--oh, and of course python for which I use [anaconda](https://store.continuum.io/cshop/anaconda/).

As an aside, let it be know that I don't _know_ python, R, and shiny, and there may be serious problems in this example, so don't use it in anything critical like your Shiny-enabled rocketship. Please let me know where I've messed up and also how you've made it better!

<h2>Technical bits

Now for the technical bits about this gist. It includes three files, the python script *py2shiny.py*, a user interface *ui.R*, and a server interface to R *server.R*. If you want to change the way the Shiny app *looks* look in ui.R. There are lots of cool examples in the [shiny gallery](http://shiny.rstudio.com/gallery/).

The _gist_ of this example is that it creates a vector of random data and passes it to shiny for visualization. It also plots in python so you can compare how broken and ugly those legs look in comparison to the shiny implementation.

If you've installed R (better get on that), lines 54-56 are passed as if they are typed in that console.

<h2>TO RUN THIS MONSTER

1> execute python py2shiny_example.py

2> spend an hour tending to error messages about the setup (_good luck with that_)

3> if you haven't abandoned ship, you should see a nice graph in your browser.

4> it has a button that allows you to cleanly exit the app, and if you had data that you selected in the shiny app, you could actually pass it back to python for further computation (see reference in py code).

