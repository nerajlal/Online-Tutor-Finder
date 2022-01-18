<?php
   include('session.php');
?>
<html>
<head>
<title>Admin</title>
<style media="all" type="text/css">
@import "css/all.css";
</style>
</head>
<body>
<div id="main">
  <div id="header"> <a href="#" class="logo"><img src="img/logo.gif" width="101" height="29" alt="" /></a>
    <ul id="top-navigation">
    <li><span><span><a href="index.php">Home</a></span></span></li>
      <li class="active"><span><span>Users</span></span></li>
      <li><span><span><a href="order.php">Conform</a></span></span></li>
      <li><span><span><a href="product.php">Action</a></span></span></li>
    </ul>
  </div>
  <div id="middle">
    <div id="center-column">
      <div class="top-bar"> 
        <h1>Contents</h1>
        <div class="breadcrumbs"><a href="#">User</a> / <a href="#">Contents</a></div>
      </div>
      <br />
      <div class="table"> <img src="img/bg-th-left.gif" width="8" height="7" alt="" class="left" /> <img src="img/bg-th-right.gif" width="7" height="7" alt="" class="right" />
      </div>

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
   $sql = "SELECT id, fullname, address, phone  FROM user";
   $result = $conn->query($sql);
   if ($result->num_rows > 0) {
   // output data of each row
   while($row = $result->fetch_assoc()) {
   echo "id: " . $row["id"]. "  //Name//  " . $row["fullname"]. "  //Address//  " . $row["address"]. "  //phone//  " . $row["phone"]. "<br>"; }
   } else {
   echo "0 results";
   } 
    ?>
  </div>
  <div id="footer"></div>
</div>
</body>
</html>