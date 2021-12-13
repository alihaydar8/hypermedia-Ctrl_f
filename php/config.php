<?php
	$servername="localhost";
    $username="hypermedia";
	$password="hypermedia";
	$dbname="hypermedia";
	$Connect = mysqli_connect($servername, $username, $password, $dbname);
	mysqli_set_charset( $Connect, 'utf8');


	function getContenuId($table,$id){ 
		global $Connect;
		$req_total = "  SELECT *	
						FROM   $table
						WHERE
						id_".$table." = '".$id."' 
				   ";
		// echo $req_total;
		$result = $Connect->query($req_total);
		 $results = $result->fetch_assoc(); 
		$ancien_historiques=array();
		foreach($results as $key => $value){
			$ancien_historiques[$key]=mysqli_real_escape_string($Connect,$value);
		}
		return $ancien_historiques;
	}
?>
