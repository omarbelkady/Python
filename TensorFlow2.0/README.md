### An Example Of A Neural Net
![neural](https://user-images.githubusercontent.com/31806568/89740302-65b0aa80-da7f-11ea-8903-448eac79d513.png)

[i=1,i]Σ(Vi * Wi)+bi
This means our output would V1W1+V2W2+V3W3+V4W4+b1+b2+b3+b4 if we have four elements in our input layer.
The output is called our weighted sum.
Say I play 1000 times a game of crashdown and I get a number of inputs and a number of outputs.
I will decide a recommened direction(usually the lowest set of cubes should be where the set of cubes should connect).Take the state of the cube block and look at it's neighbors to the right of it,below it and to the left of it.Next,
I take the output and generate an output are no more lines to populate(dead/end of game) or more lines to populate(continue playing). The network will then start to the look at the outputs and start to adjust the biases and weights to 
properly get a correct output. The network always will learn from past mistakes and will adjust the weights and biases
