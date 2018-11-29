from setuptools import setup

setup(name="aroundme",
      version="1.0",
      description="Find interesting places around you.",
      long_description='aroundme is a basic utility that lets you find interesting places around you just by providing the kind of place you are looking for.',
      long_description_content_type="text/plain",
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