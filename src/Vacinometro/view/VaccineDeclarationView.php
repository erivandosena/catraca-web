<?php
            
/**
 * Classe de visao para VaccineDeclaration
 * @author Jefferson Uchôa Ponte <j.pontee@gmail.com>
 *
 */

namespace Vacinometro\view;
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
        <form id="insert_form_vaccine_declaration" class="user" method="post" enctype="multipart/form-data" >
            <input type="hidden" name="enviar_vaccine_declaration" value="1">                

            <div class="form-group">
                <label for="dose_number">Número de Doses</label>
                <input type="number" class="form-control"  name="dose_number" id="dose_number" placeholder="Dose Number">
            </div>

            <div class="form-group">
                <label for="card_file">Cartão de Vacinação</label>
                <input type="file" class="form-control"  name="card_file" id="card_file"  accept="image/png, image/jpeg">
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
                                            
                                            
                                            

          <div class="card">
                <div class="card-header">
                  Lista Vaccine Declaration
                </div>
                <div class="card-body">
                                            
                                            
		<div class="table-responsive">
			<table class="table table-bordered" id="dataTable" width="100%"
				cellspacing="0">
				<thead>
					<tr>
						<th>Id</th>
						<th>Id User Sig</th>
						<th>Dose Number</th>
						<th>Card File</th>
                        <th>Actions</th>
					</tr>
				</thead>
				<tfoot>
					<tr>
                        <th>Id</th>
                        <th>Id User Sig</th>
                        <th>Dose Number</th>
                        <th>Card File</th>
                        <th>Actions</th>
					</tr>
				</tfoot>
				<tbody>';
            
            foreach($lista as $element){
                echo '<tr>';
                echo '<td>'.$element->getId().'</td>';
                echo '<td>'.$element->getIdUserSig().'</td>';
                echo '<td>'.$element->getDoseNumber().'</td>';
                echo '<td>'.$element->getCardFile().'</td>';
                echo '<td>
                        <a href="?page=vaccine_declaration&select='.$element->getId().'" class="btn btn-info text-white">Select</a>
                        <a href="?page=vaccine_declaration&edit='.$element->getId().'" class="btn btn-success text-white">Edit</a>
                        <a href="?page=vaccine_declaration&delete='.$element->getId().'" class="btn btn-danger text-white">Delete</a>
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
            

            
	public function showEditForm(VaccineDeclaration $selecionado) {
		echo '
	    
	    

<div class="card o-hidden border-0 shadow-lg mb-4">
    <div class="card">
        <div class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
            <h6 class="m-0 font-weight-bold text-primary">Edit Vaccine Declaration</h6>
        </div>
        <div class="card-body">
            <form class="user" method="post" id="edit_form_vaccine_declaration">
                                        <div class="form-group">
                                            <label for="id_user_sig">Id User Sig</label>
                                            <input type="number" class="form-control" value="'.$selecionado->getIdUserSig().'"  name="id_user_sig" id="id_user_sig" placeholder="Id User Sig">
                						</div>
                                        <div class="form-group">
                                            <label for="dose_number">Dose Number</label>
                                            <input type="number" class="form-control" value="'.$selecionado->getDoseNumber().'"  name="dose_number" id="dose_number" placeholder="Dose Number">
                						</div>
                                        <div class="form-group">
                                            <label for="card_file">Card File</label>
                                            <input type="file" class="form-control" value="'.$selecionado->getCardFile().'"  name="card_file" id="card_file" placeholder="Card File">
                						</div>
                                        <div class="form-group">
                                            <label for="status">Status</label>
                                            <input type="text" class="form-control" value="'.$selecionado->getStatus().'"  name="status" id="status" placeholder="Status">
                						</div>
                                        <div class="form-group">
                                            <label for="created_at">Created At</label>
                                            <input type="datetime-local" class="form-control" value="'.$selecionado->getCreatedAt().'"  name="created_at" id="created_at" placeholder="Created At">
                						</div>
                <input type="hidden" value="1" name="edit_vaccine_declaration">
                </form>

        </div>
        <div class="modal-footer">
            <button form="edit_form_vaccine_declaration" type="submit" class="btn btn-primary">Cadastrar</button>
        </div>
    </div>
</div>

	    

										
						              ';
	}




            
        public function showSelected(VaccineDeclaration $vaccinedeclaration){
            echo '
            
	<div class="card o-hidden border-0 shadow-lg">
        <div class="card">
            <div class="card-header">
                  Vaccine Declaration selecionado
            </div>
            <div class="card-body">
                Id: '.$vaccinedeclaration->getId().'<br>
                Id User Sig: '.$vaccinedeclaration->getIdUserSig().'<br>
                Dose Number: '.$vaccinedeclaration->getDoseNumber().'<br>
                Card File: '.$vaccinedeclaration->getCardFile().'<br>
                Status: '.$vaccinedeclaration->getStatus().'<br>
                Created At: '.$vaccinedeclaration->getCreatedAt().'<br>
            
            </div>
        </div>
    </div>
            
            
';
    }


                                            
    public function confirmDelete(VaccineDeclaration $vaccineDeclaration) {
		echo '
        
        
        
				<div class="card o-hidden border-0 shadow-lg">
					<div class="card-body p-0">
						<!-- Nested Row within Card Body -->
						<div class="row">
        
							<div class="col-lg-12">
								<div class="p-5">
									<div class="text-center">
										<h1 class="h4 text-gray-900 mb-4"> Delete Vaccine Declaration</h1>
									</div>
						              <form class="user" method="post">                    Are you sure you want to delete this object?

                                        <input type="submit" class="btn btn-primary btn-user btn-block" value="Delete" name="delete_vaccine_declaration">
                                        <hr>
                                            
						              </form>
                                            
								</div>
							</div>
						</div>
					</div>
                                            
                                            
                                            
                                            
	</div>';
	}
                      


}