function update(){
    let text=document.getElementById("text-maker");
    let prompt=document.getElementById("prompt");
    if(text.value.length>1){
        prompt.innerText=text.value[0].toUpperCase()+text.value.slice(1,-1)+text.value[text.value.length-1].toUpperCase();
    }
    else if(text.value.length==1){
        prompt.innerText=text.value.toUpperCase();
    }
    else{
        prompt.innerText=""
    }
}