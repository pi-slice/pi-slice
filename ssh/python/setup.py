from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='pi-slice-ssh-tunnel',
    version='0.1.0',
    description='Reverse tunnel for systemd',
    url='https://github.com/pi-slice/pi-slice',
    author='Pi-Slice',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ],
    install_requires=['paramiko'],
)
