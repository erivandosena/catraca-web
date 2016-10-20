<?php

class GeraPDFController{
	
	public function geraPDF($html){
		
		$geraPDF = new mPDF();
		$geraPDF->WriteHTML($html);
		$geraPDF->Output();
		exit();
		
	}
	
}

?>