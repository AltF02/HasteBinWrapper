import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="HasteBinWrapper",
    version="0.2",
    author="Matthew",
    description="A wrapper for HasteBin",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DankDumpster/HasteBinWrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
