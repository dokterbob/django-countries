from setuptools import setup, find_packages

try:
    README = open('README.rst').read()
except:
    README = None

try:
    VERSION = __import__('countries').__version__
except:
    VERSION = 0.1

setup(
    name='django-countries',
    version=VERSION,
    description='Provides various Django utilities for a complete list of world countries.',
    long_description=README,
    # Get more strings from http://www.python.org/pypi?:action=list_classifiers
    author='Alex Kuhl',
    author_email='',
    url='http://github.com/alexkuhl/django-countries',
    download_url='',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False, # because we're including media that Django needs
    package_data = {'': ["*.xml"]},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
