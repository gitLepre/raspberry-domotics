<?php

// Pagina di connessione al database

$mysql_server = "localhost";
$mysql_user = "S4254186";
$mysql_pass = "formaggio18";
$mysql_db = "S4254186";
 
$conn = new mysqli($mysql_server, $mysql_user, $mysql_pass, $mysql_db);
 
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
 
?>
