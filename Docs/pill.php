<html>
<h1>SEARCH ORDER PANEL</h1>
<body>
<form name="home" action = "<?php echo $_SERVER['PHP_SELF'];?>" method = "post">
<label>Order Number</label><br>
<input type = "text" name = "order_id" placeholder = "enter order id"><br>
<br><input type = "submit" name ="select" value = "submit" >
</form>
<hr>
</body>
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST"){
$url="http://cybapangolin.atwebpages.com/rest2/api.php?order_id=";
$url .= $_POST['order_id'];
    $client = curl_init($url);
    curl_setopt($client,CURLOPT_RETURNTRANSFER, true);
    $response = curl_exec($client);

    $result = json_decode($response);

    echo "<table>";
    echo "<tr><td>Order ID:</td><td>$result->order_id</td></tr>";
    echo "<tr><td>Amount:</td><td>$result->amount</td></tr>";
    echo "<tr><td>Response Code:</td><td>$result->response_code</td></tr>";
    echo "<tr><td>Response Desc:</td><td>$result->response_desc</td></tr>";
    echo "</table>";
}
?>
