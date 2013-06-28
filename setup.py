import os
from setuptools import setup, find_packages

DESCRIPTION = 'Plugin for Django-CMS to handle containers with grids'

CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Development Status :: 4 - Beta',
]

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-cmsplugin-container',
    version='0.1.0',
    author='Jacob Rief',
    author_email='jacob.rief@gmail.com',
    description=DESCRIPTION,
    long_description=read('README.rst'),
    url='https://github.com/jrief/django-cmsplugin-container',
    license='MIT',
    keywords = ['django', 'django-cms', 'cmsplugin'],
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=['Django>=1.5'],
    packages=find_packages(),
    include_package_data=True,
)
