import React, { useState } from "react";

function SortingVisualizer(){

const [array,setArray] = useState([])
const [speed,setSpeed] = useState(100)
const [inputArray,setInputArray] = useState("")

function generateArray(){

let arr = []

for(let i=0;i<25;i++){
arr.push(Math.floor(Math.random()*100)+10)
}

setArray(arr)

}

function handleInput(){

let arr = inputArray.split(",").map(Number)

setArray(arr)

}

function sleep(ms){
return new Promise(resolve => setTimeout(resolve,ms))
}

async function bubbleSort(){

let arr = [...array]

for(let i=0;i<arr.length;i++){

for(let j=0;j<arr.length-i-1;j++){

let bars = document.getElementsByClassName("bar")

bars[j].style.backgroundColor = "red"
bars[j+1].style.backgroundColor = "red"

await sleep(speed)

if(arr[j] > arr[j+1]){

let temp = arr[j]
arr[j] = arr[j+1]
arr[j+1] = temp

setArray([...arr])

}

bars[j].style.backgroundColor = "cyan"
bars[j+1].style.backgroundColor = "cyan"

}

let bars = document.getElementsByClassName("bar")
bars[arr.length-i-1].style.backgroundColor = "green"

}

}

return(

<div>

<div style={{marginBottom:20}}>

<button onClick={generateArray}>
Generate Random Array
</button>

<button onClick={bubbleSort}>
Bubble Sort
</button>

<label style={{marginLeft:20}}>
Speed
</label>

<input
type="range"
min="10"
max="500"
value={speed}
onChange={(e)=>setSpeed(e.target.value)}
/>

</div>

<div style={{marginBottom:20}}>

<input
type="text"
placeholder="Enter numbers like 5,3,8,1"
value={inputArray}
onChange={(e)=>setInputArray(e.target.value)}
style={{width:"300px",marginRight:"10px"}}
/>

<button onClick={handleInput}>
Set Array
</button>

</div>

<div style={{
display:"flex",
justifyContent:"center",
alignItems:"flex-end",
height:"400px"
}}>

{array.map((value,index)=>(
<div
className="bar"
key={index}
style={{
backgroundColor:"cyan",
height:value*3,
width:"20px",
margin:"0 2px"
}}
></div>
))}

</div>

</div>

)

}

export default SortingVisualizer