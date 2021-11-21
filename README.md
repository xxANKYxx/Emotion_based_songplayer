# Emotion_based_songplayer

The interaction between human beings and computers will be more natural if computers are able to perceive and respond to human non-verbal communication such as emotions.
In recent years deep learning has progressed much in the field of image classification.In  this project i have created song player that captures emotion and plays song related to it.

for eg==
1. if detected happy ,it plays happy song
2.if detected frustated/anger ,it plays relaxing song
3.and we can add more song for different emotions

Model weights are saved to HDF5 format. This is a grid format that is ideal for storing multi-dimensional arrays of numbers. 
Keras provides the ability to describe any model using JSON format with a to_json() function. This can be saved to file and later loaded via the model_from_json() function that will create a new model from the JSON specification.
Above Model.json file is used to store the model Structure.
The model and weight data is loaded from the saved files and a new model is created. It is important to compile the loaded model before it is used. This is so that predictions made using the model can use the appropriate efficient computation from the Keras backend.

 
Model weights are all the parameters (including trainable and non-trainable) of the model which are in turn all the parameters used in the layers of the model. And yes, for a convolution layer that would be the filter weights as well as the biases.Here the model_weights.h5 file contains all the model's weight.

