<?php
	include("connect.php");

	if(isset($_POST['email']) && $_POST['usr_name']) { //Kollar ifall det finns en post som heter fname och lname.
		//Tillgängliga poster [fname, lname, email, username och password}	
		// Check connection
		if ($conn->connect_error) { //Om anslutningen inte är sönder!
		   die("Connection failed: " . $conn->connect_error); //Post variabler innehåller ingenting. 
		} 
		else {

			$sql = "INSERT INTO  players (name, nickname, id, email, score) VALUES ('" . $_POST['first_name'] . " " . $_POST['last_name'] .
                "', '" . $_POST['usr_name'] . "', '" . $_POST['id'] . "', '" . $_POST['email'] . "', '" . "0" . "')";

			if ($conn->query($sql) === TRUE) {
				//echo "Användaren skapad!";
				//echo "<a href='" . "http://link.example.com" . "'>Tryck för att gå tillbaka!</a>";
				header('Location: http://193.11.184.62:5000');	

			} else {
				echo "Kan inte skapa användaren!";
				echo "Error: " . $sql . "<br>" . $conn->error;
				//echo "<a href='" . "http://link.example.com" . "'>Tryck för att försöka igen!</a>";
		     }

		}
	}
	else {
		echo "Email och username not set!";
	}

	$conn->close();

	?>
