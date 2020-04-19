import setuptools

setuptools.setup(
     name='HasteBinWrapper',  
     version='0.2',
     scripts=['HasteBin.py'] ,
     author="Matthew",
     description="A wrapper for hastebin",
     url="https://github.com/DankDumpster/HasteBinWrapper",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )

