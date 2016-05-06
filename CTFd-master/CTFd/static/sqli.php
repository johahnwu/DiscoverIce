<html>
    <p> Insert Username to access user information.</p>
    <form action="sqli.php" method="GET">
        <input type="text" name="user">
        <input type="submit" name="Submit" value="Submit">
    </form>
    <?php
    //Values for mysql server
	include("db.inc.php");
    
	
    if(isset($_GET['user']))
    {
        $user = $_GET['user'];
        
        $getuser = "SELECT first_name, last_name FROM users WHERE username = '$user'" /*or die("Error in the query.." . mysqli_error($link))*/;
        $userquery = mysqli_query($link, $getuser);

        while ($num = mysqli_fetch_row($userquery))
        {
            $firstname = $num[0];
            $lastname = $num[1];
            echo "<p>First Name: $firstname</p>";
            echo "<p>Last Name: $lastname</p>";
            
        }
        
    }
    mysqli_close($link);
    
    ?>
</html>
