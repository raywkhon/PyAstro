#!/usr/bin/env python
#!/ProgramData/anaconda3 python
# -*- coding: utf-8 -*- Rstudio system default
# The above lines are only needed if run the program from the command line as an executable file
"""
Created on Fri Mar 24, 2023
@author: rh
"""
# Import the os module
import os
# Get and print the current working directory
cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))
# Change the current working directory
os.chdir("python")

"""
1. Numpy is a collection of mathematical and numerical functions, from 
sin and cos to integration and linear algebra. We will use this instead 
of the python math module, which also has basic mathematical functions.
"""
import numpy as np
"""
2. Scipy is a collection of functions for scientific calculations. 
We will use the scipy functionality for curve fitting, for instance.
"""

"""
3. Astropy has functions for astronomers, including those that let us deal 
with files in the fits format and those that help us with calculating 
astronomical quantities.
"""
from astropy import constants as const
from astropy import units as u

"""
4. Matplotlib is go-to library for plotting diagrams of various kinds.
"""
import matplotlib.pyplot as plt

"""
5. Random module in Python provides functions of picking a random sample from a larger subset, 
i.e. a random floating point number x with 0  < x < 1.
"""
import random
random.random()


# Returns a random integer i with p  < i  < q.
random.randint(2,44)

# Create a random subset of k elements from a list thisList
thisList = range(100)
random.sample(thisList,5)

# Draw random values from specific probability distributions, e.g. Gaussian (normal) distribution with mean mu and standard deviation stdDev.
mu = 5
stdDev = 2
random.gauss(mu,stdDev)

"""
Concatenate strings, just use the plus sign:
"""
Strg = "def" + "def"

print(Strg)

"""
Format function builds strings out of numbers and other variables, which
works as follows: You create a string that includes a placeholder built 
from curly brackets. The string is followed by .format(), where the 
parentheses enclose those variables that are to be substituted for the placeholders.
For example, to insert an integer value into a file name:
"""
thisInt = 10
print("egon{}.jpg".format(thisInt))
print("egon{:03d}.jpg".format(thisInt))
thisFloat=1.51515151515151515
print("This is a floating point number: {:f}(see?)".format(thisFloat))
# For scientific formatting with an exponential, use {:e},
thisFloat=151515.1515
print("This is a floating point number: {:e}(see?)".format(thisFloat))
# Placeholder only switches to exponentials for numbers smaller than 10^闁???4
thisFloat=0.0001515
print("This is a floating point number: {:g}(see?)".format(thisFloat))
thisFloat=0.00001515
print("This is a floating point number: {:g}(see?)".format(thisFloat))

"""
Python 3.6 onwards has a simpler way of formatting numbers to yield strings, so-called -strings.
The string now has an  in front of the quotation marks, telling Python that this is an f-string in such
a way that expressions in curly numbers are interpreted as formatting instructions.
"""
thisFloat=0.0001515
print(f"This is a floating point number:{thisFloat:g} (see?)")

"""
Strings can be addressed as lists of characters
"""
thisString="ABCDEFGHIJKLMNOP"
print(thisString[3:6])

"""
As an astronomical example, we will automatically create a URL to download a spectrum from SDSS data
release 8. Each SDSS observation of the type we are interested in took up to a few hundreds of spectra 
simultaneously. To this end, an aluminium plate was placed in the telescope focal plane, with a pattern of holes
made to measure for the observing field in question. In each hole, a light-conducting fiber that captures the light
from a specific object, conducting it to a spectrograph. Since some plates were used more than once, we need also
specify the date of the observation, using the Modified Julian Date (MJD) common in astronomy. Specifying
plate number, fibre number and date picks out the spectrum of a specific object. As the SDSS software evolves,
spectra are sometimes re-analysed, so we need to specify the number of the reduction run  when the raw data
was sent through a specific software pipeline to yield a reduced spectrum, suitable for astrophysics. To retrieve a
specific spectrum from the SDSS server, we need combine those numbers into a suitable custom URL for download.

"""
run2d=26
plate = 1324
mjd = 53088
fiberID = 456
baseURL = "http://data.sdss3.org/sas/dr8/sdss/"
dirURL=f"spectro/redux/{run2d:d}/spectra/{plate:d}/"
fileURL="spec-{plate:d}-{mjd:d}-{fiberID:04d}"
url=baseURL+dirURL+fileURL+".fits"
print(url)

"""
A simple way to actually do the download, at least on Mac or Linux computers with curl installed, would be a
system call. This downloads the file to the working directory, where it will be saved as spectrum.fits.
"""
from subprocess import call
saveFileName= "spectrum.fits"
call(["curl", "-o", saveFileName, url])

"""
Conditions - Note that the actions that the print statement, are indented
"""

a=0.5
if a>1:
  print("a is bigger than one!")
elif a==1:
  print("a is equal to one!")
else:
  print("a is smaller than one!")
  
"""
User-defined functions, e.g. f(x) = 2x^2 - x,
"""
def polyFunc(x):
  return 2*x**2-x
a=2
b=4
polyFunc(a)
polyFunc(b)

def zeroSqrt(x):
  if x<0:
    return 0
  else:
    return np.sqrt(x)
zeroSqrt(-1)
zeroSqrt(4)

def sumOfThreeArgs(x,y,z):
  return x+y+z
sumOfThreeArgs(1,20,30)

"""
An alternative way of defining functions, which uses the keyword lambda, which echo
mathematics formal system of lambda calculus 
"""
polFunc = lambda x: 2*x**2-x
print(polFunc(2))

"""
Timing your code - The function time() will return the number of seconds that have passed since
an operating-system-specific zero point (in UNIX, January 1, 1970).
"""
import time
start_time=time.time()
for ii in range(1000000):
  pass
end_time=time.time()
print("This took {} seconds!".format(end_time-start_time))

"""
LONG DATA SETS: A list of galaxies: brightness.
"""

galaxy_u = [23.4, 23.2, 26.8, 24.6, 24.5, 24.3, 23.1, 27.0, 24.0]
galaxy_u
galaxy_u[2]
max(galaxy_u)
min(galaxy_u)
len(galaxy_u)
galaxy_u[2:5]
galaxy_u[:5]
galaxy_u[5:]
galaxy_u[5:-1]
galaxy_u.append(25.1)
# remove the last element from a list.
galaxy_u.pop()
galaxy_u

"""
Apply function or operation to each list element separately. For instance, in the case of galaxies 
from the SDSS catalogue (Sloan Digital Sky Survey), the u-filter magnitude mu is related
to the flux fu (energy received from the galaxy per unit frequency interval per unit time per unit 
receiving area) as fu = 3631 x 10^(mu/(-2.5)) Jy.
"""
galaxy_f=[]
for u in galaxy_u:
  f=3631*np.power(10,u/(-2.5))
  galaxy_f.append(f)
