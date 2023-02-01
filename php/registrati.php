<?php

require_once('dbconnect.php');

$user = $_POST['username'];
$pwd = $_POST['password'];
$idRasp = $_POST['id_rasp'];

$stmt = $conn->prepare("SELECT username FROM utenti WHERE username = ? ");
$stmt->bind_param("s", $user);
$stmt->execute();
$result = $stmt->get_result();


$stmt = $conn->prepare("SELECT id_rasp FROM utenti WHERE id_rasp = ? ");
$stmt->bind_param("s", $idRasp);
$stmt->execute();
$result_2 = $stmt->get_result();


if ($result->num_rows != 0 && $result_2->num_rows == 0) {
	http_response_code(401);
}

else if ($result->num_rows == 0 && $result_2->num_rows != 0) {
	http_response_code(409);
}

else if ($result->num_rows != 0 && $result_2->num_rows != 0) {
	http_response_code(406);
}

else if ($result->num_rows == 0 && $result_2->num_rows == 0) {
	$row = $result->fetch_array(MYSQLI_ASSOC);
	$passSha = sha1($pwd);
	$stmt = $conn->prepare("INSERT INTO utenti (username, password, id_rasp) values (?, ?, ?)");
	$stmt->bind_param("sss", $user, $passSha, $idRasp);
    $stmt->execute();
    http_response_code(201);
}

?>