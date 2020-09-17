from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

#Building a NN with two inps, three hidden layers and one output
nn = buildNetwork(2,3,1, bias=True, hiddenclass=TanhLayer)


#Making a dataset that makes a match with the network input and output sizes
norgate = SupervisedDataSet(2,1)


#Creating a data set exclusively for testing
nortrain = SupervisedDataSet(2,1)


#Add the input and target values to the dataset
norgate.addSample((0,0), (1,))
norgate.addSample((0,1), (0,))
norgate.addSample((1,0), (0,))
norgate.addSample((1,1), (0,))


#Add inp and target values to dataset now training
nortrain.addSample((0,0),(1,))
nortrain.addSample((0,1),(0,))
nortrain.addSample((1,0),(0,))
nortrain.addSample((1,1),(0,))

#Train the network
the_trainer = BackpropTrainer(nn, norgate)

#run loop 1000 times to train
for epoch in range(1000):
    the_trainer.train()
the_trainer.testOnData(dataset=nortrain, verbose=True)
