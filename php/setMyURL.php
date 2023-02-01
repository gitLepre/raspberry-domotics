<?php

require_once('dbconnect.php');

// Questa pagina inserisce un nuovo Raspberry nel database con il relativo URL, e se già presente lo aggiorna

$id_rasp = $_POST['id_rasp'];
$public_url = $_POST['url'];

$stmt = $conn->prepare("SELECT * FROM raspberry WHERE id_rasp = ?");
$stmt->bind_param("s", $id_rasp);
$stmt->execute();

$result = $stmt->get_result();
$row = $result->fetch_array(MYSQLI_ASSOC);

if($result->num_rows != 0)
{
    $stmt_update = $conn->prepare("UPDATE raspberry SET url = ? WHERE id_rasp = ?");
    $stmt_update->bind_param("ss", $public_url, $id_rasp);
    $stmt_update->execute();
    $stmt_update->close();
    echo 'id_raspberry e/o url aggiornati';
}

else {
    $stmt_insert = $conn->prepare("INSERT INTO raspberry (url, id_rasp) VALUES (?, ?)");
    $stmt_insert->bind_param("ss", $public_url, $id_rasp);
    $stmt_insert->execute();
    $stmt_insert->close();
    echo 'id_raspberry e url inseriti';
}

?>
