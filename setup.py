from setuptools import setup

setup(name='pyIAST',
    version='1.0',
    description='Ideal Adsorbed Solution Theory',
    url='https://github.com/CorySimon/pyIAST',
    install_requires=['numpy', 'scipy', 'pandas', 'matplotlib'],
    author='Cory M. Simon',
    author_email='CoryMSimon@gmail.com',
    license='MIT',
    package_dir={'':'src'},
    packages=[''],
    zip_safe=False)