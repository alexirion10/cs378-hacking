<?php
// initialize global variables, authentication and database connections
include('includes/common.php');

// if the registration form has been submitted, handle it
$action = @$_POST['action'];
if ($action == 'register') {
	$auth->register($_POST['email'], $_POST['login'], $_POST['pw1'], $_POST['pw2']);
  redirect('/');
}

// if the user is logged in, redirect him to home.php
if ($auth->user_id()) {
	redirect('/account.php');
}


// otherwise, display a login page
include('includes/header.php');
?>
   <div class="row">
    <div class="span10 offset1">
     <h3>Registration</h3>
     <p>
      Please provide a valid email address: announcements that you upload will be associated with this address.
     </p>
    </div>
   </div>

   <div class="row">

    <div class="span4 offset4 register">
     <div class="well">
      <form method="post">
       <fieldset>
        <label>Username:</label>
        <input type="text" name="login">
        <label>Email address:</label>
        <input type="text" name="email">
        <label>Password:</label>
        <input type="password" name="pw1">
        <label>Repeat password:</label>
        <input type="password" name="pw2">
        <div>
         <button class="btn" type="submit" name="action" value="register">Register</button>
        </div>
       </fieldset>
      </form>
     </div>
    </div>
   </div>
<?php
include('includes/footer.php');
?>
