# To mask sources at N sigma RMS
# Written by Ramij Raja
# Date: 19 June 2023
#########################################
import numpy as np
from astropy.io import fits
from astropy.io.fits import getdata
###########################################
# INPUTS
fits_image = 'A85_1.28GHz_spix_100uv43kl_rob0_bm25-MFS-image.fits'
image_rms = 20*10**-6 # Jy/beam
mask_level = 3 # Mask at N sigma level
#############################
# Main Code 
#############################
data, hdr = getdata(fits_image, header=True)
mi = mask_level * image_rms
data[data >= mi] = np.nan
fits.writeto(fits_image.replace(".fits", "_sMASKED.fits"), data, hdr, overwrite=True)
print('---------------- ')
print('Masked Image: '+fits_image.replace(".fits", "_sMASKED.fits"))
print('---------------- ')
