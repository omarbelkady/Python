//How to start Creating an object
const myNet = new brain.NeuralNetwork()
const diagram = document.getElementById('my-diagram')

//give our NN information
myNet.train([
	{
		//every object has an input property and an
		//output property
		input: [0,0],
		output: [0]
	},

	//Exclusive OR
	{	
		input: [1,0],
		output: [1]
	},
	
	//Exclusive OR
	{	
		input: [0,1],
		output: [1]
	},

	//NOT Exclusive OR
	{
		input: [1,1],
		output: [0]
	},
])


//Setting our inner HTML to this
diagram.innerHTML=brain.utilities.toSVG(myNet)
