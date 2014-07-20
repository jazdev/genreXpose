#genreXpose v0.1 Docs
======================

This document gives a quick overview on how to use this library in your projects.

For more technical details on what underlying technologies have been used in building this library, and how does this library work, read this post on my blog: [genreXpose - Quick music audio genre recognition]().


###1. Installation

Download the whole project source from GitHub. Do this by clicking [here](https://github.com/jazdev/genreXpose/archive/master.zip). Once downloaded, extract the source to a directory of your choice. 

The project has the following directory structure:

```
your-working-dir/
 |
 |-docs/
 |  |-README.md
 |
 |-genreXpose/
 |  |-graphs/
 |  |-test/
 |  |-ceps.py
 |  |-classifier.py
 |  |-config.cfg
 |  |-tester.py
 |  |-utils.py
 | 
 |-LICENSE
 |
 |-requirements.txt

```

The ```genreXpose/``` directory contains the main code-base. This directory also contains the ```config.cfg``` file which is used for the configuraton of the software.

* ```graphs/``` will contain all the generated graphs. The graphs are an excellent indicator of the performance of the algorithm.
* ```test/``` houses all the tests.
* The function of the other files will be explained in subsequent sections.

The ```docs/``` directory contains all the relevant documentation of the software. 

The ```LICENSE``` contains important copyright references and redistribution terms.

The ```requirements.txt``` file lists all the requirements that need to be satisfied in order to run this software. 

To install the required packages use the following command: 

``` 
		$ pip install -r /path/to/requirements.txt
```	

###2. Setup & Configuration

All the configuraton can be done using the ```config.cfg``` file. This file follows a particular syntax for storing the configurations. Please respect the syntax if you want to avoid bugs.

This file contains three variables that the user can modify as per his need. Comments begin with a ```#``` symbol and run till the end of a line. Rest everything is supposed to be valid configuration data.

The variables are:
* ```GENRE_DIR``` - This is directory where the music dataset is located (GTZAN dataset) 
* ```TEST_DIR``` - This is the directory where the test music is located
* ```GENRE_LIST``` - This is a list of the available genre types that you can use. Modify this list if you want to work with a subset of the available genres.

Set these three variables according to your system before proceeding to the next steps.

###3. The Dataset


###4. Model Generation & Caching


###5. Testing and Live Usage


###6. Interpreting the Output


###7. Internal Details
