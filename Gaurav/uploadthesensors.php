<?php

$storeFolder = "/var/www/";
$storezip = $storeFolder.basename($_FILES["zipFile"]["name"]);
$tempFile = $_FILES["zipFile"]["tmp_name"];
$check = move_uploaded_file($tempFile,$storezip);
$myObj->token = "";
$myJSON = json_encode($myObj);
$url = "http://0.0.0.0:5057/sensorUpload";
$ch = curl_init();
curl_setopt($ch,CURLOPT_URL, $url);
curl_setopt($ch,CURLOPT_POST, true);
curl_setopt($ch,CURLOPT_POSTFIELDS, $myJSON);
curl_setopt($ch,CURLOPT_RETURNTRANSFER, true); 
$result = curl_exec($ch);
?>