from setuptools import setup, find_packages
from subprocess import run

run(args=['x86_64-conda_cos6-linux-gnu-gfortran',
          '-o', 'hello/hello', 'hello/hello.f90'])

setup(
    name='hello',
    version='0.0.3',
    packages=find_packages(),
    package_data={'hello': ['hello']},
    include_package_data=True
)
