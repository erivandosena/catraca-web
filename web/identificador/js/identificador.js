$(function(){
	
	var tempo = window.setInterval(carrega, 1000);
	
	function carrega(){$('#usuario').load('?pagina=identificador #usuario');}
	
	if ($("div#dados").length) {
		$("span#aproxime").css("display","none");		
	}else{
		$("span#aproxime").css("display","block");		
	}	
	
	if ($("div#usuario").length) {
		var altura = $(window).height();
		var largura = $(window).width();
		
		$("#topo").css("display","none");
		$("#barra-governo").css("display","none");
		$(".acessibilidade").css("display","none");		
		$(".barra-menu").css("display","none");
		$(".config").css({	"max-width": largura, "height": altura })
	

		
	}
	
});