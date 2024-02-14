const green_on="background-color: green;border-radius: 100%; margin: 10%;box-shadow: 0px 0px 10px 5px green;"
const red_on="background-color: red; border-radius: 100%; margin: 10%; box-shadow: 0px 0px 10px 5px red;"
const yellow_on="background-color: yellow;border-radius: 100%; margin: 10%; box-shadow: 0px 0px 10px 5px yellow;"
const green_off="background-color: rgb(0, 46, 0);border-radius: 100%; margin: 10%;"
const yellow_off="background-color: rgb(95, 95, 0);border-radius: 100%; margin: 10%"
const red_off="background-color: rgb(112, 0, 0); border-radius: 100%; margin: 10%;"
const green=document.getElementById("green")
const red=document.getElementById("red")
const yellow=document.getElementById("yellow")
const box=document.getElementById("box")
const semaforo=document.getElementById("Semaforo")
function yellowOn(pos){
    setTimeout(()=>{
            red.style=red_off
            green.style=green_off;
            yellow.style=yellow_on;
    },3000)
}
function greenOn(){
    setTimeout(()=>{
        yellow.style=yellow_off;
        red.style=red_off;
        green.style=green_on;
    },0)
}
function redOn(){
    setTimeout(()=>{
        green.style=green_off
        yellow.style=yellow_off;
        red.style=red_on;
    },4000)
}
var isFar=true;
var intervalID=setInterval(()=>{
    //not the optimal solution, having an if statement repeat itself three times is a no-no but i need to know if it is in the range
    //where the interval can happens so it's stop properly. it looks hideous and there must be a cleaner way to do this but 
    //it's functional and that's what's matter here
    if(isFar){
        greenOn()
    }
    if(isFar){
        yellowOn()
    }
    if(isFar){
        redOn()
    }
},7000)
box.addEventListener("mousemove",(event)=>{
    let leftDistance=semaforo.offsetLeft-event.clientX;
    let rightDistance=event.clientX-(semaforo.offsetLeft+100);
    let topDistance=semaforo.offsetTop-event.clientY;
    let bottomDistance=event.clientY-(semaforo.offsetTop+200);
    if((leftDistance>200 && leftDistance>0) || (rightDistance>200 && rightDistance>0)){
        isFar=true;
    }else if ((leftDistance<200 && leftDistance>150) || (rightDistance<200 && rightDistance>150)){
        green.style=green_off;
        red.style=red_off;
        yellow.style=yellow_on;
        isFar=false
    }else if((leftDistance<150 && leftDistance>0) || (rightDistance<150 && rightDistance>0)){
        green.style=green_off;
        red.style=red_on;
        yellow.style=yellow_off;
        isFar=false;
    }
})