galaxy_u
galaxy_f

"""
Another way of solving our problem, using the map function. For this, we define the operation in as 
a function. map will apply this function to each separate element of the list, Notice the List operator 
which is required in Python 3.X
"""
import numpy as np
galaxy_f=[]
def flux(u):
  return 3631*np.power(10,u/(-2.5))
#galaxy_f = list(map(flux, galaxy_u))
galaxy_f = map(flux, galaxy_u)
galaxy_u
galaxy_f

"""
Another way of performing this task, by creating a list from another list. The construct in question is called 
a list comprehension. If you only want results satisfying a certain condition, you can add an if block at the end.

"""
galaxy_f = [ 3631*np.power(10,u/(-2.5)) for u in galaxy_u if u < 25 ]
galaxy_u
galaxy_f

"""
Operations involving more than one list, e.g. a list st_appV of apparent magnitudes in the V band of several stars, 
and a list st_distPc containing each star distance from us in parsec. We want to calculate each star 
absolute magnitude, using the formula relating the apparent magnitude m, absolute magnitude M, and distance d as
M = m - 5 xlog10 (d'/10 pc). Function range, with a single integer argument n, produces a list with n values, 
containing integer values from 0 to n  1,
"""
st_appV = [-1.46, 5.2, 3.49, 0.76]
st_distPc = [2.64, 3.5, 3.65, 5.12]
import numpy as np
st_absV=[]
for i in range(len(st_appV)):
  thisM = st_appV[i] - 5*np.log10(st_distPc[i]/10.0)
  st_absV.append(thisM)
st_absV

"""
Using list comprehensions, we can again make this operation much shorter and simpler. The zip function 
combines the 2 single lists where each entry has two values.The objects that have round instead of 
square brackets, are called tuples.Tuples, once defined, need to stay the same length.
"""
import numpy as np
st_absV = [ m - 5*np.log10(d/10.0) for m,d in
  zip(st_appV,st_distPc) ]
st_absV


"""
Creating lists simultaneously
"""
nm = ["SDSS-II SN 21387","SDSS-II SN13651","SDSS-II SN 03706","SDSS-II SN 10963","SDSS-II SN 03475"]
dpc=[4200.,1700.,3720.,577.,1040.]
zv=[0.48,0.25,0.44,0.09,0.3]

nmN=[]
dpcN=[]
zvN=[]
for i in range(len(nm)):
  if zv[i] < 0.26:
    nmN.append(nm[i])
    dpcN.append(dpc[i])
    zvN.append(zv[i])
    
nmN
dpcN
zvN
"""
A more elegant solution using a list comprehension:
"""
nmN,dpcN,zvN = zip(*[ (n,d,z) for n,d,z in
  zip(nm,dpc,zv) if z> 0.26 ])
nmN
dpcN
zvN


"""
Numpy arrays - similar to a list but has nice extra properties. e.g., if we want to create
a new array out of several old ones, we can write the formula in exactly the same way we would
write it for a simple, non-list variable. To define a numpy array from scratch, we define a list 
and transform that list into an array as follows:
"""
import numpy as np
a = np.array([1.0,2.0,3.0,4.0])
b=2*a

a,b

a[1:]
a[:-1]

"""
Variable types, lists, arrays and speed - If we assign an integer to the variable a,
then that variable will be an integer variable. If we assign a string to a, then from
that moment on, a will be a string variable
"""
a = I am a string
type(a)
a = 1
type(a)
"""
A simple one-dimensional numpy array can only contain variables of the same type. You can
also force an array to have a specific type, by using the dtype keyword.
"""
floatArray = np.array([1, 2, 3, 4], dtype="float32")
type(floatArray)
floatArray

"""
numpy array operations are typically much faster than list operations. The following program 
takes a list or array consisting of the first million integers and doubles each element:
The list operation takes 0.15 seconds, the array operation a mere 0.0012 seconds a factor hundred less!
"""
import time
import numpy as np
numberlist=[ii for ii in range(1000000)]
numberarrIt = np.array(numberlist)
numberarr = np.array(numberlist)

start_time=time.time()
for ii in range(len(numberlist)):
  numberlist[ii] = 2*numberlist[ii]
end_time=time.time()
print("List took {:.4g} seconds!".format(end_time-start_time))
start_time=time.time()
numberarr = 2*numberarr
end_time=time.time()
print("Array took {:.4g} seconds!".format(end_time-start_time))

"""
Strings and base n numbers as lists - Variables of different types can be transformed into
each other. e.g., object IDs for the SDSS survey have long numbers to begin with; every object that 
has been identified in a data release of the SDSS has a unique object ID, and every object for which
a spectrum has been taken has a spectral object ID, specObjID. Consider the object with the 
spectral object id 1490816872793270272, which is an elliptical galaxy. To extract the information 
contained in that long number, we put the specObjID into a suitable variable, and transform that to 
a binary number, using the function bin:
"""

specObjId = 1490816872793270272
binVersion=bin(specObjId)
bin(specObjId)
len(binVersion)

"""
The 0b in the beginning indicates that what follows is a binary number.The conversion leaves out any
leading zeros. To restore them, we can use the zfill function. If we use the int function, specifying 
base 2 as an extra argument, we can convert this into an ordinary integer: i.e. the object plate number,

"""
binVersion=bin(specObjId)[2:].zfill(64)
len(binVersion)
binVersion[0:16]
int(binVersion[0:16],2)

"""
PLOTTING WITH PYTHON AND MATPLOTLIB - Plotting a function
np.linspace creates a set of 200 points, evenly distributed between (and including) the points 0 and 2.
plt.clf() clears all figures you might have plotted beforehand. plt.subplots_adjust stretches the display window 
while plt.xlabel and plt.ylabel add axis names. plt.xlim and plt.ylim set the lowest and the highest value.
"r" specified the colour red;  set the line width, and set the linestyle to shed.axvline and axhline 
add straight lines to show where x or y values are located w/ two different colors. Annotations - The xy tuple 
specifies where the arrow points, the xytext is where the annotation text should be displayed. The arrowprops option 
specifies the type of arrow to be used.
"""
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,2*np.pi,200)
y = np.sin(x)

plt.clf()
#plt.figure(figsize=(2,1))
plt.subplots_adjust(bottom=.2, left=.2)
plt.xlabel("Time in seconds")
plt.ylabel("Pendulum angle [arbitrary units]")
plt.axhline(0.0,color="g")
plt.axvline(0.5*np.pi,color= "m")
plt.annotate("intersection!", xy=(np.pi, 0), xytext=(4, 0.3),fontsize=10,
            arrowprops=dict(facecolor='black', headwidth=4, width=0.5, shrink=0.1))
