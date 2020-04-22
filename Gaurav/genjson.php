<?php
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
    if(isset($_POST['butstatus']))
    {
        $arr = explode(":",$_POST['butstatus']);
        $sens = $arr[0];
        $action = $arr[1];
        if($action == "Select")
        {
            $sql = "insert into ".$tablename." values(\"".$sens."\")";
            $conn->query($sql);
        }
        if($action == "Deselect")
        {
            $sql = "delete from ".$tablename." where sensorid=\"".$sens."\"";
            $conn->query($sql);
        }   
    }
    $urlforsend = "http://10.0.0.4/sendsensors.php";
    $button = "<form method=\"post\" action=\"".$urlforsend."\">
    <td><button type=\"submit\" name=\"sendsens\">Generate JSON</button></td>
    </form>";
    echo $button;
    $sensordata = file_get_contents("http://10.0.0.4:41095/getsensorfile");
    $sensordata = json_decode($sensordata,true);
    $sensordata = json_decode($sensordata,true);
    #now we display table
    $tc = "";
    $tc = "<table cellpadding=\"5\" width=\"500\">
         <th>Sensor</th>
         <th>Name</th>
         <th>Area</th>
         <th>Building</th>
         <th>Room no</th>
         <th>Status</th>";
    foreach( $sensordata as $sensor=>$details)
    {
        $sql = "select sensorid from ".$tablename." where sensorid=\"".$sensor."\"";
        $result = $conn->query($sql);
        $buttonValue = "";
        if ($result->num_rows == 0)
        {
            $buttonValue = "Select";
        }else{
            $buttonValue = "Deselect";
        }
        $tc.="<tr>";
        $tc.="<td>".$sensor."</td>";
        $tc.="<td>".$details[sensor_name]."</td>";
        $tc.="<td>".$details[sensor_address][area]."</td>";
        $tc.="<td>".$details[sensor_address][building]."</td>";
        $tc.="<td>".$details[sensor_address][room_no]."</td>";
        $tc.="<form method=\"post\" action=\"".$_SERVER["PHP_SELF"]."\">
               <td><button type=\"submit\" name=\"butstatus\" value=\"".$sensor.":".$buttonValue."\">".$buttonValue."</button></td>
               </form>";
        $tc.="</tr>";
    }
    echo $tc;
    $conn->close();
?>
