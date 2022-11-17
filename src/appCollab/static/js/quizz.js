/* Response is checked 
    return list: name of input checked
*/
function isChecked(){
    let checkedBox = []; 
    const inputElements = document.getElementsByClassName('reponse');
    for(var i=0; inputElements[i]; ++i){
        if(inputElements[i].checked){
            checkedBox.push(i);
        }
    }
    return checkedBox
}

/* Send data to the view after clicking the Submit button
    return json
*/
const form = document.getElementById('myForm')
form.addEventListener('submit', sendData);
function sendData(event){
    event.preventDefault();
    const csrf  = $('input[name="csrfmiddlewaretoken"]').val()   // collect token
    const respUser = isChecked()
    // ------------------- Send data to view -------------------
    $.ajax({
        type: "POST",
        url: 'nextQuestion', // Name of the django view that will retrieve the data
        data: {
            csrfmiddlewaretoken : csrf,
            "result": respUser,       // data to send
        },
        dataType: "json",
        // ------------------- Receiving data from the view -------------------
        success: function (data) { // if send successful 
            // Update variables with the new data received
            timerQuestion = data["data"]["duree"]
            titre         = data["data"]["titre"]
            intitule      = data["data"]["intitule"]
            listRep       = data["data"]["reponses"]
            updateTag()  // Updates fields with the update variables
            onTimesUp()  // Stop the setInterval method
            initTimer()  // Resets the variables concerning the countdown 
            startTimer() // Start the countdown
        },
        failure: function () {
            alert("failure");
        }
    })
}

/* Add data in tag
*/
const containerRep  = document.getElementById("container-reponses");
function updateTag(){
    document.getElementById("titre").textContent    = titre    // title
    document.getElementById("intitule").textContent = intitule // entitled
    // Responses
    containerRep.innerHTML = "";
    const tagsRep = document.createElement("div");
    for (let r = 0; r < listRep.length; r++) {
        tagsRep.innerHTML  += `<input name=${r} type="checkbox" class="reponse">
                               <label for=${r}> ${listRep[r]} </label> `;
      } 
      containerRep.appendChild(tagsRep);

} 

window.onload = function() {
    updateTag()
  };
  