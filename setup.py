from setuptools import setup

long_description = open("README.md", "r").read()

setup(
    name='latlon3',
    version='1.0.4',
    packages=[''],
    url='https://github.com/search5/latlon',
    license='GNU General Public License v3 (GPLv3)',
    author='Lee persy ji-ho',
    author_email='search5@gmail.com',
    description='Methods for representing geographic coordinates',
    scripts=['__init__.py', 'latlon.py'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['six', 'pyproj'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering"
    ]
)
