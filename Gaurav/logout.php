<?php
    $servername = "localhost";
    $username = "admindb";
    $password = "password";
    $dbname = "mydetails";
    // Create connection
    $conn = new mysqli($servername, $username, $password,$dbname);
    // Check connection
    if ($conn->connect_error) {
       die("Connection failed: " . $conn->connect_error);
    } 
    $sql = "delete from details where 1";
    $result = $conn->query($sql);
    echo "Logged Out";
?>