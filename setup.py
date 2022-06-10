from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='syringedriver',
    author='Thomas Morvan, Mathias Lechelon',
    author_email='thomas.MORVAN@univ-amu.fr, mathias.LECHELON@univ-amu.fr',
    version='0.0.1',
    description='Syringe driver',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/CENTURI-Hackathon-2022/syringe-driver',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    install_requires=['scipy', 'numpy', 'matplotlib',
                        'ipython', 'jupyter'],
)
