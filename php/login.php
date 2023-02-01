<?php

require_once('dbconnect.php');

$user = $_POST['username'];
$pwd = $_POST['password'];
$passSha = sha1($pwd);

$stmt = $conn->prepare("SELECT username FROM utenti WHERE username = ? AND password = ?");
$stmt->bind_param("ss", $user, $passSha);
$stmt->execute();
$result = $stmt->get_result();

if ($result->num_rows == 0) {
	http_response_code(401);
}

else if($result->num_rows != 0) {
    http_response_code(200);
}

?>