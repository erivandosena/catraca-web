<?php

   
    
	$dateStart 		= new DateTime($dateStart);
    $dateEnd 		= new DateTime($dateEnd);
    
 
    //Prints days according to the interval
    $dateRange = array();
    while($dateStart <= $dateEnd){
        $dateRange[] = $dateStart->format('Y-m-d');
        $dateStart = $dateStart->modify('+1day');
    }
 
    var_dump($dateRange);

?>



