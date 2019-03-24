import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='py_microhtml',  
     version='0.1',
     author="Jarno Elonen",
     author_email="elonen@iki.fi",
     description="Minimalistic HTML builder for Python 3.6+ with compact syntax",
     long_description=long_description,
     long_description_content_type='text/markdown',
     url="https://github.com/elonen/py_microhtml",
     py_modules=['microhtml'],
     packages=setuptools.find_packages(),
     install_requires=['pytidylib'],
     test_suite='nose.collector',
     tests_require=['nose'],
     classifiers=[
         "Programming Language :: Python :: 3.6",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
         "Topic :: Text Processing :: Markup :: HTML",
         'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
         'Topic :: Software Development :: Libraries :: Python Modules',
     ],
 )