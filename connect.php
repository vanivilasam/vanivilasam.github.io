<?php
$fullName = $_POST['fulnm'];
$phoneNumber = $_POST['phonenum'];
$Class = $_POST['class'];

$conn = new mysql('localhost','root','','test');
if ($conn->connect_error){
	die('Connect Eroor :' $conn->connect_error );
	
}else $stmt = $conn->prepare("insert into testing(fullName, lastName, phonenumber, class) values(?, ?, ?)");
		$stmt->bind_param("ssi", $fullName, $phoneNumber, $Class);
		$execval = $stmt->execute();
		echo $execval;
		echo "Registration successfully...";
		$stmt->close();
		$conn->close();
	



?>