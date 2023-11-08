

$(document).ready(
	function(){
		$('.botao-anexo').click(trocarImagemModal);
	}
);

function trocarImagemModal(){
	var imagem = $(this).attr('src');
	$('#imagem-modal-anexo').attr('src', imagem);
}

$(document).ready(function(e) {
	$("#insert_form_vaccine_declaration").on('submit', function(e) {
		e.preventDefault();
        $('#modalAddVaccineDeclaration').modal('hide');
        
        var dados = new FormData(this);
        
		jQuery.ajax({
            type: "POST",
            url: "index.php?ajax=vaccine_declaration",
            data: dados,
            success: function( data )
            {
            
                
            	if(data.split(":")[1] == 'sucesso'){
            		
            		$("#botao-modal-resposta").click(function(){
            			window.location.href='?pagina=vaccine_declaration';
            		});
            		$("#textoModalResposta").text("Cartão de Vacina Enviada Com Sucesso! ");                	
            		$("#modalResposta").modal("show");
            		
            	}
            	else
            	{
            		console.log(data);
                	$("#textoModalResposta").text("Falha ao enviar cartão de vacina. ");                	
            		$("#modalResposta").modal("show");
            	}

            },
            cache: false,
            contentType: false,
            processData: false,
            xhr: function() { // Custom XMLHttpRequest
                var myXhr = $.ajaxSettings.xhr();
                if (myXhr.upload) { // Avalia se tem suporte a propriedade upload
                    myXhr.upload.addEventListener('progress', function() {
                    /* faz alguma coisa durante o progresso do upload */
                    }, false);
                }
                return myXhr;
            }
        });
		
		
	});
	
	
});
   
