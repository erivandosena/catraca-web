$(function(){
	
	if($("#custo-refeicao").length){
		$("#form-custo-refeicao").css("display","none");
	}
	
	if($("#custo-cartao").length){
		$("#form-custo-cartao").css("display","none");
	}
	
	if($("#form-confirma").length){
		$("#form-custo-unidade").css("display","none");
	}
	
	if($("#form-confirma-cartao").length){
		$("#pergunta").css("display","none");
	}
	
	if($("#catraca-virtual").length){
		$(".fundo").css("top","10%");
	}
	
	$("#btnUser").click(function (){		
		$("#marcacao").toggle();		
	});	
	
});