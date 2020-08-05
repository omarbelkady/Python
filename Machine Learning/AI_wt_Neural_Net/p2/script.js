//How to start Creating an object and we are going to have 3 different hidden 
//layers one with 4 nodes, one with 5 nodes and one with 6 nodes
const myNet = new brain.NeuralNetwork()

//give our NN information
const myData = [
	{
		//every object has an input property and an
		//output property
		input: [r:0, g:0, b:0],
		output: [1]
	},
	{	
		input: [r:1, g:0, b:1],
		output: [0]
	}
]
myNet.train(myData)

const diagram = document.getElementById('diagram')

//Setting our inner HTML to this
diagram.innerHTML=brain.utilities.toSVG(myNet)