plt.xlim(0,2*np.pi)
plt.ylim(-1.1,1.1)
plt.plot(x,y,"r",lw=1.0,linestyle="dashed")
plt.show()

"""
Scatter plots - e.g. 5 galaxies values : distance to Earth in Mpc and their redshift values. 
We begin by defining lists containing the galaxy names, distances and redshifts.
Now create a Hubble diagram, by plotting redshift values on the x axis and distance values on the
y axis. The options s changes the size of markers (size correspond to area, not diameter), 
color changes color, and marker changes the shape of the marker.
The plot function also plots a scatter diagram using a data marker shape,

"""
nm = ["SDSS-II SN 21387","SDSS-II SN 13651","SDSS-II SN 03706","SDSS-II SN 10963","SDSS-II SN 03475"]
dpc=[4200.,1700.,3720.,577.,1040.]
zv=[0.48,0.25,0.44,0.09,0.3]
sizes = [40,15,25,80,38]

plt.clf()
#plt.scatter(zv,dpc,marker="^",s=40,color="r")
#plt.scatter(zv,dpc,s=sizes)
plt.xlabel("Redshift z")
plt.ylabel("Distance in Mpc")
plt.plot(zv,dpc,"*")
plt.show()

"""
Fitting data - polyfit function fits zv as x values and dpc as y values with a polynomial of degree 1, i.e. 
a linear function y = a  x + b. The Hubble-Lema re relation is: for distant galaxies, redshifts z and 
distances d are related by z = Ho/c  d, with Ho as the Hubble constant and c the vacuum speed of light. 
Here x = d(dpc) e.g. 4200 and y = Z(zc), e.g. 0.48 and Ho = (3x10^5 km/s)/9560 = 31.4 km/s/Mpc, which is 
rather different from the best current values 70 km/s/Mpc. Setting cov=True will return the associated 
covariance matrix.Square roots of the diagonal of that matrix gives us estimates for the errors of the parameters.
For the parameter a, we obtain a = 9560  2321, so Hubble constant estimate comes with an error H0 = (31.4 +/- 7.6)km/s/Mpc
"""
import matplotlib.pyplot as plt
import numpy as np

nm = ["SDSS-II SN 21387","SDSS-II SN 13651","SDSS-II SN 03706","SDSS-II SN 10963","SDSS-II SN 03475"]
dpc=[4200.,1700.,3720.,577.,1040.]
zv=[0.48,0.25,0.44,0.09,0.3]
sizes = [40,15,25,80,38]

# Scatter plots
plt.clf()
plt.xlabel("Redshift z")
plt.ylabel("Distance in Mpc")
plt.plot(zv,dpc,"*")

# Fitting data
popt,pcov = np.polyfit(zv,dpc,1,cov=True)
perr = np.sqrt(np.diag(pcov))
popt
pcov
perr
x = np.linspace(0,0.5,200)
y = x*popt[0] + popt[1]
plt.plot(x,y,"r",lw=1.0)

plt.show()

"""
As Hubble-Lemaitre relation is actually y = ax, we program this new version of our fitting function by curve_fit 
of the SciPy library: an additional step to define the function. To fit data to a general function f(x), with 
free parameters a,b,c, whose values will then need to be fixed by the fitting procedure, and x must be the 
first argument, followed by free parameters. curve_fit has three input slots: the 1st is for our pre-defined 
fit function, the 2nd for x data and the 3rd for the array of y data. The result is a = 7597.89 +/- 932.90, then 
Ho = (3x10^5 km/s)/a = (39.5 +/- 4.8) km/s/Mpc, so the discrepancy is due to something else.
"""
dpc=[4200.,1700.,3720.,577.,1040.]
zv=[0.48,0.25,0.44,0.09,0.3]
from scipy.optimize import curve_fit
def fitFunc(x,a):
  return x*a
popt, pcov = curve_fit(fitFunc, zv, dpc)
perr = np.sqrt(np.diag(pcov))
popt
pcov
perr

"""
Histograms - central limit theorem. ns=30 means the histogram to have 30 bins. The histogram has no clear 
structure; all values are of similar frequency, around the expectation value 10000/30 +/- 330, but with random 
fluctuations above and below that value.
"""
import numpy as np
randArray = np.random.rand(10000)
plt.clf()
plt.hist(randArray,bins=30)
plt.show()

"""
If we add two random arrays, so that each number in the resulting array is now the sum of two random
numbers. Now, the histogram has a maximum in the middle, near 1, and smaller and larger values are less common. 
Because the sums of the integers between 1 and 5, there is only one way to obtain the 10, namely 5+5. But there 
are several ways to obtain 5: 4+1, 3+2, 2+3, 1+4. An outcome near the middle of the set is more likely.

As we sums over more and more random numbers, the histogram looks more and more to a normal (Gaussian) distribution. 
The central limit theorem says for situation like this, where the sum of many random variables, all drawn from the 
same probability distribution : as the number of terms in the sum grows, the resulting distribution comes ever closer
to a normal distribution. T
"""
import numpy as np
randArray = np.random.rand(10000)+np.random.rand(10000)
plt.clf()
plt.hist(randArray,bins=30)
plt.show()

"""
Saving figures - file type is determined by the file extension, e.g pdf, png or jpg. Resolution for pixel-based 
formats can be set using the option dpi=300 for 300 dots per inch. The bbox_inches=tight makes sure the figure 
fits itself nicely into the allotted space.
"""
plt.savefig("python/histogram.pdf",bbox_inches="tight")

"""
Glue is a multi-disciplinary tool at [https://glueviz.org]- interactive functionality glueing data sets for the different subsets, 
sorting them into different arrays, and plotting the results in the histograms and diagrams we need. That would be a matter
of coding the distinctions we make, and the visualisations to select subsets from data, and then have that selection represented 
simultaneously in the relevant histograms and diagrams,
"""

