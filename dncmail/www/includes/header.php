<!DOCTYPE html>
<html>
 <head>
  <title>DNC Mail</title>
  <link href="/assets/bootstrap/css/bootstrap.css" rel="stylesheet" type="text/css">
  <link href="/assets/screen.css" rel="stylesheet" type="text/css">
  <link href="/assets/bootstrap/css/bootstrap-responsive.css" rel="stylesheet" type="text/css">
 </head>
 <body>
    <div class="row" align="center">
      <form action="notimp.php">
       <label style="color:white;">Search Announcements:</label>
       <input type="text" id="decoy">
       <div>
        <input type="submit" value ="search">
       </div>
      </form>
     </div>
  <div class="container header">
   <img src="/assets/dnc.png" width = 314 height=134>
   <h2 align="center">Democratic National Committee</h2>
   <h3 align="center">Secure Announcement Server</h3>
<?php if ($auth->user_id()): ?>
   <p>You are logged in as <?php echo $auth->username() ?> (<?php echo $auth->email() ?>) - <a href="?logout">Log out</a></p>
<?php endif; ?>
  </div>
  <div class="container main">
<?php if (@$_SESSION['notification']): ?>
  <div class="alert alert-<?php echo $_SESSION['notification']['type'] ?>">
   <button type="button" class="close" data-dismiss="alert" data-identifier="<?php echo $n->notification_id ?>">&times;</button>
   <?php echo htmlentities($_SESSION['notification']['message']) ?>
  </div>
<?php $_SESSION['notification'] = false; endif; ?>
