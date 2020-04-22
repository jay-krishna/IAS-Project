<?php

    $dbservername = "localhost";
    $dbusername = "admindb";
    $dbpassword = "password";
    $dbname = "mydetails";
    $conn = new mysqli($dbservername, $dbusername, $dbpassword, $dbname);
    if ($conn->connect_error){
        die("Connection failed: " . $conn->connect_error);
    }
    $usernamequery = "select username from details";
    $result = $conn->query($usernamequery);
    if($result->num_rows == 0){
        # this check is to ensure user is logged in
        $newURL = "http://0.0.0.0/index.html";
        header('Location: '.$newURL);
        exit();
    }
    $row = $result->fetch_assoc();
    $username = $row["username"];
    $myObj->username = $username;
    $conn->close();
    $myJSON = json_encode($myObj);
    #pratik
    $url = "http://0.0.0.0:5051/getsensordata";
    $ch = curl_init();
    curl_setopt($ch,CURLOPT_URL, $url);
    curl_setopt($ch,CURLOPT_POST, true);
    curl_setopt($ch,CURLOPT_POSTFIELDS, $myJSON);
    curl_setopt($ch,CURLOPT_RETURNTRANSFER, true); 
    $result = curl_exec($ch);
    //echo $jsonobj;
    $temp = json_decode($result,true);
    $parseit = json_decode($temp,true);
    $tc="";
    $tc = "<table cellpadding=\"5\" width=\"500\">
         <th>Name</th>
         <th>Area</th>
         <th>Building</th>
         <th>Room no</th>";
    for ($i=0; $i<sizeof($parseit);$i++)
    {

        $tc.= "<tr>";
        $tc.= "<td>".$parseit[$i][sensor_name]."</td>";
        $tc.= "<td>".$parseit[$i][sensor_address][area]."</td>";
        $tc.= "<td>".$parseit[$i][sensor_address][building]."</td>";
        $tc.= "<td>".$parseit[$i][sensor_address][room_no]."</td>";
        $tc.= "</tr>";
    }
    echo $tc;
?>