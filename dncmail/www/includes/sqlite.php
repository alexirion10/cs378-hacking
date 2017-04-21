<?php

// this file handles database interaction

class Database {
    var $database;
    function Database($filename){
        $victim_key = 'We are going to build a Dyson Sphere and make the Galactic Federation pay for it!';
        $this->database = new SQLite3($filename);
        $this->database->busyTimeout(500);
        $exists = filesize($filename) > 0;
        if (!$exists) {
            $this->database->exec('CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, username TEXT, password TEXT, salt TEXT, pubkey TEXT)');
            $this->database->exec('INSERT INTO users (email, username, password, salt, pubkey) VALUES (\'victim@naive.com\', \'victim\', \'\', \'\', \''.$victim_key.'\')');
        }
    }
    function query($q){
        $result = $this->database->query($q);
        return new ResultSet($result);
    }

    function escape($s){
        return $this->database->escapeString($s);
    }

    function __destruct() {
        $this->database->close();
    }
}

class ResultSet {
    var $result;
    var $currentRow;
    
    function ResultSet(&$result){
        $this->result =& $result;
    }

    function getCurrentValueByName($name){
        if($this->currentRow)
            return $this->currentRow[$name];
        return false;
    }

    function next(){
        $this->currentRow = $this->result->fetchArray();
        return $this->currentRow;
    }
    
    // ignore row number this is so broke
    function getValueByNr($rowno,$colno){
        if(!$this->currentRow)
            $this->next();
        return $this->currentRow[$colno];

    }

    function getCurrentValues(){
        if(!$this->currentRow)
            $this->next();
        return $this->currentRow;
    }

}
?>
