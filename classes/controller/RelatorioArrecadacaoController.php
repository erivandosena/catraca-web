<?php

class RelatorioArrecadacaoController
{

    private $view;

    private $dao;

    public static function main($nivelDeAcesso)
    {
        switch ($nivelDeAcesso) {
            case Sessao::NIVEL_SUPER:
                $controller = new RelatorioArrecadacaoController();
                $controller->relatorio();
                break;
            case Sessao::NIVEL_ADMIN:
                $controller = new RelatorioArrecadacaoController();
                $controller->relatorio();
                break;
            
            case Sessao::NIVEL_POLIVALENTE:
                $controller = new RelatorioArrecadacaoController();
                $controller->relatorio();
                break;
            case Sessao::NIVEL_CATRACA_VIRTUAL:
                $controller = new RelatorioArrecadacaoController();
                $controller->relatorio();
                break;
            case Sessao::NIVEL_USUARIO_EXTERNO:
                $controller = new RelatorioArrecadacaoController();
                $controller->relatorio();
                break;
            case Sessao::NIVEL_CATRACA_VIRTUAL_ORFA:
                $controller = new RelatorioArrecadacaoController();
                $controller->relatorio();
                break;
            default:
                UsuarioController::main($nivelDeAcesso);
                break;
        }
    }

    public function __construct()
    {
        $this->dao = new UnidadeDAO();
        $this->view = new RelatorioArrecadacaoView();
    }

    public function relatorio()
    {
        if (! isset($_GET['gerar'])) {
            $listaDeUnidades = $this->dao->retornaLista();
            $this->view->exibirFormulario($listaDeUnidades);
            return;
        }
        if (! isset($_GET['data_inicial']) || ! isset($_GET['data_final'])) {
            echo "Preencha duas datas";
            return;
        }
        $unidades = array();
        foreach ($_GET as $chave => $valor) {
            if (strstr($chave, 'unidade')) {
                $unidades[] = $valor;
            }
        }
        $this->geraValoresArrecadados($unidades, $_GET['data_inicial'], $_GET['data_final']);
    }

