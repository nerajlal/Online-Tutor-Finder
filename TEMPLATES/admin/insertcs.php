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
      $income = $_POST['income'];
      $expense = $_POST['expense'];
      $sql = "UPDATE `service_tbl` SET `income` = '$income', `expense` = '$expense', `status` = 'yes'   WHERE `service_tbl`.`id` ='$id'";
      
      if ($conn->query($sql) === TRUE) {
      echo "Updated successfully";
      } else {
      echo "Error: " . $sql . "<br>" . $conn->error;
      }
      
      $conn->close();
      header("Location: collectororder.php");
      ?>