<?php
require_once('dbconnect.php');
// Questa pagina restituisce il set di porte di un utente
$user = $_POST['username'];

$stmt = $conn->prepare("SELECT * FROM porte WHERE username = ?");
$stmt->bind_param("s", $user);
$stmt->execute();
$result = $stmt->get_result();
$row = $result->fetch_array(MYSQLI_ASSOC);

$response = array('username' => $user, 'porta1' => $row['porta1'], 'porta2' => $row['porta2'],
     'porta3' => $row['porta3'], 'porta4' => $row['porta4'], 'porta5' => $row['porta5'], 
     'porta6' => $row['porta6'], 'porta7' => $row['porta7'], 'porta8' => $row['porta8']);
$responseJson = json_encode($response);

echo $responseJson;

?>