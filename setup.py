import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()


setup(name="aroundme",
      version="1.0",
      description="Find interesting places around you",
      long_description=README,
      long_description_content_type="text/markdown",
      url="https://github.com/rishabh570/what-is-around",
      author="Rishabh Rawat",
      author_email="icode365@gmail.com",
      license="MIT",
      packages=["aroundme"],
      include_package_data=True,
      install_requires=["googlemaps"],
      entry_points={
        "console_scripts": ["aroundme=aroundme.__main__:main"]
      },
      )