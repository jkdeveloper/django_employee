console.log("inside my js")
$("#ajax").click(function () {
	console.log($(this).val())
    $.ajax({
        type: 'GET',
        url: '/employee_info/ajax_employee',
        data: {"message" :"bhupendra khatri"},
        dataType: 'json',
        success: function (data) {
            console.log("inside data",data)
            if (data.is_taken){
                console.log("insdie success")
                $('#ajax_info').text(data.is_taken);
            }
        }
    });
});


function get_all_options(){
    var opt = []
    $.each($("#browsers").find('option'),function(i,d){
        opt.push($(d).val())
    })
    if(opt.length){
        var match_opt = []
        $("[name='browser']").keyup(function(){
            for(var i = 0 ; i<opt.length ; i++){
                var pattern = ""+$(this).val()+".+"
                var re = new RegExp(pattern)
                if(opt[i].match(re) && opt[i].match(re)["input"] && match_opt.indexOf(opt[i].match(re)["input"]) == -1) {
                    match_opt.push(opt[i].match(re)["input"])
                }
            }
            $("#browsers").empty()
            var html = ""
            for(i=0;i<match_opt.length;i++){
                html += "<option value='"+match_opt[i]+"'>" 
            }
            console.log(html)
            $("#browsers").append(html)
            $('#browser').val("")
        })
        
    }  
}

//get_all_options()
$('#browser').change(function(){
    console.log("hiiiiiiiiii")
    search_name()
})


//variables for sorting
var $table = $("table");
var $tableBody = $table.find("tbody");
var rows, sortedRows, firstName, secondName, sortAscending;

//sort table 
function cmp(a, b) {
    firstName = $(a).find('td:first-child').text();
    secondName = $(b).find('td:first-child').text();
    if (firstName < secondName) { return (sortAscending) ? -1 : 1 }
    else if (firstName > secondName) { return (sortAscending) ? 1 : -1 }
    else { return 0 }
}

//common_click function
function common_click(button){
    rows = $tableBody.find("tr");
    if (button.attr('id') === 'asc') { sortAscending = true }
    else { sortAscending = false }
    sortedRows = rows.sort(cmp);
    $tableBody.remove('tr');
    $tableBody.append(sortedRows);
}

$('#asc').click(function(){
    common_click($(this));
})

$('#desc').click(function(){
    common_click($(this));
})

function search_name() {
    var input, filter, table, tr, td, i;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }       
    }
}