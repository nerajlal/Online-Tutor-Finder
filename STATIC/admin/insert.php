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
      $id = $_POST['id'];
      $sql = "INSERT INTO service_tbl (id)
      VALUES ('$id')";
      
      if ($conn->query($sql) === TRUE) {
      echo "New record created successfully";
      } else {
      echo "Error: " . $sql . "<br>" . $conn->error;
      }
      
      $conn->close();
      ?>