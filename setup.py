from setuptools import find_packages, setup

setup(
    name='mangatools',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click>=7.1.2',
        'requests>=2.25.1'
    ],
    entry_points='''
    [console_scripts]
    mangatools=mangatools.mangatools:mangatools
    '''
)