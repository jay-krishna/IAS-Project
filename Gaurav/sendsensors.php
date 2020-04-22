<?php
    header('Content-Type: application/json');
    $dbservername = "localhost";
    $dbusername = "admindb";
    $dbpassword = "password";
    $dbname = "mydetails";
    $conn = new mysqli($dbservername, $dbusername, $dbpassword, $dbname);
    if ($conn->connect_error){
        die("Connection failed: " . $conn->connect_error);
    }
    $tablename = "sensor";
    $sql = "create table if not exists ".$tablename."(sensorid varchar(30))";
    $conn->query($sql);
    $sql = "select sensorid from sensor";
    $result = $conn->query($sql);
    $sendit =  array();
    while ($row = $result->fetch_assoc())
    {
        array_push($sendit,$row["sensorid"]);
    }
    $deleteall = "delete from sensor where 1";
    $conn->query($deleteall);
    $conn->close();
    $jsonobj = json_encode($sendit);
    $jsonobjsend->sensors = $jsonobj;
    $jsonobjsend = json_encode($jsonobjsend);
    $url = "http://10.0.0.4:41095/getsensorfile";
    $ch = curl_init();
    curl_setopt($ch,CURLOPT_URL, $url);
    curl_setopt($ch,CURLOPT_POST, true);
    curl_setopt($ch,CURLOPT_POSTFIELDS, $jsonobjsend);
    curl_setopt($ch,CURLOPT_RETURNTRANSFER, true); 
    $result = curl_exec($ch);
    $temp = json_decode($result);
    $json_pretty = json_encode(json_decode($temp), JSON_PRETTY_PRINT);
    echo $json_pretty;
?>