var reg = false;
$(document).ready(function() {
	$("#form2").hide();  

	$(document).keypress(function(e) {
		if(e.which == 13) {
			$("#form1").blur();
			if (reg == false) {
				var id = String($("#id-input").val());

				reg = true;
				
				$("#form1").hide();
				setTimeout(function() {
					$("#form2").show();
					//alert(id);
				}, 700); 
			}

		}

	});  



});




