<?php
 include ( "../inc/connection.inc.php" );

ob_start();
session_start();
if (!isset($_SESSION['user_login'])) {
	$user = "";
	$utype_db = "";
}
else {
	$user = $_SESSION['user_login'];
	$result = $con->query("SELECT * FROM user WHERE id='$user'");
		$get_user_name = $result->fetch_assoc();
			$uname_db = $get_user_name['fullname'];
			$utype_db = $get_user_name['type'];
}
?>


<?php

        $applied_by_id = mysqli_real_escape_string($con, $_REQUEST['app_tut']);

echo $applied_by_id." ";
         
         $resul = $con->query("SELECT * FROM user WHERE id='$applied_by_id'");
         $get_name = $resul->fetch_assoc();
         $reciver_name = $get_name['fullname'];
         echo $reciver_name;
         $con->query("UPDATE user SET chatting = '$reciver_name' WHERE id =$user");
         header('Location: index2.php');
         ?>