from setuptools import find_packages, setup

PACKAGE_NAME = 'mangatools'

# Read-in the README.md
with open('README.md', 'r') as f:
    readme = f.readlines()
readme = ''.join(readme)

setup(
    name='mangatools',
    version='0.1.0',
    description='tools for manga',
    url='https://github.com/Arrow420/mangatools',
    license='MIT',
    author='Arrow',
    author_email='arrowsoftwaresolutions@gmail.com',
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords='anime, tools, python',
    packages=find_packages(),
    install_requires=[
        'click',
        'requests'
    ],
    zip_safe=True,
    entry_points='''
    [console_scripts]
    mangatools=mangatools.mangatools:mangatools
    '''
)
