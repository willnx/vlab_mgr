# -*- coding: UTF-8 -*-
"""
Defines how to build the Python package
"""
from setuptools import setup, find_packages


setup(name="vlab-mgr",
      author="Nicholas Willhite",
      version='0.0.0',
      packages=find_packages(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: System Administration',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
      ],
      description="CLI for administrating a vLab server",
      long_description=open('README.rst').read(),
      entry_points={'console_scripts' : 'vlab=vlab_cli.vlab:cli'},
      install_requires=['click', 'pyyaml'],
      )
