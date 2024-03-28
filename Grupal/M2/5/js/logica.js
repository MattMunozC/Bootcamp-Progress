function login(){
    let user=document.getElementById("user")
    let password=document.getElementById("password")
    let msgboard=document.getElementById("messages")
    let messages=document.createElement("div")
    messages.innerHTML="<div class='msg-value'></div><span onclick='msg_close(this)'>X</span>";
    messages.classList.add("msg")
    if(user.value==password.value && user.value){
        messages.classList.add("login")
        messages.firstChild.innerText="Contraseña Correcta"
        setTimeout(()=>{window.location="/home/index.html"},1000)
        msgboard.appendChild(messages)
        
    }else{
        messages.classList.add("error")
        messages.firstChild.innerText="Contraseña Incorrecta"
        msgboard.appendChild(messages)
    }
}
function msg_close(element){
    let msgboard=document.getElementById("messages")
    msgboard.removeChild(element.parentElement)
    console.log(element.parentElement)
}
function plus(element){
    let input=element.parentElement.children[1]
    input.value=parseInt(input.value)+1
}

function minus(element){
    let input=element.parentElement.children[1]
    if (parseInt(input.value)>0){
        input.value=parseInt(input.value)-1
    }
    
}

function comprar(element){
    let smartphone=element.parentElement.parentElement.parentElement 
    let counter=document.getElementById("shopping-counter")
    let table_content=document.getElementById("shopping-table").lastElementChild
    let new_product=document.createElement("tr")
    let name=smartphone.children[0].innerText
    let price=smartphone.children[2].innerText.split("$")[1]
    let cantidad=element.parentElement.children[1].value
    new_product.innerHTML+=`<td>${name}</td>
    <td>${cantidad}</td>
    <td>${parseInt(price)*parseInt(cantidad)}</td>`

    table_content.appendChild(new_product)
    counter.innerText=parseInt(counter.innerText)+1
}

function redirigir(){
    setTimeout(()=>{
        window.location="../home/index.html"
    },5000)
}