<?php
require_once('dbconnect.php');
// Questa pagina inserisce un nuovo set di porte nel database prese dalla configurazione

$user = $_POST['username'];
$porta1 = $_POST['porta1'];
$porta2 = $_POST['porta2'];
$porta3 = $_POST['porta3'];
$porta4 = $_POST['porta4'];
$porta5 = $_POST['porta5'];
$porta6 = $_POST['porta6'];
$porta7 = $_POST['porta7'];
$porta8 = $_POST['porta8'];

$stmt = $conn->prepare("SELECT * FROM porte WHERE username = ?");
$stmt->bind_param("s", $user);
$stmt->execute();
$result = $stmt->get_result();
$row = $result->fetch_array(MYSQLI_ASSOC);
if($result->num_rows != 0)
{
    $stmt_update = $conn->prepare("UPDATE porte SET porta1 = ?, porta2 = ?, porta3 = ?, porta4 = ?, porta5 = ?, porta6 = ?, porta7 = ?, porta8 = ? WHERE username = ?");
    $stmt_update->bind_param("sssssssss", $porta1, $porta2, $porta3, $porta4, $porta5, $porta6, $porta7, $porta8, $user);
    $stmt_update->execute();
    $stmt_update->close();
    echo 'porte aggiornate';
}
else{
    $stmt_insert = $conn->prepare("INSERT INTO porte (username, porta1, porta2, porta3, porta4, porta5, porta6, porta7, porta8) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)");
    $stmt_insert->bind_param("sssssssss", $user, $porta1, $porta2, $porta3, $porta4, $porta5, $porta6, $porta7, $porta8);
    $stmt_insert->execute();
    $stmt_insert->close();
    echo 'porte inserite';
}

?>