"""
Open a FITS table - The hdulist variable contains all the HDUs (header/data units) of the FITS file. They consist of multiple data,
e.g. image or a table or another type of array, and the header contains meta-information about the data. function, dex, and you 
will get a brief table of contents: The primary HDU is not commonly used for scientific data. The second HDU, index 1, is a table 
stored in a binary format (nTableHDU), with 243500 rows and 233 columns. K are 64-bit-integers, 11A is a string with 11 characters, 
I a 16 bit integer, E a single precision floating point. hdulist[1] calls the 2nd columns attribute of the table. 
Once we have opened the HDULIST and assigned it to a variable hdulist, we can get the data via hdulist[1].data
tdata.field(specobjid) access a specific column from this table with column name

"""
from astropy.io import fits
hdulist = fits.open("zoo2MainSpecz.fits")
hdulist.info()
hdulist[1].columns
tdata = hdulist[1].data
tdata.field("specobjid")
# index conventions to get specific elements
tdata.field("specobjid")[2]
"""
Open an ASCII table. The csv file has been reduced to 9 entries. List index data["specobjid"][4] gives the 5th entry in that column,
"""
from astropy.io import ascii
data=ascii.read("zoo2MainSpecz2.csv")
data.info
data
data["specobjid"]
data["specobjid"][4]

"""
Access astronomical data in GAIA Virtual Observatory (VO) with pyvo.
The multiline string inside double quotation marks " contains the ADQL query. The properties 
galactic longitude l and galactic latitude b refer to the coordinate system in which 
the Milky Way band across the sky at latitude b=0. RANDOM_INDEX retrieves a random subsample 
of Gaia point sources. '+180.0) % 360' is used to shift the galactic longitude by 180 degrees, 
so the galactic center is at the centre of image, not around l=0. cmap=plt.cm.jet Sets the 
colormap to 'jet' (other colormaps incude 'viridis', 'plasma', 'inferno', 'magma', 'cividis'). 
The Milky Way, the Large Magellanic Cloud and the Small Magellanic Cloud are clearly visible.
https://www.arxiv-vanity.com/papers/1905.13189/#S4
"""
# Import the os module
import os
# Get and print the current working directory
cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))
# Change the current working directory to C:\Users\Raymond\Documents\python
os.chdir("python")

import requests
import numpy as np
import pyvo as vo
import matplotlib.pyplot as plt
serviceURL="https://gea.esac.esa.int/tap-server/tap"
service = vo.dal.TAPService(serviceURL)
resultset = service.search(
"""
SELECT TOP 1000000
l,b
FROM gaiadr2.gaia_source
ORDER BY RANDOM_INDEX
""")
plt.clf()
plt.hist2d((resultset["l"]+180.0) % 360,resultset["b"], bins=(200, 200), cmap=plt.cm.jet)
# Plot of Gaia stars, retrieved with PyVO
plt.show()
plt.savefig("gaia-plot.pdf",bbox_inches="tight")

"""
Select ra and dec of Andromeda galaxy,from the table gaiadr2.gaia_source in Gaia DR2 (https://gea.esac.esa.int/tap-server/tap)
CIRCLE specifies a circular region of radius  3.2 degrees in the sky, with center point at right ascension 10.684708 degrees
and declination 41.268750 degrees, i.e. the center of the Andromeda galaxy. POINT selects the ra and dec in ICRS 
(International Celestial Reference System). CONTAINS returns 1 if the point is contained in the region, and 0 otherwise. 
  """
import pyvo as vo
import matplotlib.pyplot as plt
serviceURL="https://gea.esac.esa.int/tap-server/tap"
service = vo.dal.TAPService(serviceURL)
resultset = service.search(
"""
SELECT ra, dec
FROM gaiadr2.gaia_source
WHERE 1=CONTAINS(POINT('ICRS',ra,dec),
                    CIRCLE('ICRS',10.684708,41.268750, 3.2))
""")
plt.clf()
plt.hist2d((resultset["ra"]+180.0) % 360,resultset["dec"], bins=(200, 200), cmap=plt.cm.jet)
# Plot of Gaia stars, retrieved with PyVO
plt.show()

"""
Find the brightest stars of the whole sky in the Gaia DR2 catalog. phot_g_mean_mag sets the magnitude 
(i.e. the brightness expressed in the usual logarithmic scale of astronomy) of the object in the G filter band. 
SELECT the TOP million of rows in ascending order(ASC), while descending order would be DESC.
"""
import pyvo as vo
import matplotlib.pyplot as plt
serviceURL="https://gea.esac.esa.int/tap-server/tap"
service = vo.dal.TAPService(serviceURL)
resultset = service.search(
"""
SELECT TOP 1000000 ra, dec, phot_g_mean_mag
FROM gaiadr2.gaia_source
ORDER BY phot_g_mean_mag ASC
""")
plt.clf()
plt.hist2d(resultset["ra"] % 360,resultset["dec"], bins=(200, 200), cmap=plt.cm.jet)
# Plot of Gaia stars, retrieved with PyVO
plt.show()

"""
Select the top N rows for random_index, then get a random sub-sample from the table. column random_index 
contains a random permutation of the integers from 1 to N. Note that this is not a generic ADQL feature, 
but instead relies on the Gaia team having supplied an extra column random_index for the purpose. 
The result shown as a plane plot with some extra structure, namely the Large Magellanic Cloud and the 
Small Magellanic cloud, our nearest neighbouring galaxies, in the bottom left corner
"""
import pyvo as vo
import matplotlib.pyplot as plt
serviceURL="https://gea.esac.esa.int/tap-server/tap"
service = vo.dal.TAPService(serviceURL)
resultset = service.search(
"""
SELECT TOP 1000000 ra, dec
FROM gaiadr2.gaia_source
ORDER BY random_index
""")
plt.clf()
plt.hist2d(resultset["ra"] % 360,resultset["dec"], bins=(200, 200), cmap=plt.cm.jet)
# Plot of Gaia stars, retrieved with PyVO
plt.show()

"""
JOIN combines data from 2 tables, gaiadr2.vari_cepheid containing all Cepheids in DR2 with fp (fundamental pulsation period)
and gaiadr2.gaia_source with ra and dec. source_id is the unique identifier.

"""
import pyvo as vo
import matplotlib.pyplot as plt
serviceURL="https://gea.esac.esa.int/tap-server/tap"
service = vo.dal.TAPService(serviceURL)
resultset = service.search(
"""
SELECT s.ra, s.dec, c.pf
FROM gaiadr2.gaia_source AS s
JOIN gaiadr2.vari_cepheid AS c
USING (source_id)
""")
plt.clf()
plt.hist2d(resultset["ra"] % 360,resultset["dec"], bins=(200, 200), cmap=plt.cm.jet)
# Plot of Gaia stars, retrieved with PyVO
plt.show()

