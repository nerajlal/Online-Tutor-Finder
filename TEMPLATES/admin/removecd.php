<?php
     $servername = "localhost";
     $username = "root";
     $password = "";
     $dbname = "user-registration";
     
     // Create connection
     $conn = new mysqli($servername, $username, $password, $dbname);
     // Check connection
     if ($conn->connect_error) {
     die("Connection failed: " . $conn->connect_error);
     }
     $pid = $_POST['id'];
     $sql = "DELETE FROM service_tbl WHERE id='$pid'";
     
     if ($conn->query($sql) === TRUE) {
     echo "record deleted successfully";
     } else {
     echo "Error: " . $sql . "<br>" . $conn->error;
     }
     
     $conn->close();
     ?>
     <?php  
     header("Location: collectororder.php");
     ?>