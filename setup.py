from setuptools import find_packages, setup

PACKAGE_NAME = 'mangatools'

# Read-in the README.md
with open('README.md', 'r') as f:
    readme = f.readlines()
readme = ''.join(readme)

setup(
    name='mangatools',
    version='0.2.0',
    description='tools for manga',
    url='https://github.com/Arrow420/mangatools',
    license='MIT',
    author='Arrow',
    author_email='arrowsoftwaresolutions@gmail.com',
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords='manga, tools, python',
    package_dir={"": "mangatools"},
    packages=find_packages(where="mangatools"),
    python_requires=">=3.6",
    install_requires=[
        'click',
        'requests',
        'wheel',
        'natsort'
    ],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points='''
    [console_scripts]
    mangatools=mangatools.mangatools:mangatools
    '''
)
