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

/* Add Leading Zeros
- num(int)        : value where zeros will be added
- totalLength(int): number of zeros that will be added
return str        : value with totalLength zeros added  
*/
function addLeadingZeros(num, totalLength) {
    return String(num).padStart(totalLength, '0');
}

/* Send data to the view after clicking the Submit button
*/
const form = document.getElementById('myForm')

form.addEventListener('submit', sendData);
function sendData(event){
        event.preventDefault();
        form.disabled = true; // Prevents information from being out of synchronization with the server
                              //   by disabling the button so that the user is not the way to spam it.
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
                numQuestion   = data["data"]["numQuestion"]
                updateTag()  // Updates fields with the update variables
                onTimesUp()  // Stop the setInterval method
                initTimer()  // Resets the variables concerning the countdown 
                startTimer() // Start the countdown
                form.disabled = false;
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
    document.getElementById("titre").textContent    = addLeadingZeros(numQuestion+1, 2) + "/" + totalQ + " - " + titre; // title
    document.getElementById("intitule").textContent = intitule                                                          // entitled
    // Responses
    containerRep.innerHTML = ""; // empty the div of its children to add the new answers whose number of answers can be more 
                                 //   or less than the answers of the previous question
    const tagsRep = document.createElement("div");
    for (let r = 0; r < listRep.length; r++) {
        tagsRep.innerHTML  += `<input name=${r+1} type="checkbox" class="reponse">
                               <label for=${r+1}> ${listRep[r]} </label> `;
      } 
      containerRep.appendChild(tagsRep);

} 

window.onload = function() {
    updateTag()
  };
  