<?php
            
/**
 * Classe de visao para VaccineDeclaration
 * @author Jefferson Uchôa Ponte <j.pontee@gmail.com>
 *
 */

namespace Vacinometro\view;

use Usuario;
use Vacinometro\model\VaccineDeclaration;


class VaccineDeclarationView {
    public function showInsertForm() {
		echo '
<!-- Button trigger modal -->
<button type="button" class="btn btn-primary m-3" data-bs-toggle="modal"  data-bs-target="#modalAddVaccineDeclaration">
  Declarar Vacinação
</button>

<!-- Modal -->
<div class="modal fade" id="modalAddVaccineDeclaration" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Submeter Cartão de Vacinação</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <p>Declaro, sob as penas da lei, que as informações prestadas neste habite-se são de minha inteira
        responsabilidade, e que tenho ciência que a universidade poderá a qualquer tempo realizar o
        monitoramento/fiscalização do documento, procedendo à declaração de nulidadedo mesmo, caso seja
        constatado que foram prestadas declarações falsas ou enganosas, omitidas informações relevantes ou em
        desacordo com a legislação vigente, além da aplicação das demais penalidades administrativas, cíveis e penais
        cabíveis.</p>
        <form id="insert_form_vaccine_declaration" class="user" method="post" enctype="multipart/form-data" >
            <input type="hidden" name="enviar_vaccine_declaration" value="1">                

            <div class="form-group">
                <label for="dose_number">Número de Doses</label>
                <input type="number" class="form-control"  name="dose_number" id="dose_number" placeholder="Dose Number" required>
            </div>

            <div class="form-group">
                <label for="card_file">Cartão de Vacinação</label>
                <input type="file" class="form-control"  name="card_file" id="card_file"   accept="application/pdf" required>
            </div>
        </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Fechar</button>
        <button form="insert_form_vaccine_declaration" type="submit" class="btn btn-primary">Salvar</button>
      </div>
    </div>
  </div>
</div>





<!-- Modal Resposta -->
<!-- Modal -->
<div class="modal fade" id="modalResposta" tabindex="-1" aria-labelledby="labelModalResposta" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="labelModalResposta">Resposta</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <span id="textoModalResposta"></span>
      </div>
      <div class="modal-footer">
        <button type="button" id="botao-modal-resposta"  data-bs-dismiss="modal" class="btn btn-primary">Continuar</button>
      </div>
    </div>
  </div>
</div>


			
';
	}



                                            
                                            
    public function showList($lista){
           echo '
                                            
                                            
                                            

          <div class="card m-4">
                <div class="card-header">
                  Lista de Cartões de Vacina Submetidos
                </div>
                <div class="card-body">
                                            
                                            
		<div class="table-responsive">
			<table class="table table-bordered" id="dataTable" width="100%"
				cellspacing="0">
				<thead>
					<tr>
                        <th>Id</th>
                        <th>Estado</th>
                        <th>Cartão de Vacina</th>
                        <th>Avaliar</th>
					</tr>
				</thead>
				<tfoot>
					<tr>
                        <th>Id</th>
                        <th>Estado</th>
                        <th>Cartão de Vacina</th>
                        <th>Avaliar</th>
					</tr>
				</tfoot>
				<tbody>';
            
            foreach($lista as $element){
                
                echo '<tr>';
                echo '<td>'.$element->getId().'</td>';
                echo '<td>'.$element->getStrPTStatus().'</td>';
                echo '<td>'.$element->getCardFile().'</td>';
                echo '<td>
                        <a href="?pagina=vaccine_declaration&edit='.$element->getId().'" class="btn btn-success text-white">Avaliar</a>
                      </td>';
                echo '</tr>';
            }
            
        echo '
				</tbody>
			</table>
		</div>
            
            
            
            
  </div>
</div>
            
';
    }
            

                                            
    public function showListMy($lista){
        echo '
                                         
                                         
                                         

       <div class="card">
             <div class="card-header">
               Meus Envios
             </div>
             <div class="card-body">
                                         
                                         
     <div class="table-responsive">
         <table class="table table-bordered" id="dataTable" width="100%"
             cellspacing="0">
             <thead>
                 <tr>
                     <th>Número de Doses</th>
                     <th>Data de Envio</th>
                     <th>Estado</th>
                 </tr>
             </thead>
             <tfoot>
                 <tr>
                     <th>Número de Doses</th>
                     <th>Data de Envio</th>
                     <th>Estado</th>
                 </tr>
             </tfoot>
             <tbody>';
         //<object data="'.$element->getCardFile().'" height="100%" width="100%"></object>
         foreach($lista as $element){

             echo '<tr>';
             echo '<td>'.$element->getDoseNumber().'</td>';
             
             echo '<td>
                     '.date("d/m/Y H:i:s", strtotime($element->getCreatedAt())).'
                   </td>
                   <td>'.$element->getStrPTStatus().'</td>
                   ';
             echo '</tr>';
         }
         
     echo '
             </tbody>
         </table>
     </div>
         
         
         
         
</div>
</div>
         
';
 }
         
            
	public function showEditForm(VaccineDeclaration $selecionado, Usuario $usuario) {

        if($selecionado->getCardFile() != null && file_exists($selecionado->getCardFile())){
            $file = file_get_contents($selecionado->getCardFile());
            $encoded = chunk_split(base64_encode( $file ));
            
        }
        
        // echo $encoded;
        
        
		echo '
	    
	    

<div class="card o-hidden border-0 shadow-lg m-4">
    <div class="card">
        <div class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
            <h6 class="m-0 font-weight-bold text-primary">Deferir ou Indeferir</h6>
        </div>

        <div class="card-body">

            <p>Nome do Usuário: '.$usuario->getNome().'</p>
            <p>Cartão de Vacinação: </p>
            <object width="100%" height="500" data="data:application/pdf;base64,'.$encoded.'" type="application/pdf">
                <p>Seu navegador não tem um plugin pra PDF</p>
            </object>
            <form class="user" method="post" id="edit_form_vaccine_declaration">
                                       
                                        
                                        <div class="form-group">
                                            <label for="status">Estado:</label>
                                            <select class="form-select" aria-label="Default select example" required name="status" id="status" >
                                            <option selected>Selecione uma opção</option>
                                                <option value="'.VaccineDeclaration::STATUS_APPROVED.'" selected>Deferido</option>
                                                <option value="'.VaccineDeclaration::STATUS_DISAPPROVED.'">Indeferido</option>
                                            </select>
                                            
                						</div>
                                       
                <input type="hidden" value="1" name="edit_vaccine_declaration">
                </form>

        </div>
        <div class="modal-footer">
            <button form="edit_form_vaccine_declaration" type="submit" class="btn btn-primary">Atualizar</button>
        </div>
    </div>
</div>

	    

										
						              ';
	}





          


}