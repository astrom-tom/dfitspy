from setuptools import setup
import dfitspy.__info__ as dfits


setup(
   name = 'dfitspy',
   version = dfits.__version__,
   author = dfits.__author__,
   packages = ['dfitspy'],
   entry_points = {'gui_scripts': ['dfitspy = dfitspy.__main__:main',],},
   description = 'A dfits|fitsio implementation in python',
   python_requires = '>=3.6',
   install_requires = [
       "numpy >= 1.14.3",
   ],
   include_package_data=True,
)
