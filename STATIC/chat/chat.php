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
			$sender = $get_user_name['fullname'];
			$reciver = $get_user_name['chatting'];
}
?>

<?php
	include 'connection.php';
	$query = "SELECT * FROM chat WHERE name = '$sender' AND receiver = '$reciver' OR (name = '$reciver' AND receiver = '$sender' ) ORDER BY id DESC";
	$run = $con -> query($query);
	while ($row = $run->fetch_array()) :
	$name = $row['name'];
?>
<div id="message">
	<img class="message-avatar" src="images/user.png" alt="">
	<a class="message-author" href="#"> <?php echo $name;?> </a>
	<span class="message-date"> <?php echo formatDate($row['date']);?> </span>
	<span class="message-content"> <?php echo $row['message'];?> </span>
</div>
<?php endwhile; ?>