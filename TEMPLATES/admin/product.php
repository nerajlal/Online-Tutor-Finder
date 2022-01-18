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
      <li><span><span><a href="user.php">User</a></span></span></li>
      <li><span><span><a href="order.php">Conform</a></span></span></li>
      <li class="active"><span><span>Action</span></span></li>
    </ul>
  </div>
  <div id="middle">
    <div id="center-column">
      <div class="top-bar"> <a href="#" class="button">ADD NEW </a>
        <h1>Contents</h1>
        <div class="breadcrumbs"><a href="#">action</a> / <a href="#">Contents</a></div>
        
      </div>
      <br />
      
      <div class="table"> <img src="img/bg-th-left.gif" width="8" height="7" alt="" class="left" /> <img src="img/bg-th-right.gif" width="7" height="7" alt="" class="right" />
      </div>
      <H1>After Contact Profile Update Form </H1>
      <form action="insertadd.php" method="post">
      <label for="fname">User id</label><br>
      <input type="number" id="tid" name="tid"><br>
      <label for="fname">User address</label><br>
      <input type="text" id="address" name="address"><br>
      <input type="submit" value="Submit">
      <br>
      <br>
      </form> 
      <H1>Remove User</H1>
      <form action="remove.php" method="post">
      <label for="fname">User id</label><br>
      <input type="number" id="id" name="id"><br>
      <input type="submit" value="Submit">
      </form>
  </div>
  <div id="footer"></div>
</div>
</body>
</html>