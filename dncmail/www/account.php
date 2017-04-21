<?php
// initialize global variables, authentication and database connections
include('includes/common.php');

// if the user is NOT logged in, redirect him to login page
if (!$auth->user_id()) {
	redirect('/');
}

// handle the form submission
$action = @$_POST['action'];
if ($action == 'save') {
  $pubkey = $db->escape($_POST['pubkey']);
  $db->query("UPDATE users SET pubkey='$pubkey' WHERE user_id='".$auth->user_id()."'");
  notify('Changes saved');
  reload();
}

// get a queried public key if search form is submitted
$email = @$_GET['email'];
if ($email) {
  $queried_announcement = $db->query("SELECT pubkey FROM users WHERE email='$email'")->next();  
}

// grab form values from database if available
$row = $db->query("SELECT pubkey FROM users WHERE user_id='".$auth->user_id()."'")->next();
$my_pubkey = $row['pubkey'];

include('includes/header.php');
?>

    <div class="row">
     <div class="span4 offset1">
      <h4>Look up a DNC member's announcement</h4>
      <p>You may use this form to find the latest announcement associated with a given email address.</p>
      <form method="get">
       <label>Email address:</label>
       <input type="text" name="email" value="<?php echo stripslashes(@$email) ?>">
       <div>
        <button class="btn submit">Look up</button>
       </div>
      </form>
     </div>
     <div class="span6">
<?php if (@$email): ?>
<?php   if ($queried_announcement): ?>
      <h4>The latest announcement from <?php echo htmlentities($email) ?>:
      <pre id="announcement-entry">
      <!-- user data appears here -->
      </pre>
      <div id="result" data-result="announcement='<?php echo str_replace("\n", "\\n", normalize_newlines($queried_announcement['pubkey'])) ?>'"></div>
      <script>
eval(document.getElementById('result').getAttribute('data-result'));
document.getElementById('announcement-entry').innerHTML = announcement;
      </script>
<?php   else: ?>
      <p>This email address is not registered.</p>
<?php   endif; ?>
<?php endif; ?>
     </div>
    </div>

<hr>

    <div class="row">
     <div class="span10 offset1">
      <h3>Your Latest Announcement</h3>
      <form method="post" action="/account.php">
       <textarea name="pubkey"><?php echo htmlentities($my_pubkey) ?></textarea>
       <div>
        <button class="btn submit" name="action" value="save">Save</button>
       </div>
      </form>
     </div>
    </div>
<?php
include('includes/footer.php');
?>
