var reg = false;
$(document).ready(function() {
    $("#form2").hide();  
    $("#gameDiv").hide();
    
    //$("#gameDiv").show();
    //$("body").css('background', '-webkit-linear-gradient(left, rgba(150,0,0,1) 50%,rgba(0,0,150,1) 50%,rgba(0,0,150,1) 55%)');
    //$("#player1set1").css('background-color', 'white');
    function showIDWindow(){
        $("#gameDiv").hide();
        $("#form2").hide();
        $("#form1").show();
    }

    $(document).keypress(function(e) {
        if(e.which == 13) {
            $("#form1").blur();
            if (reg == false) {
                var id = String($("#id-input").val());
                $("#form1").hide();
                reg = true;

                /*$.ajax({
                   url: 'AirtimeCalculator.php',
                   success: function (response) {
                       var commaCheck = response.includes(",");
                       
                           
                       }
                       
                });*/
                /*
                $.ajax({
                    url: 'GetCard.php',
                    type: 'POST',
                    data: $(String($("#id-input").val())).serialize(), // it will serialize the form data
                        dataType: 'html'
                    })
                    .done(function(data){
                        alert(data);
                        //$("#id").text(data);
                    })
                    .fail(function(){
                    alert('Ajax Submit Failed ...');    
                    });
                */
                
                setTimeout(function() {
                    $("#form2").show();
                    //alert(id);
                }, 700); 
            }

        }

    });  

});
