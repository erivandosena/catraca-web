<?php
/**
 *
 * @author Jefferson Uchôa Ponte
 *
 */
class RelatorioIsentoController {
    private $view;
    private $dao;
    public static function main($nivelDeAcesso) {
        switch ($nivelDeAcesso) {
            case Sessao::NIVEL_SUPER :
                $controller = new RelatorioIsentoController();
                $controller->relatorio ();
                break;
            case Sessao::NIVEL_ADMIN :
                $controller = new RelatorioIsentoController();
                $controller->relatorio ();
                break;
                
            default :
                UsuarioController::main ( $nivelDeAcesso );
                break;
        }
    }
    public function __construct(){
        $this->dao = new UnidadeDAO ();
        $this->view = new RelatorioAvulsoView();
    }
    
    public function relatorio() {
        echo '<div class="borda doze colunas">';

        
            echo '
            <form action="">
                Selecione a data que deseja consultar. 
                <input type="date" name="data">
                <input type="hidden" name="pagina" value="relatorio_isentos">
                <input name="relatorio" value="Gerar Relatório" type="submit">
            </form>';
        if(isset($_GET['data'])){
            $data = date("Y-m-d G:i:s", strtotime($_GET['data']));
            $this->gerar($data);
            echo '<a href="?pagina=relatorio_isentos&relatorio=1">Clique aqui para visualizar o histórico Completo de Isenções</a>';
        }else if(isset($_GET['relatorio'])){
            $this->gerar();
        }
        
        
        echo '</div>';
        
    }

    public function gerar($data = null){
        if($data != null){
            $sql = "SELECT * FROM isencao
                INNER JOIN cartao ON cartao.cart_id = isencao.cart_id
                INNER JOIN vinculo ON vinculo.cart_id = cartao.cart_id
                INNER JOIN usuario ON usuario.usua_id = vinculo.usua_id
                WHERE '$data' BETWEEN isencao.isen_inicio AND isen_fim";
            
        }else{
            
            $sql = "SELECT * FROM isencao
                INNER JOIN cartao ON cartao.cart_id = isencao.cart_id
                INNER JOIN vinculo ON vinculo.cart_id = cartao.cart_id
                INNER JOIN usuario ON usuario.usua_id = vinculo.usua_id";
            
        }
        
        $result = $this->dao->getConexao()->query($sql);
        $i = 0;
        echo '<br><table  class="tabela borda-vertical zebrada">';
        echo '<thead>';
        echo '<tr><th>Usuario</th><th>Início da Isenção</th><th>Fim da Isenção</th></tr>';
        echo '</thead>';
        echo '<tbody>';
        foreach($result as $linha){
            $i++;
            echo '<tr><td>'.$linha['usua_nome'].'</td><td>'.date("d/m/Y",strtotime($linha['isen_inicio'])).'</td><td>'.date("d/m/Y", strtotime($linha['isen_fim'])).'</td></tr>';
        }
        echo '</tbody>';
        echo '</table>';
        if($data != null){
            echo '<br><p>'.$i.' isenções válidas na data '.date("d/m/Y" ,strtotime($data)).'</p>';
        }
        
    }
    
    
}

?>