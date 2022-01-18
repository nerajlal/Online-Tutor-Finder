<?php
   $servername = "localhost";
   $username = "root";
   $password = "";
   $dbname = "main_db";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
$t_id = $_POST["t_id"];
$inst_name = $_POST["inst_name"];
$prefer_sub = $_POST["prefer_sub"];
$class = $_POST["class"];
$medium = $_POST["medium"];
$prefer_location = $_POST["prefer_location"];
$salary = $_POST["salary"];
$sql = "INSERT INTO tutor (t_id, inst_name , prefer_sub, class, medium, prefer_location, salary)
VALUES ('$t_id', '$inst_name', '$prefer_sub', '$class', '$medium', '$prefer_location', '$salary')";
if ($conn->query($sql) === TRUE) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>