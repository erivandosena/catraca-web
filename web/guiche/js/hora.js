$(function(){
	
	var tempo = window.setInterval(carrega, 1000);	
	function carrega(){$('#hora').load('?pagina=gerador #hora');}
	
});