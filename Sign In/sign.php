<html>
<body>
	<h1>Welcome</h1><br>
	<h3><b><?php
	echo $_GET["username"];
		?></b></h3><br>
	You are a <?php
	echo $_GET["gender"];
	?><br>
	your Date of Birth is : <?php
	echo $_GET["dob"];
	?><br>
	your skin colour is : <?php
	echo $_GET["sc"];
	?><br>
	Email : <?php
	echo $_GET["email"];
	?><br>
	picture :<?php
	echo $_GET["file"];
	?><br>
</body>
</html>