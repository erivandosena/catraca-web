<?php
function isLogin($usuario, $senha) {

	$ds = ldap_connect ( "ldap", "389" );
	$sr = ldap_search ( $ds, "ou=Users, dc=edsonk, dc=com", "(|(sn=$usuario*)(givenname=$usuario*)(uid=$usuario))");
	$info = ldap_get_entries ( $ds, $sr );
	$cnC = $info [0] ["dn"];
	ldap_close ( $ds );
	$comando = "ldapsearch -x -w " . $senha . " -D '" . $cnC . "' uid='" . $usuario . "' uidNumber";
	$rs = exec ( $comando, $output );
	if ($rs != "") {
		$tmp = explode ( " ", $output [10] );
		echo "ID: " . $tmp [1];
		return true;
	}
	return false;
}

if (! isLogin ( $_POST ['usuario'], $_POST ['senha'] )) {
	echo "Fracasso";
	
} else {
	echo "Sucesso!";
}

