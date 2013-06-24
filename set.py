#from distutils.core import setup
#import py2exe
#
#setup(console=[{'script':'weiboapp.py'}])

#!/usr/bin/env python
from distutils.core import setup
import py2exe

setup(windows=["WeiBoForm.py"],
    data_files=[("", ["face.ico"])]
    )