"""
Select subsets (open cluster NGC 188) directly from a 2D plot ra and dec, but also the proper motion (i.e. the motion on the celestial sphere)
in the ra and dec directions, pmra and pmdec, respectively. bp_g is the blue minus the green brightness of the object, 
which serves as a measure of colour, and phot_g_mean_mag is the magnitude (brightness) in Gaia broad G band, which 
can stand in for the object overall brightness.  X as  and Y as dec will plot the proper motions of the stars
"""
import pyvo as vo
import matplotlib.pyplot as plt
serviceURL="https://gea.esac.esa.int/tap-server/tap"
service = vo.dal.TAPService(serviceURL)
resultset = service.search(
"""
SELECT ra, dec, pmra, pmdec, bp_g, phot_g_mean_mag
FROM gaiadr2.gaia_source
WHERE 1=CONTAINS(POINT('ICRS',ra,dec), CIRCLE('ICRS', 12.1083,85.2550, 0.4))
""")
plt.clf()
plt.hist2d(resultset["ra"],resultset["dec"] ,bins=(200, 200), cmap=plt.cm.jet)
# plt.hist2d(np.isfinite(resultset["bp_g"]),np.isfinite(resultset["phot_g_mean_mag"]),bins=(200, 200), cmap=plt.cm.jet)
# Plot of Gaia stars, retrieved with PyVO
plt.show()

"""
Histograms for the subset (stars within the open cluster NGC 188)
"""
import numpy as np
plt.clf()
plt.hist(resultset["phot_g_mean_mag"],bins=30)
plt.show()

"""
Galaxy spectrum id 1237659161195249685 from SDSS DR8 data release 8 (telescopes located at Apache Point Observatory (APO) in New Mexico), 
at http://skyserver.sdss.org/dr8/en/tools/explore/obj.asp. Download  FITS file spec-1330-52822-0304.fits. COADD is the spectrum we want. 
SPECOBJ contains general information about the object, while SPZLINE describes the spectral lines that have been identified in the spectrum. 
B1 and R1 are different exposures of the (overlapping) blue and red portions of the spectrum, recorded on separate chips; they have been added up 
and combined to give COADD.

"""
from astropy.io import fits
hdulist = fits.open("spec-1330-52822-0304.fits")
hdulist.info()
hdulist[1].columns
tdata = hdulist[1].data
tdata
tdata.field("flux")
# index conventions to get specific elements
tdata.field("flux")[2]

import matplotlib.pyplot as plt
import numpy as np

# Scatter plots
plt.clf()
plt.xlabel("loglam")
plt.ylabel("flux")
plt.plot(tdata.field("loglam"),tdata.field("flux"),"r",lw=1.0)
plt.show()

"""

"""



"""
- Table Access Protocol (TAP)  accessing source catalogs using ADQL queries.
- Simple Image Access (SIA)  finding images in an archive.
- Simple Spectral Access (SSA)  finding spectra in an archive.
- Simple Cone Search (SCS)  for positional searching a source catalog or an observation log.
- Simple Line Access (SLAP)  finding data about spectral lines, including their rest frequencies.
require:numpy, astropy, requests
https://pyvo.readthedocs.io/en/latest/

Table Access Protocol (TAP)  access source catalogs vo.dal.TAPService, at GAVO (German Astrophysical Virtual Observatory).
Run database query: service.search. ivoa.obscore table contains generic metadata for datasets at GAVO.
The resultset object works like a numpy record array, which can be processed by columns or rows.
"""
service = vo.dal.TAPService("http://disc.g-vo.org/tap")
resultset = service.search("SELECT TOP 3 * FROM ivoa.obscore")
resultset
row = resultset[2]
row
column = resultset["dataproduct_type"]
column
columnlast = resultset["source_table"]
columnlast
for row in resultset:
  calib_level = row["calib_level"]
calib_level

"""
Registry search - interrogate the IVOA Registry, e.g.  iterate over all TAP services supporting the obscore data model
"""
for service in vo.regsearch(datamodel="obscore"):
  print(service['ivoid']) 

"""
Using pyvo
- Data Access (pyvo.dal)
- Registry (pyvo.registry)
- IO (pyvo.io)
- Auth (pyvo.auth)
- Prototype Implementations (pyvo.utils.prototype)
"""
import pyvo as vo
service = vo.dal.SIAService("http://dc.zah.uni-heidelberg.de/lswscans/res/positions/siap/siap.xml")
print(service.description)
resultset = service.search(pos=pos, size=size)
resultset
"""
Astrometrical parameters - PyVO accept SkyCoord or Quantity objects as well as any other sequence containing right ascension and 
declination in degrees, which are converted to the standard coordinate frame (in the VO, that usually is ICRS) in the standard units
(always degrees in the VO) before they are submitted to the service.
"""
import pyvo as vo
from astropy.coordinates import SkyCoord
from astropy.units import Quantity
pos = SkyCoord.from_name('NGC 4993')
pos
size = Quantity(0.5, unit="deg")
size
from astropy.time import Time
time = Time(('2015-01-01T00:00:00', '2018-01-01T00:00:00'),
            format='isot', scale='utc')
time           
"""
Table Access Protocol (TAP) - defines a service protocol for accessing general table data, including astronomical catalogs and 
general database tables. Access is provided for both database and table metadata and for actual table data. 
This protocol supports the query language Astronomical Data Query Language (ADQL) 
"""
tap_service = vo.dal.TAPService("http://dc.g-vo.org/tap")
tap_service
tap_results = tap_service.search("SELECT TOP 10 * FROM ivoa.obscore")
tap_results
print(tap_service.maxrec)
tap_results = tap_service.search("SELECT * FROM ivoa.obscore", maxrec=100000)
print(tap_service.hardlimit)

"""
Simple Image Access (SIA)  for the discovery, description, access, and retrieval of multi-dimensional 
image datasets, including 2-D images as well as datacubes of three or more dimensions.
"""
pos = SkyCoord.from_name('Eta Carina')
size = Quantity(0.5, unit="deg")
sia_service = vo.dal.SIAService("http://dc.zah.uni-heidelberg.de/hppunion/q/im/siap.xml")
sia_results = sia_service.search(pos=pos, size=size)

"""
ASTRONOMICAL IMAGE MANIPULATION WITH PYTHON - FITS 65536, or 16 bits. Open Hubble Space Telescope images with HDU contains 
meta-information. hdulist[1].header calls the science image SCI with index 1 (2nd HDU), and ["NAXIS1"] give the number of pixels.
[PTIME gives the exposure time in seconds. data gives the image data.imshow function display the image, set_aspect('equal') tells 
matplotlib that both x and y axes should have the same scale. cmap option tells imshow to use grayscale. The result is at first rather dark.
"""
from astropy.io import fits
hdulist=fits.open("hst_05773_05_wfpc2_f502n_wf_drz.fits")
hdulist.info()
hdulist[0].header
hdulist[0].header["EXPTIME"]
hdulist[1].header
hdulist[1].header["NAXIS1"]
hdulist[1].header["BUNIT"]
imdata =  hdulist[1].data
imdata
plt.clf()
plt.axes().set_aspect("equal")
plt.imshow(imdata,cmap="gray")
plt.show()

