from setuptools import setup

setup(name="what's around",
      version="1.0",
      description="Find good places around you",
      long_description=README,
      long_description_content_type="text/markdown",
      url="https://github.com/rishabh570/what-is-around",
      author="rishabh rawat",
      author_email="icode365@gmail.com",
      license="MIT",
      packages=["app"],
      include_package_data=True,
      install_requires=["googlemaps"],
      entry_points={
        "console_scripts": ["what's around = app.__main__:main"]
      },
      )