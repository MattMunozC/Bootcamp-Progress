//JS puro

function add(){
    const list=document.getElementById("list");//featch list from DOM
    let li=document.createElement("li") //create a new li element
    let input=document.getElementById("new_element"); //fetch new_element from DOM
    li.setAttribute("id",input.value)
    li.setAttribute("onClick","removeFromList(this.id)")
    if(input.value!=""){
        li.innerText=input.value; //insert the value of input into li
        input.value="";//clean the value of new_element
        list.appendChild(li) //append li to list
    }
}
function removeFromList(id){
    const list=document.getElementById("list");//featch list from DOM
    list.removeChild(document.getElementById(id))
}

//JQUERY
function addJQ(){
    const list=$("#listJQ")
    let input=$("#new_elementJQ")
    let li=$("<li>")
    li.text(input.val())
    li.attr({
        "id":input.val(),
        "onClick":"removeFromListJQ(this.id)"
    })
    if(input.val()!=""){
        list.append(li)
        $("#new_elementJQ").val("")
    }
    
}
function removeFromListJQ(id){
    $(`#${id}`).remove()
}