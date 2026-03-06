import React, { useEffect, useState } from "react";
import { Line } from "react-chartjs-2";
import {
Chart as ChartJS,
LineElement,
CategoryScale,
LinearScale,
PointElement,
Title,
Tooltip,
Legend
} from "chart.js";

ChartJS.register(LineElement, CategoryScale, LinearScale, PointElement, Title, Tooltip, Legend);

function App() {

const [labels,setLabels] = useState(["09:00"]);
const [values,setValues] = useState([30]);
const [prediction,setPrediction] = useState("");

function generateFakeLoad(){

const hour = new Date().getHours();
let base = 40;

if(hour >= 12 && hour <= 14){
base = 150; // lunch surge
}

if(hour > 14 && hour <= 17){
base = 90;
}

if(hour > 17){
base = 60;
}

return base + Math.floor(Math.random()*20);
}

useEffect(()=>{

const interval = setInterval(()=>{

const newTime = new Date().toLocaleTimeString();

const load = generateFakeLoad();

setLabels(prev => [...prev,newTime]);

setValues(prev => {

const newData = [...prev,load];

if(load > 140){
setPrediction("Lunch Hour Surge Detected");
}

return newData;

});

},2000);

return () => clearInterval(interval);

},[]);

const data = {
labels:labels,
datasets:[
{
label:"Predicted Cafeteria Load",
data:values,
borderColor:"blue",
backgroundColor:"rgba(0,0,255,0.2)",
tension:0.4
}
]
};

const options = {
responsive:true,
plugins:{
legend:{position:"top"}
},
scales:{
y:{
min:0,
max:200,
title:{display:true,text:"Students"}
},
x:{
title:{display:true,text:"Time"}
}
}
};

return(

<div style={{width:"900px",margin:"auto",marginTop:"40px"}}>

<h1>Cafeteria Load Prediction Dashboard</h1>

<Line data={data} options={options}/>

<h2 style={{color:"red"}}>{prediction}</h2>

</div>

);
}

export default App;
