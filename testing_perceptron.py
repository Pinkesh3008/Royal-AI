import numpy as np
from perceptron import Perceptron    #file mathi userdefined class import karyo.
'''

# for 2 inputs

training_inputs=[]
training_inputs.append(np.array([1,1]))
training_inputs.append(np.array([0,1]))
training_inputs.append(np.array([1,0]))
training_inputs.append(np.array([0,0]))


labels=np.array([1,0,0,0])

perceptron = Perceptron(2)   #for 2 inputs
perceptron.train(training_inputs,labels)

inputs = np.array([1,0])
print(perceptron.predict(inputs))
'''

training_inputs=[]
training_inputs.append(np.array([0,0,0]))
training_inputs.append(np.array([0,0,1]))
training_inputs.append(np.array([0,1,0]))
training_inputs.append(np.array([0,1,1]))
training_inputs.append(np.array([1,0,0]))
training_inputs.append(np.array([1,0,1]))
training_inputs.append(np.array([1,1,0]))
training_inputs.append(np.array([1,1,1]))



labels=np.array([0,0,0,0,0,0,0,1])      # providing o/p so when we give new i/p it can predict
                                        # from the previous result.

perceptron = Perceptron(3)   #for 3 objects
perceptron.train(training_inputs,labels)

inputs = np.array([1,1,1])
print(perceptron.predict(inputs))
 
 