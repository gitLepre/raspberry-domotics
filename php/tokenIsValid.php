<?php

require_once('dbconnect.php');

// Ritorna un file JSON contenente un codice che stabilisce la validità del token

$token = $_POST['token'];

//query che prende la scadenza del token e l'url da mandare all'app se il token è valido
$stmt = $conn->prepare("SELECT token.expireDate, raspberry.url FROM token, utenti, raspberry 
	WHERE token.token = ? AND token.username = utenti.username AND utenti.id_rasp = raspberry.id_rasp");
$stmt->bind_param("s", $token);
$stmt->execute();
$result = $stmt->get_result();

if ($result->num_rows != 0) {
	$row = $result->fetch_array(MYSQLI_ASSOC);
	$isExpired = (strtotime($row['expireDate'])) - time();
	if($isExpired > 0){
		
		$response = '{"code": "0", "url": "'.$row['url'].'"}'; //non è scaduto
	}
	else{
		$response = '{"code": "1", "url": ""}'; //è scaduto
	}
} else {
		
		$response = '{"code": "2", "url": ""}'; //non esiste
}

$responseJson = json_encode($response);

echo $responseJson;

?>