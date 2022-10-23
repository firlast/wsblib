from setuptools import setup
from wsblib import __version__

setup(
    author='Jaedson Silva',
    author_email='imunknowuser@protonmail.com',
    name='wsblib',
    version=__version__,
    description='Base library for other web servers.',
    packages=['wsblib'],
    install_requires=['http_pyparser==0.4.1']
)