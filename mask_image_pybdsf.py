# To mask sources with PyBDSF mask file
# Written by Ramij Raja
# Date: 19 June 2023
#########################################
import numpy as np
from astropy.io import fits
from astropy.io.fits import getdata
#############################
# INPUTS
fits_image = 'A85_1.28GHz_spix_100uv43kl_rob0_bm25-MFS-image.fits'
mask_image = 'A85_1.28GHz_spix_100uv43kl_rob0_bm25-MFS-image.pybdsf_island_mask.fits'
#############################
# Main Code 
#############################
data, hdr = getdata(fits_image, header=True)
mdata = getdata(mask_image)

shape = (hdr['NAXIS1'], hdr['NAXIS2'])
p = np.array(hdr['NAXIS1']*[hdr['NAXIS1']*[0.]])
q = p + mdata
q[q == 1.] = 'NaN'
data[0,0,0:,0:] = data[0,0,0:,0:] + q

fits.writeto(fits_image.replace(".fits", "_pMASKED.fits"), data, hdr, overwrite=True)
print('---------------- ')
print('Masked Image: '+fits_image.replace(".fits", "_pMASKED.fits"))
print('---------------- ')
