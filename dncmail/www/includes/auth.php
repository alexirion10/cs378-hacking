<?php

class Auth {
	
	// we store a reference to the database so that we can access it
	var $db = null;
	function Auth(&$db) {
		$this->db = $db;
	}
	
	
	// get information about logged in user if available, false if not logged in
	function user_id() {
		return @$_SESSION['user_id'];
	}
	function username() {
		return @$_SESSION['username'];
	}
	function email() {
		return @$_SESSION['email'];
	}

	// basic authentication functions
	function logout() {
		session_destroy();
	}
	
	function login($username, $password) {
		$escaped_username = $this->db->escape($username);
		// get the user's salt
		$sql = "SELECT salt FROM users WHERE username='$escaped_username'";
		$result = $this->db->query($sql);
		$user = $result->next();
		// make sure the user exists
		if (!$user) {
			notify('User does not exist', -1);
			return false;
		}
		// verify the password hash
		$salt = $user['salt'];
		$hash = md5($salt.$password);
		$sql = "SELECT user_id, email, username FROM users WHERE username='$username' AND password='$hash'";
		$userdata = $this->db->query($sql)->next();
		if ($userdata) {
			// awesome, we're logged in
			$_SESSION['user_id'] = $userdata['user_id'];
			$_SESSION['username'] = $userdata['username'];
			$_SESSION['email'] = $userdata['email'];
		} else {
			notify('Invalid password', -1);
			return false;
		}
	}
	function register($email, $username, $password1, $password2) {
		$escaped_email = $this->db->escape($email);
		$escaped_username = $this->db->escape($username);
		// make sure the user doesn't exist
		$sql = "SELECT user_id FROM users WHERE username='$escaped_username'";
		$result = $this->db->query($sql);
		if ($result->next()) {
			notify('User exists!', -1);
			return false;
		}
		// make sure the passwords match
		if ($password1 != $password2) {
			notify('Passwords do not match', -1);
			return false;
		}
		// OK good to go! Generate a salt and insert the user
		$salt = mt_rand(10000,99999);
		$hash = md5($salt.$password1);
		$sql = "INSERT INTO users (email, username, password, salt) VALUES ".
			"('$escaped_email', '$escaped_username', '$hash', '$salt')";
		$this->db->query($sql);
		// redirect to homepage
		notify('Account '.$username.' registered. Please log in');
	}
}


?>
