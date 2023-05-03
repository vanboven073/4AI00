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