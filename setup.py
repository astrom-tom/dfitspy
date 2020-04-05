from setuptools import setup

__version__ = '20.4.1'
__place__ = 'ESO Paranal observatory'
__credits__ = "Romain Thomas"
__license__ = "GNU GPL v3"
__maintainer__ = "Romain Thomas"
__email__ = "the.spartan.proj@gmail.com"
__status__ = "released"
__website__ = "https://astrom-tom.github.io/dfitspy/build/html/index.html"

setup(
   name = 'dfitspy',
   version = __version__,
   author = __credits__,
   packages = ['dfitspy'],
   entry_points = {'gui_scripts': ['dfitspy = dfitspy.__main__:main',],},
   description = 'A dfits|fitsio implementation in python',
   license = __license__,
   url = __website__,
   python_requires = '>=3.6',
   install_requires = [
       "numpy >= 1.14.3",
       "fitsio == 0.9.11",
       "python-magic >= 0.4.15",
   ],
   include_package_data=True,
)
