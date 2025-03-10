# To mask sources with DS9 region
# Written by Ramij Raja
# Date: 10 May 2023
#########################################
import numpy as np
from astropy.io import fits
from astropy.io.fits import getdata
import pyregion
##########################
# INPUTS
fits_image = 'A85_700MHz_GWB_rob0_uvsub4kl_bm25_6-MFS-image.pbcor.image.tt0.fits'
ds9_reg = 'RG_mask.reg'

#############################
# Main Code 
#############################
data, hdr = getdata(fits_image, header=True)

f = fits.open(fits_image)

r = pyregion.open(ds9_reg)

r = r.as_imagecoord(f[0].header)

shape = (hdr['NAXIS1'], hdr['NAXIS2'])

mymask = r.get_mask(hdu=f[0],shape=shape)

p = np.array(hdr['NAXIS1']*[hdr['NAXIS1']*[0.]])

q = p + mymask

q[q == 1.] = 'NaN'

data[0,0,0:,0:] = data[0,0,0:,0:] + q

fits.writeto(fits_image.replace(".fits", "_dMASKED.fits"), data, hdr, overwrite=True)

print(' ')
print('Output Image: '+fits_image.replace(".fits", "_dMASKED.fits"))
print(' ')
print('###########################  DONE  #########################')
print('Enjoy!, ... or Not???')
# THE END
