### An Example Of A Neural Net
![neural](https://user-images.githubusercontent.com/31806568/89740302-65b0aa80-da7f-11ea-8903-448eac79d513.png)

[i=1,i]Σ(Vi * Wi)+bi
This means our output would V1W1+V2W2+V3W3+V4W4+b1+b2+b3+b4 if we have four elements in our input layer.
The output is called our weighted sum.
Say I play 1000 times a game of crashdown and I get a number of inputs and a number of outputs.
I will decide a recommened direction(usually the lowest set of cubes should be where the set of cubes should connect).Take the state of the cube block and look at it's neighbors to the right of it,below it and to the left of it.Next,
I take the output and generate an output are no more lines to populate(dead/end of game) or more lines to populate(continue playing). The network will then start to the look at the outputs and start to adjust the biases and weights to 
properly get a correct output. The network always will learn from past mistakes and will adjust the weights and biases


### Sigmoid Function
```
	A sigmoid function has a range of -1 to 1 and its domain is all reals. The closer the input is to infinity, the closer the ouput is to 1.
	The closer the input is to negative infinity the closer the output is to -1. This adds a degree of complexity to the network.
```

### Activation Function
```
	An activation function would be: the weighted sum and we would apply the activation function to it which is f(x). We would take the weighted sum
	as an input and capital F(X) would be our output which is referred to as our output neuron.
	This is done so that when we adjust our weights and biases and we bring in our activation function into play we can get a way more complex function as opposed
	to the normal linear regression aka y=mx+b trend.
```

### Rectify Linear Unit Activ Func PII
```
	Takes all the numbers that are negative and outputs 0. The values that are positive are turned into more positive values.
```

### How to adjust data and know how much are we off and how much to tune by?
```
	We use what's called a loss function! A loss function will tell you how wrong your answer is similar to a percent diff in Physics
```
### neural network description
```
	A neural network is composed of a ton of different neurons that are connected to a hidden layer or multiple hidden layers of neurons.
The more interconnected they are makes them more complex which gives them the ability to solve more complex problems.
This is because we can generate more combinations of inputs. Hidden layer neurons give us the ability to solve our
problems and have more weights and biases. This enables us to be more accurate to produce certain models.
```
