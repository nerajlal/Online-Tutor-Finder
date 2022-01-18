<?php
	include 'connection.php';
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
	$chat = $get_user_name['chatting'];
	}
	$receiver = $_POST['x'];
	
?>





<!DOCTYPE html>
<html>
<head>
<style>
	.butt {
	background-color: red;
	border: none;
	color: white;
	padding: 15px 32px;
	text-align: center;
	text-decoration: none;
	display: inline-block;
	font-size: 16px;
	margin: 4px 2px;
	cursor: pointer;
	}
	</style>
	</head>
	<body>
	<a href="../notification.php" class="butt">Leave Chat</a>
	<title>Chat Room</title>
	<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
	<link rel="stylesheet" type="text/css" href="css/main.css">
	<script >
		function ajax(){
			var req = new XMLHttpRequest();
			req.onreadystatechange = function() {
				if(req.readyState == 4 && req.status == 200){
					document.getElementById('chat').innerHTML = req.responseText;	
				}
			}
			req.open('GET','chat.php',true);
			req.send();
		}
		setInterval(function() {ajax()}, 1000);
	</script>
</head>
<body onload="ajax();">
	<h2 align="center" style="border-bottom: 1px solid grey;"> CHAT ROOM</h2>
	<div class="ibox-content">
        <div class="row">
            <div style="margin-left: 10%;" class=" col-md-10">
                <div class="chat-discussion">
                    <div class="chat-message left">
                        <div id="chat"></div>
                    </div>
                </div>
            </div>
		</div>
	</div>
	<div style="background-color:white;" class="row">
     	<div style="margin-left: 20%;" class="col-md-8">
			<form method="POST" action="index2.php">
				<div></div>
				<textarea name="message" placeholder="Enter your message" required=""></textarea>
				<input type="submit" style="color: white;" name="submit" value="Send it"/>
			</form>
		</div>
	</div>
	
	
	
	
	
	
	
	
	<div class="footer">
	</div>
	<?php
		if(isset($_POST['submit'])){
		    $value=$reciver;
			$name = $uname_db;
			$message = $_POST['message'];
			$query = "INSERT INTO chat (name, message, receiver) VALUES ('$name','$message','$chat')";
			$run = $con -> query($query);

			if($run){
				?>
				<audio src='audio/notification.mp3' hidden='true' autoplay='true'/>
				<?php
			}
		}
	?>
</body>
</html>