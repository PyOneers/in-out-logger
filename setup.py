import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="inoutlogger",
    version="1.0.3",
    author="Pankaj Suthar",
    author_email="sutharpanks.opensource@gmail.com",
    description="Decorator based utility to implement Entry-Exit logs for methods",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PanksSuthar/InOutLogger",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