"""
We now map the high contrast of the FITS image to our more modestly contrasted version, with use the clim option to map a more 
restricted range of values to our image. Let look at the 1st and 99th percentile values of the image data (i.e. the brightness
value below which the darkest 1% of the pixels fall, and the brightness value above which 1% of the pixels fall). 
"""
np.percentile(imdata,1)
np.percentile(imdata,99)
# clim option map a more restricted range of values to our image
plt.clf()
plt.axes().set_aspect("equal")
plt.imshow(imdata,cmap="gray",clim=(-0.03,0.088))
#plt.imshow(imdata,cmap="gray",clim=(-0.05,0.058))
plt.show()

"""
PIXELWISE OPERATIONS - type of image data we have put on display is an array. shape shows the image is a Numpy array 
2150  2150. retrieved s the brightness value of the pixel at x = 1200, y = 1400.
"""
type(imdata)
imdata.shape
imdata[1400][1200]

"""
Operations on the SDSS data file frame-g-007923-5-0307.fits downloaded from https://dr9.sdss.org/fields/ 
Search by Object Coordinates for RA 20.0 and Dec 20.0 and click on the link €-band FITS

"""
hdulistS=fits.open("frame-g-007923-5-0307.fits")
imdataS=hdulistS[0].data
imdataS
lowerOne = np.percentile(imdataS,1)
lowerOne
upperOne = np.percentile(imdataS,99)
upperOne
plt.clf()
plt.imshow(imdataS,cmap="gray",clim=(lowerOne,upperOne))
plt.show()
#plt.savefig("sdss-py.pdf",bbox_inches="tight")

"""
Aperture Photometry - SAOImage DS9 (developed by Smithsonian Astrophysical Observatory located at  Cambridge, Massachusetts http://ds9.si.edu/) 
Sort the catalog by gmag in increasing order, pick star with (choose the SDSS DR9 catalog. Sort the catalog by gmag in increasing order so you 
can pick out specific values for gmag. Go to the star with gmag 19.659. It at around RA 20.0714 and Dec +19.9777, corresponding to the pixel 
coordinates X=1819, Y=1215. xlim and ylim zoom in onto those locations;
"""

centerX = 1819
centerY = 1215
plt.xlim(centerX-100,centerX+100)
plt.ylim(centerY-75,centerY+75)
plt.show()

# add a circle to our diagram, centered on the star,centered on (1819,1215) with radius 10
thisCircle = plt.Circle((centerX, centerY), 10, color="r",fill=False,lw=2)
plt.gca().add_artist(thisCircle)
plt.show()
# repeat those commands with radius 20. the outer circles mark the area for determining the background brightness. 
thisCircle = plt.Circle((centerX, centerY), 20, color="r",fill=False,lw=2)
plt.gca().add_artist(thisCircle)
plt.show()

# Next, do aperture photometry. we determine the sum of pixel brightness values in the outer circle, as well as the area of that outer circle in pixels.
radius=20
photCollector=np.array([])
for ii in range(centerX-radius, centerX+radius):
    for jj in range(centerY-radius,centerY+radius):
        distance = np.sqrt((ii-centerX)**2 + (jj-centerY)**2 )
        if distance < radius:
            photCollector= np.append(photCollector, imdataS[jj][ii])
C1 = np.sum(photCollector)
A1 = len(photCollector)
C1
A1

"""
M16 the Eagle Nebula - hst (Hubble Space Telescope), WFPC2 (Wide-Field and Planetary Camera 2) on that telescope, wf means downloading the wide-field camera images. 
f502, f656 and f673 denote different filters placed before the camera for these respective images. We will combine 3 images into a false-color images, corresponding
to red, green, and blue.
hst_05773_05_wfpc2_f502n_wf
hst_05773_05_wfpc2_f656n_wf
hst_05773_05_wfpc2_f673n_wf
"""
?
"""
PROFILES - Download mage C_3198_RO_MOM1_THINGS.FITS,  version of the ment 1file, for the galaxy NGC 3198, from THINGS (The HI Nearby Galaxy Survey ), 
at http://www.mpia.de/THINGS/Data.html. Very Large Array (VLA) in Socorro, New Mexico.This is a radial velocity map,with each pixel showing the average speed 
at which atomic hydrogen gas in that region of the galaxy moves away from us or towards us. 
* DS9 also has the tools to create brightness profiles from astronomical images
"""
?
"""
SIMULATION - e.g. 1) provide a point of comparison for observations 2) IllustrisTNG27 simulation follow a cubic region within the cosmos from shortly after the Big Bang to the present. 
3) This example is the EULER METHOD of the harmonic oscillatora, STEP-BY-STEP NUMERICAL INTEGRATION: A particle with mass m, which can move only in the (horizontal) x direction, is fixed 
to the wall with a spring. If the particle is displaced from its rest position at x = 0, the spring exerts a force following Hooke law, Fx = , with k the spring constant. Its equation
of motion, ma = ,linking the x acceleration a and the force using Newton second law, is readily solved analytically. The solution is x(t)= A ,where the angular frequency 
is linked to the oscillation period T by the definition  = 2/T ,and the equations of motion demand 	 = . Differentiating the orbit equation once with respect to time, we have 
v = s(),and differentiating withrespect totime once more ,a = -2 An() = /m.

To simulate the system: find a solution numerically, look at very small time interval, all of the changes will be approximately linear, dx=v.eplace the infinitesimally small interval dt
by a finite small interval . if we know the particle x position at one time t, we can estimate its position at a slightly later time t+ as x(t+)=x(t)+v(t).The rate of change of 
the velocity is the acceleration, which by Newton second law F=mis linked to the force acting on the particle.Thus, to obtain the velocity at some time t+, with the approximation
v(t+)=v(t)+(t)=v(t)+F(t)/m.
Now, discretize the whole problem: consider time steps ti, with i=1,,N, and evaluate the position and the velocity of our particle at each step. We choose the times ti equidistant, 
with t(i+1)= for all i, for some fixed, small  (much smaller than the system natural period T).
Differential equations do not completely determine what is happening. It is necessary to specify initial conditions in order to define a unique solution.let us choose an initial position x0 
and initial speed v0 for our particle. Let xi be the object position at time ti, vi its velocity in x direction at that time, ai its acceleration and Fi the force acting on it at the time.
v(i+1)=vi+ai=vi+1/mFi , xi+1=xi+vi.The process of following the evolution step by step is called numerical integration, and the simple algorithm we have given for going from one step
to the next is called Euler method. 

"""
import numpy as np
import matplotlib.pyplot as plt
k=0.5
m=1.0
numberOfSteps = 30000
DeltaT = 0.001
tCollector=np.linspace(0,numberOfSteps*DeltaT,numberOfSteps+1)
# Initial conditions:
xCollector=[1.0]
yCollector=[1.0]
xydifference =[0.0]
vCollector=[0]
for ii in range(numberOfSteps):
    # numerical simulation   
    xNew = xCollector[-1] + DeltaT*vCollector[-1]
    vNew = vCollector[-1] + DeltaT*(-k/m*xCollector[-1])
    # analytical calculation    
    yNew =  np.sin(np.pi/2-np.sqrt(k/m)*tCollector[ii])
    # append to the array 
    xCollector.append(xNew)
    vCollector.append(vNew)
    yCollector.append(yNew)
    # calculate the difference numerical vs analytical
    xydifference.append(xNew-yNew)
    
    #print("ii ={}".format(ii))
    #print("tCollector = {}".format(tCollector[ii]))
    #print("xCollector = {}".format(xCollector[ii]))
    #print("yCollector = {}".format(yCollector[ii]))
    #print("xydifference = {}".format(xydifference[ii]))

