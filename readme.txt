webcamPyc
=========

Python2/pygame script taking photos with webcam

Requirements : 
  -python2
  -python-pygame (get it using pip or apt-get)
  -images2gif which I provided (because I had an issue with the original one so changed a line, 426) but did not write. It is Almar Klein, Ant1 and Marius van Voorden work
=========
  How to use : 
  First, it doesnt work on microsoft windows, if you want to port it, please yourself :) . It has been tested on linux mint 17 and Xubuntu 14.10.
  
  This is basically a CLI script. Following are the ways you can call it in your terminal :
   1 $python ./webcamPyc.py  
    this will take one .jpg picture.
   2 $python ./webcamPyc.py 50 -gif 
    this will take a series of 50 .jpg and process them into an animated gif
   3 $python ./webcamPyc.py 50 -gif -clean 
    this will take a series of 50 .jpg, make an animated gif out of it and delete the .jpg files.