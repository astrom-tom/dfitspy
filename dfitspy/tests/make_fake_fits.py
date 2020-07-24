from astropy.io import fits
import fitsio

spec = 'test5.fits'
hdul = fits.open(spec)
header = hdul[0].header
#print(type(dict(header)), list(header.values()))
#hdul[0].header['EXTRA'] = 'extra keyword'
#hdul.writeto('test_extra_keyword.fits')
s = fitsio.FITS(spec)
print(len(s))
