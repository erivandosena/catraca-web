

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
            
                console.log(data.split(":"));
            	if(data.split(":")[1] == 'sucesso'){
            		
            		$("#botao-modal-resposta").click(function(){
            			window.location.href='?page=vaccine_declaration';
            		});
            		$("#textoModalResposta").text("Vaccine Declaration enviado com sucesso! ");                	
            		$("#modalResposta").modal("show");
            		
            	}
            	else
            	{
            		console.log(data);
                	$("#textoModalResposta").text("Falha ao inserir Vaccine Declaration, fale com o suporte. ");                	
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
   