    public function geraValoresArrecadados($listaDeUnidades, $dateStart, $dataEnd)
    {
        if (! count($listaDeUnidades)) {
            echo "Nenhuma unidade selecionada";
            return;
        }
        
        $dao = new TipoDAO($this->dao->getConexao());
        $turnoDao = new TurnoDAO($this->dao->getConexao());
        $listaDeTurnos = $turnoDao->retornaLista();
        
        $tipos = $dao->retornaLista();
        
        $strFiltroUnidade = "";
        $strUnidade = "Restaurantes: ";
        $unidadeDao = new UnidadeDAO($this->dao->getConexao());
        $strFiltroUnidade = " AND (";
        $i = 0;
        $tamanho = count($listaDeUnidades) - 1;
        foreach ($listaDeUnidades as $idUnidade) {
            
            if ($i > 0 && $i < $tamanho) {
                $strFiltroUnidade .= " OR ";
                $strUnidade .= ', ';
            } else if ($i > 0) {
                $strFiltroUnidade .= " OR ";
                $strUnidade .= ' e ';
            }
            $strFiltroUnidade .= " catraca_unidade.unid_id = $idUnidade ";
            
            $unidade = new Unidade();
            $unidade->setId($idUnidade);
            $unidadeDao->preenchePorId($unidade);
            
            $strUnidade .= $unidade->getNome();
            $i ++;
        }
        $strFiltroUnidade .= ")";
        $dateStart = new DateTime($dateStart);
        $dateEnd = new DateTime($dataEnd);
        
        $dataInicial = $dateStart->format('Y-m-d') . ' 00:00:00';
        $dataFinal = $dateEnd->format('Y-m-d') . ' 23:59:59';
        
        
        $listaDeDatas = array();
        while ($dateStart <= $dateEnd) {
            $listaDeDatas[] = $dateStart->format('Y-m-d');
            $dateStart = $dateStart->modify('+1day');
        }
        
        $listaDeDados = array();
        $listaDeDadosTurno = array();
        
        foreach ($listaDeDatas as $data) {
            foreach ($tipos as $tipo) {
                $listaDeDados[$data][$tipo->getId()] = 0;
            }
            $listaDeDados[$data]['total'] = 0;
            foreach($listaDeTurnos as $turno){
                foreach ($tipos as $tipo) 
                {
                    $listaDeDadosTurno[$turno->getId()][$data][$tipo->getId()] = 0;
                }
                $listaDeDadosTurno[$turno->getId()][$data]['total'] = 0;
            }
        }
        
        
        $sql = "SELECT regi_valor_pago, regi_data, vinculo_tipo.tipo_id as tipo_id
         FROM registro
		INNER JOIN vinculo ON vinculo.vinc_id = registro.vinc_id
		INNER JOIN vinculo_tipo ON vinculo.vinc_id = vinculo_tipo.vinc_id
		INNER JOIN catraca ON registro.catr_id = catraca.catr_id
		INNER JOIN catraca_unidade ON catraca.catr_id = catraca_unidade.catr_id
		WHERE (regi_data BETWEEN '$dataInicial' AND '$dataFinal') 
		$strFiltroUnidade;";

		foreach($listaDeTurnos as $umTurno){
		    $umTurno->setHoraInicial(strtotime($umTurno->getHoraInicial()));
		    $umTurno->setHoraFinal(strtotime($umTurno->getHoraFinal()));
		}
		
        foreach ($dao->getConexao()->query($sql) as $linha) {
            
            $timeRegistro = strtotime(date("H:i:s", strtotime($linha['regi_data'])));
            
            foreach($listaDeTurnos as $umTurno){
                if($timeRegistro <= $umTurno->getHoraFinal() && $timeRegistro >$umTurno->getHoraInicial())
                {
                    $turnoDoRegistro = $umTurno;
                    break;
                }
            }
            $data = date('Y-m-d', strtotime($linha['regi_data']));
            $listaDeDados[$data][$linha['tipo_id']] += $linha['regi_valor_pago'];
            $listaDeDados[$data]['total'] += $linha['regi_valor_pago'];
            
            
            $listaDeDadosTurno[$turnoDoRegistro->getId()][$data][$linha['tipo_id']] += $linha['regi_valor_pago'];
            $listaDeDadosTurno[$turnoDoRegistro->getId()][$data]['total'] += $linha['regi_valor_pago'];
            
        }
        $titulos = array();
        $titulos[0] = "Relatorio de Arrecadação Diária";
        $titulos[1] = $strUnidade;
        $titulos[2] = 'De '. date ( 'd/m/Y', strtotime ( $dataInicial ) ) . ' a ' . date ( 'd/m/Y', strtotime ( $dataFinal) );
        $titulos[3] = "Todos os Turnos";
        
        
        
        if($_GET['gerar'] == 'Excel'){
            $dados = $this->view->geraStrCSV($listaDeDados, $titulos, $tipos, $listaDeDatas);
            foreach($listaDeTurnos as $turno){
                $dados .= "\n\n";
                $titulos[3] = $turno->getDescricao();
                $dados .= $this->view->geraStrCSV($listaDeDadosTurno[$turno->getId()], $titulos, $tipos, $listaDeDatas);
            }
            $dados = utf8_decode($dados);
            $nomeArquivo = "../tmp/relatorio".uniqid().".csv";
            if(fwrite($file=fopen($nomeArquivo,'w+'),$dados)) {
                
                
                header('Content-Description: File Transfer');
                header('Content-Disposition: attachment; filename="relatorio.csv"');
                header('Content-Type: application/octet-stream');
                header('Content-Transfer-Encoding: binary');
                header('Content-Length: ' . filesize($nomeArquivo));
                header('Cache-Control: must-revalidate, post-check=0, pre-check=0');
                header('Pragma: public');
                header('Expires: 0');
                fclose($file);
                readfile($nomeArquivo);
                
                unlink($nomeArquivo);
                
            }
            
        }else{
            $this->view->mostraListaDeDados($listaDeDados, $titulos, $tipos, $listaDeDatas);
            foreach($listaDeTurnos as $turno){
                $titulos[2] = 'De '. date ( 'd/m/Y', strtotime ( $dataInicial ) ) . ' a ' . date ( 'd/m/Y', strtotime ( $dataFinal) );
                $titulos[3] = 'Turno: '.$turno->getDescricao();
                $this->view->mostraListaDeDados($listaDeDadosTurno[$turno->getId()], $titulos, $tipos, $listaDeDatas);
            }
            
        }
        
        
    }
}

?>