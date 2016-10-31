<!DOCTYPE html>
<html lang="sv">
<meta charset="UTF-8">
<head>


<!--BOOTSTRAP-->
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>

<!-- Latest compiled JavaScript -->
<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
<!--BOOTSTRAP-->


	<link rel="stylesheet" href="css/style_pingponghack.css" type="text/css" />

</head>
<body>

<?php
$kod = $_GET["id"];

?>

<div class="container">
        <div class="row centered-form">
        <div class="col-xs-12 col-sm-8 col-md-4 col-sm-offset-2 col-md-offset-4">
        	<div class="panel panel-default">
        		<div class="panel-heading">
			    		<h3 class="panel-title">Registrera en ny användare för att börja spela PingPong!</h3>
			 			</div>
			 			<div class="panel-body">
			    		<form role="form" method="post" action="/pingponghack_register.php">
			    			<div class="row">
			    				<div class="col-xs-6 col-sm-6 col-md-6">
			    					<div class="form-group">

			                <input type="text" name="first_name" id="first_name" class="form-control input-sm" placeholder="Förnamn">

			    					</div>
			    				</div>
			    				<div class="col-xs-6 col-sm-6 col-md-6">
			    					<div class="form-group">

			    						<input type="text" name="last_name" id="last_name" class="form-control input-sm" placeholder="Efternamn">

			    					</div>
			    				</div>
			    			</div>

			    			<div class="form-group">
							<input type="hidden" name="id" value="<?php echo $kod;?>">
		    				<input type="text" name="usr_name" id="usr" class="form-control input-sm" placeholder="Användarnamn">

			    			</div>

			    			<div class="form-group">

			    				<input type="email" name="email" id="email" class="form-control input-sm" placeholder="Email">

			    			</div>

			    			<div class="row">
			    				<div class="col-xs-6 col-sm-6 col-md-6">
			    					<div class="form-group">

			    						<input type="password" name="password" id="password" class="form-control input-sm" placeholder="Lösenord">

			    					</div>
			    				</div>
			    				<div class="col-xs-6 col-sm-6 col-md-6">
			    					<div class="form-group">

			    						<input type="password" name="password_confirmation" id="password_confirmation" class="form-control input-sm" placeholder="Bekräfta lösenord">

			    					</div>
			    				</div>
			    			</div>
			    			
			    			<input type="submit" value="Registrera" class="btn btn-info btn-block">
			    		</body>
			    		</form>
			    	</div>
	    		</div>
    		</div>
    	</div>
    </div>
		