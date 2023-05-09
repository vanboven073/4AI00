# 4AI00
Tasks to solve the inverse machine learning problem: Predicting surface tension from dropp images
1.  Generate photo realistic data set in blender, using the provided gen_singledrop.py file.  
2.  Create a pipeline that is able to do edge detection.
3.  Design,train and evaluate Convelutional Neural Network.
4.  (Evaluate Neural Network with "real" figures.) 
5.  (Detirmine if the drop is "clean".)

These general steps can bring some difficulties with them. To ease, solving these steps, some intermediate steps are taken to create the foundation of the solution of each steps. When this foundation is set, the foundation should be converted to the case. This to get the solution of that certain step.

Some intermediate steps will be:
1.  Automate a data generating algorithm, that produces clean images (no wierd shadowing) in blender. 
2.  Do edge detection on these clean images.
3.  Adjust data generating algoritm, such that it produces images with noise.
4.  Do edge detection on these noisy images.
5.  Adjust data generating algoritm, such that it produces photorealistic images with shadowing.
5.  Do edge detection on these images.

# Theoretical Neural Network

## RNN

RNNs can be used to solve problems related to: Time series data, Text data and audio data. These data sets are all sequential, this is not applicable for pictures. As pictures are spatial data.

## CNN

A CNN captures the spatial features of an image. This is known as the arrangement and and relations of pixels. With this information, identification, location, as well as relation with other object in an image. 

Looking at this description of a CNN, we can see that a CNN can be used for this case. Detirmine the surface tension of a drop.

## Edge detection

https://github.com/sniklaus/pytorch-hed

https://medium.com/@nikatsanka/comparing-edge-detection-methods-638a2919476e#:~:text=Sobel%20Operator,inexpensive%20in%20terms%20of%20computations
