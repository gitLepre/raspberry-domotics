<?php

require_once('dbconnect.php');

// Questa pagina stampa la lista di tutti i Raspberry presenti nel Database

// Modificare la query per stampare solo quelli non ancora assegnati a nessun utente ?
//   (not in ( select id_raspberry from utenti where ...)) 

$stmt = $conn->prepare("SELECT * FROM raspberry order by date");
$stmt->execute();

echo '
<html>
  <head>
  <title>Raspberry List</title>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
  </head>
  <body>';


$result = $stmt->get_result();
if ($result->num_rows != 0) {
	$cont = 1;
	echo'<div class="container"><h1>Unassigned Raspberry List</h1><br><table class="table">
  		<thead>
    		<tr>
      		<th scope="col">&#35;</th>
      		<th scope="col">ID Raspberry</th>
      		<th scope="col">URL</th>
      		<th scope="col">Data</th>
    		</tr> 
  		</thead>

  		<tbody>';

    while($row = $result->fetch_array(MYSQLI_ASSOC)) {
    	echo "<tr>";
    	echo "<td>" . $cont . "</td>";
        echo "<td>" . $row['id_rasp'] . "</td>";
        echo "<td>" . $row['url'] . "</td>";
        echo "<td>" . $row['date'] . "</td>";
        echo "</tr>";
        $cont +=1;
    }
    echo'</tbody></table></div>';
}
else {
    echo '<h2 style="padding:10px;margin-top:10px;"><center>Non sono attualmente presenti raspberry nel database</center></h2>';
}

echo'
  </body>
</html>';

?>