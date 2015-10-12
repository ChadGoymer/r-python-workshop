
from pyper import R, Str4R

# create an R instance object 
r = R()

# Send commands to be executed 
r('library(ART)')
r('library(ARTanalyses)')

r('synd_scr <- execute(synd_scr, Run_Request = 18196)[["data"]]')

# Retrieve objects from R
x = r.synd_scr
print(x)
print(type(x))

