//How to start Creating an object and we are going to have 3 different hidden 
//layers one with 4 nodes, one with 5 nodes and one with 6 nodes
const myNet = new brain.NeuralNetwork()

const guess = myNet.run(color)[0]

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

//Setting our inner HTML to this
diagram.innerHTML=brain.utilities.toSVG(myNet)

//Select different color
const colorElem = document.getElementById('color')

//Select the guess Text element
const guessElem = document.getElementById('guess')

//Selecting the white button
const whiteButton = document.getElementById('white-bttn')

//Selecting the black button
const blackButton = document.getElementById('black-bttn')

//Selecting the print button
const printButton = document.getElementById('prnt-bttn')

let color

//Fetching a random color
setRandomColor()


whiteButton.addEventListener('click', () => {
    selectColor(1)
})

blackButton.addEventListener('click', () => {
    selectColor(0)//selectColor=chooseColor
})

printButton.addEventListener('click',print)

function selectColor(val){
    myData.push({
        input: color,
        output: [val]
    })
    setRandomColor()
}

function print(){
    console.log(JSON.stringify(myData))
}

function setRandomColor(){
    color = {
        rd = Math.random(),
        grn = Math.random(),
        bl = Math.random(),
    }
    
    //guessElem.style.color =  `rgba(${color.r * 255}, ${color.g * 255}, ${color.b * 255})`
    guessElem.style.color = guess > 0.5 ? '#FFF':'#000'
    
    colorElem.style.backgroundColor= 
        `rgba(${color.rd * 255}, ${color.grn * 255}, ${color.bl * 255})`
}
