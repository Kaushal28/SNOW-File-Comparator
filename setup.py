import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="snowcomp",
    packages=['snowcomp'],
    package_dir={'snowcomp': 'snowcomp'},
    version="0.1.4",
    author="kaushal28",
    entry_points={'console_scripts': ['snowcomp = snowcomp.__main__:main' ]},
    author_email="shah.kaushal95@gmail.com",
    description="Compares files from different branches and spits out deleted files",
    url="https://github.com/Kaushal28/SNOW-File-Comparator.git",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'GitPython == 2.1.11'
   ],
   classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)