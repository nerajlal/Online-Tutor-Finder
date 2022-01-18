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
$id = $_POST["tid"];
$address = $_POST["address"];
$sql = "UPDATE `user` SET `address` = '$address' WHERE `user`.`id` = '$id'";
if ($conn->query($sql) === TRUE) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>