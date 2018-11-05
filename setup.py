from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pyromine',
    version='0.1.0',
    description='a mcpe python server',
    long_description=readme,
    author='Clark Dwain Luna',
    author_email='lclarkdwain@outlook.com',
    url='https://github.com/pyromine/pyromine',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)