# plot the xCollector(numerical) & yCollector(analytical) vs time    
plt.clf()
plt.subplots_adjust(bottom=.2, left=.2)
plt.xlabel("Time")
plt.xlim(tCollector)
#plt.ylabel("Numerical & analytical")
#plt.ylim(-1.1,1.1)
#plt.plot(tCollector,xCollector)
#plt.plot(tCollector,yCollector)

# plot the difference xCollector(numerical) vs yCollector(analytical)
# the differences are getting larger over time, so the numerical simulation is unstable in this sense.
plt.ylabel("Difference - numerical vs analytical")
plt.ylim(-0.007,0.007)
plt.plot(tCollector,xydifference)
plt.show()

"""
VERLET - an algorithm to introduces “half-step” velocities, to mitigate the unstability problem, for a better-behaved numerical integration.
The velocity Verlet algorithm is unstable in the long-term too, with the error increasing over time. But the simple of expedient of adding 
the half-step velocity has greatly improved the accuracy. 
"""
k=0.5
m=1.0
#numberOfSteps = 30000
numberOfSteps = 30000
DeltaT = 0.001
finalT =numberOfSteps*DeltaT
tCollector=np.linspace(0,finalT,numberOfSteps+1)
# Initial conditions:
xCollector=[1.0]
yCollector=[1.0]
xydifference=[0.0]
vCollector=[0]

for ii in range(numberOfSteps):
    # numerical simulation  
    #vHalf = vCollector[-1] + 0.5*DeltaT*(-k/m*xCollector[-1])
    xNew = xCollector[-1] + 0.5*DeltaT*vCollector[-1]
    vNew = vCollector[-1] + 0.5*DeltaT*(-k/m*xCollector[-1])
    # analytical calculation 
    yNew =  np.sin(np.pi/2-np.sqrt(k/m)*0.5*tCollector[ii])
    # append to the array 
    xCollector.append(xNew)
    vCollector.append(vNew)
    yCollector.append(yNew)
    # calculate the difference numerical vs analytical
    xydifference.append(xNew-yNew)   
    #print("ii ={}".format(ii))
    #print("tCollector = {}".format(tCollector[ii]))
    #print("xCollector = {}".format(xCollector[ii]))
    #print("yCollector = {}".format(yCollector[ii]))
    #print("xydifference = {}".format(xydifference[ii]))

# plot the xCollector(numerical) & yCollector(analytical) vs time    
# plt.clf()
plt.subplots_adjust(bottom=.2, left=.2)
plt.xlabel("Time")
#plt.ylabel("Numerical & analytical")
plt.xlim(tCollector)
#plt.ylim(-1.1,1.1)
#plt.plot(tCollector,xCollector)
#plt.plot(tCollector,yCollector)
y=xydifference
# plot the difference xCollector(numerical) vs yCollector(analytical)
plt.ylabel("Difference - numerical vs analytical")
plt.ylim(-0.007,0.007)
plt.plot(tCollector,xydifference)
plt.show()

"""
TWO-DIMENSIONAL SIMULATION - The motion of a test particle around a central mass under the influence of the central mass’s (Newtonian) gravity, which provides a model for the orbit of a planet around a star.
Let us put the central mass into the origin of our coordinate system. We treat the x and y components of the motion separately as well as the 2 directons of the force (vector). For the half-step velocity, 
calculate the accelerations in x and y direction, starting with the magnitude of the acceleration, which follows directly from Newton’s law. Then, evolve the position one time step further, re-calculate 
the acceleration for the new position, and use those to update the x and y component of the velocity for the second half of the time step.
"""
import numpy as np
import matplotlib.pyplot as plt
numberOfSteps = 30000
DeltaT = 0.0001
accFac = 39.48 # Corresponding to one solar mass in au per square year
finalT=numberOfSteps*DeltaT
tCollector=np.linspace(0,finalT,numberOfSteps+1)
# Initial conditions:
xCollector=[1.5]
vxCollector=[0] 
yCollector=[0.0]
vyCollector=[2.0]
for ii in range(numberOfSteps):
  rNow = np.sqrt(xCollector[-1]**2+yCollector[-1]**2)
  accNow = -accFac/rNow**2 #adjust the accelleration by distance from focus
  accNowx= accNow*xCollector[-1]/rNow
  accNowy= accNow*yCollector[-1]/rNow
  #print("ii ={}".format(ii))
  #print("xCollector = {}".format(xCollector))
  #print("yCollector = {}".format(yCollector))
  #print("rNow = {}".format(rNow))
  #print("accNow = {}".format(accNow))
  #print("accNowx = {}".format(accNowx))
  #print("accNowy = {}".format(accNowy))
  vxHalf = vxCollector[-1] + 0.5*DeltaT*accNowx
  vyHalf = vyCollector[-1] + 0.5*DeltaT*accNowy
  xNew = xCollector[-1] + DeltaT*vxHalf
  yNew = yCollector[-1] + DeltaT*vyHalf
  rNew = np.sqrt(xNew**2 + yNew**2)
  accNew = -accFac/rNew**2
  accNewx = accNew*xNew/rNew
  accNewy = accNew*yNew/rNew
  vxNew = vxHalf + 0.5*DeltaT*accNewx
  vyNew = vyHalf + 0.5*DeltaT*accNewy
  xCollector.append(xNew)
  yCollector.append(yNew)
  vxCollector.append(vxNew)
  vyCollector.append(vyNew)

