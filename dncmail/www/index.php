<?php
// initialize global variables, authentication and database connections
include('includes/common.php');

// if the login form has been submitted, handle it
$action = @$_POST['action'];
if ($action == 'login') {
	$auth->login($_POST['login'], $_POST['pw']);
}

// if the user is logged in, redirect him to home.php
if ($auth->user_id()) {
	header('location: /account.php');
}


// otherwise, display a login page
include('includes/header.php');
?>
   <div class="row">

    <div class="span6 offset1">
     <h3>Hello!</h3>
     <p>
     Welcome to the canonical announcement server for the DNC, guaranteed* to protect against Russia, China, and 400 pound hackers. 
     </p>
     <p>
      If you would like an account, please <a href="/register.php">register here</a>.
     </p>
     <p>
</br>
</br>
     <font size = 1> *Not guaranteed </font>
     </p>
    </div>
   
    <div class="span4">
     <div class="well">
      <form method="post">
       <fieldset>
        <legend>Please log in</legend>
        <label>Username:</label>
        <input type="text" name="login" value="<?php echo @$_POST['login'] ?>">
        <label>Password:</label>
        <input type="password" name="pw">
        <div>
         <button class="btn" type="submit" name="action" value="login">Log In</button>
        </div>
       </fieldset>
      </form>
     </div>
    </div>



   </div>
<?php
include('includes/footer.php');
?>
