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
     $id = $_POST['id'];
     $sql = "DELETE FROM user WHERE id='$id'";
     
     if ($conn->query($sql) === TRUE) {
     echo "record deleted successfully";
     } else {
     echo "Error: " . $sql . "<br>" . $conn->error;
     }
     
     $conn->close();
     ?>