# plot the xCollector vs yCollector - If it is an elliptical orbit, confirm Kepler’s first law: the orbit of a planet orbiting a central mass is an ellipse, with the central mass in one of the focal points     
plt.clf()
plt.subplots_adjust(bottom=.2, left=.2)
plt.xlabel("x")
plt.xlim(xCollector)
plt.ylabel("y")
plt.ylim(-0.48,0.48)
plt.plot(xCollector,yCollector, lw=1.0)
plt.axhline(0.0,color="g",linestyle="dashed")  # one of the focus points at x = 0.0
plt.axvline(0.0,color="m",linestyle="dashed")  # one of the focus points at y = 0.0
plt.show()

# plot the reference ellipse to compare with the simulated orbit.
majoraxis = np.max(xCollector) - np.min(xCollector) # major axis  a = 1.623 au.
minoraxis = np.max(yCollector) - np.min(yCollector) # minor axis  b = 0.860 au.
xc = np.min(xCollector) + (np.max(xCollector) - np.min(xCollector))/2  #x-position of the center
yc = np.min(yCollector) + (np.max(yCollector) - np.min(yCollector))/2  #y-position of the center
eccentricity =  np.sqrt(1 - minoraxis**2/majoraxis**2) # eccentricity e = 0.848.

#plt.clf()
#plt.xlabel("x")
#plt.ylabel("y")
#plt.subplots_adjust(bottom=.2, left=.2)
theta = np.linspace(0, 2*np.pi, 100)
plt.plot( xc+majoraxis*np.cos(theta)/2 , yc+minoraxis*np.sin(theta)/2, "r",lw=1.0)
plt.show()

"""
compare analytical solution and simulation quantitatively - take each simulated point, calculate the position angle θ and distance r
from the focus point, and compute the absolute value of the difference between the simulated value r and the analytical value r(θ)
"""
diffCollector=[]
for x,y in zip(xCollector,yCollector):
    r=np.sqrt(x**2+y**2) # simulated value r for the ellipse
    theta = np.arctan2(y,x) # angle in radian
    anr = 0.5*(np.max(xCollector) - np.min(xCollector))*(1-eccentricity**2)/(1-eccentricity*np.cos(theta)) # analytical r(θ) for an ellipse
    diffr = np.sqrt((r-anr)**2)
    diffCollector.append(diffr)
    
#The histogram of the values contained in diffCollector - shows the cascade-like  systematic errors involved in the simulation. The largest deviation is 4/10 000 of an au (half axis length of our orbit), i.e. deviation is fairly small, and simulated planet appears to have an elliptical orbit.
plt.clf()
plt.hist(diffCollector,bins=100)
plt.show()

"""
Kepler’s second law says that the connecting line between the planet and the central mass sweeps out equal areas in equal time intervals. Each of our time steps defines the same time interval, so if we calculate the triangle swept out in each time step (whose three vertices are the planet’s 
position at the beginning and at the end of the time step, and the location of the central mass), we should always obtain the same area.
For each triangle,  x and y coordinates of all three vertices can calculate all the side lengths a,b,c using the Pythagorean theorem. Heron’s formula calculate the triangle’s area as A = √(s(s−a)(s−b)(s−c)), where s = (a+b+c)/2 is the triangle’s semi-perimeter
The following bit of code collects the relative deviation of each such triangle area from the mean in an array relativeDiff
"""
areaCollector=np.array([])
for x1, x2, y1, y2 in zip(xCollector[1:],xCollector[:-1],yCollector[1:],yCollector[:-1]):
  a = np.sqrt(x1**2+y1**2)
  b = np.sqrt(x2**2+y2**2)
  c = np.sqrt((x1-x2)**2+(y1-y2)**2)
  s = 0.5*(a+b+c)
  A = np.sqrt(s*(s-a)*(s-b)*(s-c))
  areaCollector = np.append(areaCollector,A)
averageArea=np.average(areaCollector)
relativeDiff = (areaCollector-averageArea)/averageArea

# The histogram of the values in relativeDiff shows that all those areas, swept out in the same time interval, are indeed very close to their average value
# The distribution shows a strong maximum at the average area value, with small (a few parts in a trillion!) fluctuations to smaller and larger values.
plt.clf()
plt.xlabel("Histogram of relative difference \nfrom averaged triangle areas for each time step")
plt.hist(relativeDiff,bins=47)
plt.show()
"""
Kepler’s third law -  the orbital periods T is proportional to major elliptical half axis a as a**3/T**2. The advanced form of Kepler’s law found by Newton is a**3/T**2 = GM/4π**2
The plot of y coordinate of our planet against time is unsurprisingly periodical.
"""
plt.clf()
plt.subplots_adjust(bottom=.2, left=.2)
plt.xlabel("Time in years")
plt.xlim(xCollector)
plt.ylabel("y coordinate in au")
plt.ylim(-0.48,0.48)
plt.plot(tCollector,yCollector, lw=1.0)
plt.show()
"""
We have already estimated a. Let us do the same for period T. We fold the time evolution by assuming a value for the period T, 
and define the phase as φ = np.mod(tCollector/T, 1), i.e. all integer multiples of the period T get mapped to 0, and all times  
written as t = (n + φ) · T with integer n and 0 ≤ φ < 1 get mapped to φ. After a few dozen tries, the final round with a 
microscopic look at the steepest curve region via plt.xlim(0.475,0.525), arrive at T = 0.7313a(year). We could automate this
sorting the phase values into different arrays indexed by the integer part of t/T, and minimising the differences between those 
partial curves. This is very similar to how you determine the orbital of an exoplanet by folding the light curve data (from the 
transit method) or Doppler shift data (in the radial velocity method).
"""
T = np.array([0.7313 for ii in range(30001)]) #fill the array T with estimated value
φ = np.mod(tCollector/T, 1)
#len(φ)
#np.info(φ)
#np.info(phase)
#φ[27091:27991]
plt.clf()
plt.subplots_adjust(bottom=.2, left=.2)
plt.xlabel("Phase")
plt.xlim(-0.05,1.05)
#plt.xlim(0.475,0.525)
plt.ylabel("y coordinate in au")
plt.ylim(-0.48,0.48)
plt.plot(φ,yCollector, lw=1.0)
plt.show()

"""
Our final test is to see if this T value indeed satisfies equation a**3/T**2 = GM/4π**2, with right-hand side = 1 au**3/a**2,
since the Earth does have a semimajor axis of length 1 au and an orbital period of 1 year. Our simulation satisfies
(a/1au)**3 · (1a/T)**2= 0.99991.The two values coincide up to one part in 10 000. So our simulation reproduces Kepler’s third law.
"""
((majoraxis/2)**3)/((0.7313)**2)

"""

"""

