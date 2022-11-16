const form = document.getElementById('myForm')

/* Response is checked 
    return list: name of input checked
*/
function isChecked(){
    let checkedBox = []; 
    const inputElements = document.getElementsByClassName('reponse');
    for(var i=0; inputElements[i]; ++i){
        if(inputElements[i].checked){
            // checkedBox.push(inputElements[i].name);
            checkedBox.push(i);
        }
    }
    return checkedBox
}

/* Send data to the view after clicking the Submit button
    return json
*/
form.addEventListener('submit', sendData);
function sendData(event){
    event.preventDefault();
    console.log("sendData")
    const csrf  = $('input[name="csrfmiddlewaretoken"]').val()   // Mise en place du jeton csrf
    $.ajax({
        type: "POST",
        url: 'nextQuestion', // Nom de la vue de django 
        data: {
            csrfmiddlewaretoken : csrf,
            // Les données à envoyer sous forme de dictionnaire
            "result": isChecked()
        },
        dataType: "json",
        success: function (data) {
            alert("successfull")
            // departMinutes = 
            // titre         = 
            // intitule      = 
            // listRep       = 
            // updateTag()
        },
        failure: function () {
            alert("failure");
        }
    })
}