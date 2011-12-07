#!/usr/bin/env python

from distutils.core import setup

setup(
    name='pwhich',
    version='0.1.0',
    description='Python which - find out where Python modules are located on your drive',
    author='Harry Percival',
    author_email='hjwp2@cantab.net',
    url='https://github.com/hjwp/pwhich',
    download_url='https://github.com/hjwp/pwhich/raw/master/dist/pwhich-0.1.0.linux-x86_64.zip',
    packages=[],
    scripts=['scripts/pwhich.py'],
    classifiers= [
        'Environment :: Console',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
    ],
)

