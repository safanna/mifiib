<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/v/dt/dt-1.11.5/datatables.min.css" />
<title>This is Anna Safonova HomeWork:)</title>
</head>
<body>
<h1>This is Anna Safonova HomeWork:)</h1>
<h3>My Pets</h3>
<?php
echo '<table id="tbl">';
echo '<thead><th>pet_id</th><th>name</th><th>type</th><th>sex</th><th>age</th></thead>';
$num_pets = 0;
$conn = mysqli_connect('database', 'root', 'secret', 'mypets');
$query = 'SELECT * FROM my_pets';
$result = mysqli_query($conn, $query);
while ($value = $result->fetch_array(MYSQLI_ASSOC)){
echo '<tr>';
foreach($value as $element){
echo '<td>'.$element.'</td>';
}
echo '</tr>';
$num_pets += 1;
}
$result->close();
mysqli_close($conn);
echo '</table>';
if ($num_pets>3){
echo '<h5>Looks like i think about dog...</h5>';
}
phpinfo();
?>
</body>
</html>
