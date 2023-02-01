<?php

require_once('dbconnect.php');

$user = "pime";
$pwd = "ciaociao";

//$user = $_POST['username'];
//$pwd = $_POST['password'];

$stmt = $conn->prepare("SELECT username FROM utenti WHERE username = ? AND password = ?");
$stmt->bind_param("ss", $user, $pwd);
$stmt->execute();
$result = $stmt->get_result();

if ($result->num_rows != 0) {
	$row = $result->fetch_array(MYSQLI_ASSOC);
	$concat = $row['username'] . time();
	$token = sha1($concat);
	$expireDate = date("Y-m-d h:i:sa", time() + (8 * 60 * 60));
	$stmt = $conn->prepare("INSERT INTO token (username, token, expireDate) values (?, ?, ?)");
	$stmt->bind_param("sss", $user, $token, $expireDate);
	$stmt->execute();
	echo $token;
}
else echo "Dati inseriti sbagliati";

?>