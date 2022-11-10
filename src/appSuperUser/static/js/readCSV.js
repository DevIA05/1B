const csvFile = document.getElementById('csvFile')
const form = document.getElementById('myForm')

$(document).ready( function () {
    $('#example').DataTable();
} );

// Extract data from csv 
csvFile.addEventListener('change', (e) => {
    Papa.parse(csvFile.files[0], {
        download: true,
        encoding: "ISO-8859-1",
        header: false,
        skipEmptyLines: true,
        complete: function(results){
            fillHtmlTable(results.data)
        }
    })
})

// Fill table with data
function fillHtmlTable(res){
    const t = $('#example').DataTable();
    emptyTable(t) 
    for (let i = 1; i < res.length; i++) { 
        t.row.add([res[i][7], res[i][6], res[i][5]]).draw(false);
  }
}

// Empty the table
function emptyTable(table){
    table
    .clear()
    .draw();
}

// Get Data from html table
function getDataFromTable(){
    const res = $('#example').DataTable().rows().data();
    let dict = {};
    for (let e = 0; e < res.length; e++) {
        dict[e] = {"prenom": res[e][0], "nom": res[e][1], "matricule": res[e][2]}
    }
    return dict
}

function sendData(event){
    event.preventDefault();
    console.log("Hello")
    const res = getDataFromTable()
    $.ajax({
        type: "POST",
        url: 'addDataInDB',
        // headers: {
        //     'X-CSRFToken': $.cookie("csrftoken")
        // },
        data: {
            csrfmiddlewaretoken: '{{ csrf_token }}',
            "result": res,
        },
        dataType: "json",
        success: function (data) {
            // any process in data
            alert("successfull")
        },
        failure: function () {
            alert("failure");
        }
    })
}

form.addEventListener('submit', sendData);
  