<?php 
    if(isset($_POST["opinfo"]))
    {
        $concat = $_POST["opinfo"];
        $arr = explode(":",$concat);
        $applicationname = $arr[0];
        $servicename = $arr[1];
        $requesttype = $arr[2];
        $username = $arr[3];
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
        //echo "Connected successfully";
        $sql = "select username,token from details";
        $result = $conn->query($sql);
        if($result->num_rows == 0){
            # this check is to ensure user is logged in
            $newURL = "http://0.0.0.0/index.html";
            header('Location: '.$newURL);
            exit();
        }
        $row = $result->fetch_assoc();
        $token = $row["token"];
        $username = $row["username"];
        $count = 1;
        
        
        $payload->appname = $applicationname;
        $payload->servicename = $servicename;
        $payload->username = $username;
        $jsonpayload = json_encode($payload);
        $url = "http://0.0.0.0:5000/output";
        $ch = curl_init();
        curl_setopt($ch,CURLOPT_URL, $url);
        curl_setopt($ch,CURLOPT_POST, true);
        curl_setopt($ch,CURLOPT_POSTFIELDS, $jsonpayload);
        curl_setopt($ch,CURLOPT_RETURNTRANSFER, true); 
        $result = curl_exec($ch);
        echo $result;
    }else{    
                echo "Illegal access";
        }
?>
