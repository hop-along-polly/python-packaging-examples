# setup.py
from setuptools import setup, find_packages

setup(
  name='pytranslator', # Names the package. pip list will show package-greeter
  version='0.1.0', # it's best practice to assign a version #
  packages=find_packages() # Searches the working directory for folders containing python packages
)
