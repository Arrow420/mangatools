from setuptools import find_packages, setup

# Read-in the README.md
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='mangatools',
    version='0.2.2',
    description='tools for manga',
    url='https://github.com/Arrow420/mangatools',
    license='MIT',
    author='Arrow',
    author_email='arrowsoftwaresolutions@gmail.com',
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords='manga, tools, python',
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        'click',
        'requests',
        'natsort'
    ],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "mangatools=mangatools.cli:mangatools",
        ],
    },
)