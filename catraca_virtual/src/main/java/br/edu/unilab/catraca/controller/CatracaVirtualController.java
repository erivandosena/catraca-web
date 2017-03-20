package br.edu.unilab.catraca.controller;

import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.net.UnknownHostException;
import java.sql.Connection;
import java.sql.SQLException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.concurrent.Semaphore;

import javax.swing.JFrame;

import br.edu.unilab.catraca.controller.recurso.CartaoRecurso;
import br.edu.unilab.catraca.controller.recurso.CatracaRecurso;
import br.edu.unilab.catraca.controller.recurso.CatracaUnidadeRecurso;
import br.edu.unilab.catraca.controller.recurso.CustoUnidadeRecurso;
import br.edu.unilab.catraca.controller.recurso.RegistroRecurso;
import br.edu.unilab.catraca.controller.recurso.TipoRecurso;
import br.edu.unilab.catraca.controller.recurso.TurnoRecurso;
import br.edu.unilab.catraca.controller.recurso.TurnoUnidadeRecurso;
import br.edu.unilab.catraca.controller.recurso.UnidadeRecurso;
import br.edu.unilab.catraca.controller.recurso.UsuarioRecurso;
import br.edu.unilab.catraca.controller.recurso.VinculoRecurso;
import br.edu.unilab.catraca.dao.CatracaDAO;
import br.edu.unilab.catraca.dao.CatracaVirtualDAO;
import br.edu.unilab.catraca.dao.TipoDAO;
import br.edu.unilab.catraca.dao.UsuarioDAO;
import br.edu.unilab.catraca.dao.VinculoDAO;
import br.edu.unilab.catraca.view.CatracaVirtualView;
import br.edu.unilab.catraca.view.FrameSplash;
import br.edu.unilab.catraca.view.LoginView;
import br.edu.unilab.unicafe.model.Catraca;
import br.edu.unilab.unicafe.model.Registro;
import br.edu.unilab.unicafe.model.Tipo;
import br.edu.unilab.unicafe.model.Turno;
import br.edu.unilab.unicafe.model.Unidade;
import br.edu.unilab.unicafe.model.Usuario;
import br.edu.unilab.unicafe.model.Vinculo;

public class CatracaVirtualController {
	
	private LoginView frameLogin;
	private CatracaVirtualView frameCatracaVirtual;
	private Catraca catracaVirtual;
	private CatracaDAO dao;
	private double custo;
	private ArrayList<Turno>turnos;
	private Turno turnoAtual;
	private boolean turnoAtivo;
	private Unidade unidade;
	private FrameSplash splash;
	private Usuario operador;
	private Semaphore semaforo;
	ArrayList<Tipo> listaTipos;
	
	public CatracaVirtualController(){
		
		turnoAtivo = false;
		vinculoSelecionado = false;
		semaforo = new Semaphore(1);
		
	}
	
	public void iniciar(){
		
		this.splash = new FrameSplash();
		splash.setVisible(true);
		
		this.catracaVirtual = new Catraca();
		this.dao = new CatracaDAO();
		
		
		this.frameLogin = new LoginView();
		this.frameLogin.getLabelMensagem().setText("Aguarde a Sincronização dos Dados");
		this.frameLogin.setExtendedState(JFrame.MAXIMIZED_BOTH);
		try {
			
			this.catracaVirtual.maquinaLocal();
			
		} catch (UnknownHostException e) {
			System.out.println("Impossivel determinar nome da maquina. ");
			e.printStackTrace();
			return;
		}
		
		this.sincronizacaoBasica();
		
		splash.setVisible(false);
		this.frameLogin.setVisible(true);
		
		
		this.verificarNomeDaCatraca();
		this.verificarUnidadeDaCatraca();
		this.verificarTurnosDaCatraca();
		try {
			this.dao.getConexao().close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		this.adicionarEventosDeLogin();
		
	}
	public void adicionarEventosDeLogin(){
		getFrameLogin().getSenha().addKeyListener(new KeyAdapter() {
			@Override
			public void keyPressed(KeyEvent e) {
				if(e.getKeyCode() == KeyEvent.VK_ENTER){
					tentarLogar();
				}
			}
		});
		
		getFrameLogin().getBtnEntrar().addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				tentarLogar();
			}
		});
		
		
	}
	public void adicionarEventoConfirmar(){
		getFrameCatracaVirtual().getBtnConfirmar().addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				if(vinculoSelecionado){
					vinculoSelecionado = false;
					Registro registro = new Registro();
					registro.setCatraca(catracaVirtual);
					registro.setCartao(vinculoConsultado.getCartao());
					registro.setValorCusto(custo);
					registro.setVinculo(vinculoConsultado);
					registro.setValorPago(vinculoConsultado.getCartao().getTipo().getValorCobrado());
					CatracaVirtualDAO catracaVirtualDao = new CatracaVirtualDAO();
					if(catracaVirtualDao.inserirRegistro(registro)){
						mensagemSucesso("Inserido com sucesso!");
					}else{
						mensagemSucesso("Erro ao tentar inserir dados, tente novamente. ");
					}
					
					int tamanho = listaTipos.size();
					String colunas[] = new String[tamanho+3];
					colunas[0] = "Catraca Virtual";
					String dados[][] = new String[1][tamanho+3];
					int i = 1;
					int somatorio = 0;
					int valor = 0;
					for (Tipo tipo : listaTipos) {
						valor = catracaVirtualDao.totalGiroTurnoAtualNaoIsento(catracaVirtual, tipo, turnoAtual);
						frameCatracaVirtual.getDados()[0][i] = ""+valor;
						somatorio += valor;
						i++;
					}	
					frameCatracaVirtual.getDados()[0][i] = ""+catracaVirtualDao.totalGiroTurnoAtualIsento(catracaVirtual, turnoAtual);
					frameCatracaVirtual.getDados()[0][i+1] = ""+somatorio;
					colunas[i] = "Isento";
					colunas[i+1] = "Total";
					frameCatracaVirtual.getTabela().updateUI();
					
					try {
						catracaVirtualDao.getConexao().close();
					} catch (SQLException e1) {
						// TODO Auto-generated catch block
						e1.printStackTrace();
					}
				}
			}
		});
	}
	
	public void adicionarEventosCartao(){
		getFrameCatracaVirtual().getNumeroCartao().addKeyListener(new KeyAdapter() {
			@Override
			public void keyPressed(KeyEvent e) {
				if(e.getKeyCode() == KeyEvent.VK_ENTER){
					String numero = getFrameCatracaVirtual().getNumeroCartao().getText();
					getFrameCatracaVirtual().getNumeroCartao().setText("");
					if(turnoAtivo){
						passarCartao(numero);
					}else{
						erroForaDoTurno();
					}
					
				}
			}
		});
				
	}
	
	
	public Vinculo vinculoConsultado;
	public boolean vinculoSelecionado;
	
	
	public void passarCartao(final String numero){
		Thread passando = new Thread(new Runnable() {
			
			@Override
			public void run() {
				getFrameCatracaVirtual().getNumeroCartao().setEnabled(false);
				CatracaVirtualDAO catracaVirtualDAO = new CatracaVirtualDAO();
				vinculoConsultado = new Vinculo();
				vinculoConsultado.getCartao().setNumero(numero);
				if(catracaVirtualDAO.verificaVinculo(vinculoConsultado)){
					
					if(!catracaVirtualDAO.podeContinuarComendo(vinculoConsultado, turnoAtual)){
						mensagemSucesso("Usuário já passou neste turno!");
						return;
					}
					
					try {
						catracaVirtualDAO.getConexao().close();
					} catch (SQLException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					vinculoSelecionado = true;
					
					getFrameCatracaVirtual().getNomeUsuario().setText(vinculoConsultado.getResponsavel().getNome());
					getFrameCatracaVirtual().getTipoUsuario().setText(vinculoConsultado.getCartao().getTipo().getNome());
					getFrameCatracaVirtual().getValorCobrado().setText(""+vinculoConsultado.getCartao().getTipo().getValorCobrado());
					getFrameCatracaVirtual().getRefeicoesRestantes().setText(""+vinculoConsultado.getRefeicoesRestantes());
					getFrameCatracaVirtual().getPanel_3().setVisible(true);	
					
					
				}
				else{
					getFrameCatracaVirtual().getLblErro().setText("Sem Vinculo Valido");
					getFrameCatracaVirtual().getPanelErro().setVisible(true);
				}
				
				try {
					Thread.sleep(3000);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
				vinculoSelecionado = false;
				
				getFrameCatracaVirtual().getPanel_3().setVisible(false);
				getFrameCatracaVirtual().getPanelErro().setVisible(false);
				getFrameCatracaVirtual().getNumeroCartao().setEnabled(true);
				getFrameCatracaVirtual().getNumeroCartao().grabFocus();
				
			}
		});
		passando.start();
	}
	public void erroForaDoTurno(){
		Thread mostrar = new Thread(new Runnable() {
			
			@Override
			public void run() {
				getFrameCatracaVirtual().getLblErro().setText("Fora do horário de atendimento. ");
				getFrameCatracaVirtual().getPanelErro().setVisible(true);
				try {
					Thread.sleep(3000);
				} catch (InterruptedException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
				getFrameCatracaVirtual().getPanelErro().setVisible(false);
			}
		});
		mostrar.start();
	}
	
	public void mensagemSucesso(final String mensagem){
		Thread mostrar = new Thread(new Runnable() {
			
			@Override
			public void run() {
				getFrameCatracaVirtual().getPanel_3().setVisible(false);
				getFrameCatracaVirtual().getLblErro().setText(mensagem);
				getFrameCatracaVirtual().getPanelErro().setVisible(true);


				try {
					Thread.sleep(3000);
				} catch (InterruptedException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
				getFrameCatracaVirtual().getPanelErro().setVisible(false);
				getFrameCatracaVirtual().getNumeroCartao().setEnabled(true);
				getFrameCatracaVirtual().getNumeroCartao().grabFocus();
			}
		});
		mostrar.start();
	}
	
	public void erroJaPassou(){
		Thread mostrar = new Thread(new Runnable() {
			
			@Override
			public void run() {
				getFrameCatracaVirtual().getLblErro().setText("Ja comemeu. ");
				getFrameCatracaVirtual().getPanelErro().setVisible(true);
				try {
					Thread.sleep(3000);
				} catch (InterruptedException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
				getFrameCatracaVirtual().getPanelErro().setVisible(false);
			}
		});
		mostrar.start();
	}
	public void tentarLogar(){
		@SuppressWarnings("deprecation")
		String senha = UsuarioDAO.getMD5(getFrameLogin().getSenha().getText());
		this.operador = new Usuario();
		this.operador.setLogin(getFrameLogin().getLogin().getText().toLowerCase().trim());
		this.operador.setSenha(senha);
		UsuarioDAO usuarioDao = new UsuarioDAO();
		this.getFrameLogin().getLogin().setText("");
		this.getFrameLogin().getSenha().setText("");
		
		
		
		if(usuarioDao.autentica(this.operador))
		{
			try {
				usuarioDao.getConexao().close();
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			this.iniciarCatracaVirtual();
		}
		else
		{
			this.getFrameLogin().getLabelMensagem().setText("Errou login ou senha");
			try {
				usuarioDao.getConexao().close();
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
	}
	
	public void verificandoTurnoAtual(){
		Thread verificando = new Thread(new Runnable() {
			
			@Override
			public void run() {
				while(true){

					try {
						Thread.sleep(1000);
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					
					Date horaAtual = new Date();
					SimpleDateFormat dataNoFrame = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
					getFrameCatracaVirtual().getLabelDataHora().setText(dataNoFrame.format(horaAtual));
					
					
					if(turnoAtivo){
						
						Turno turno = turnoAtual;
						String horaInicial = turno.getHoraInicial();
						String horaFinal = turno.getHoraFinal();
						
						Date dateHoraInicial = null;
						Date dateHoraFinal = null;
						SimpleDateFormat format = new SimpleDateFormat("HH:mm:ss");
						format.setLenient(false);
						try {
							dateHoraFinal = format.parse(horaFinal);
							dateHoraInicial = format.parse(horaInicial);
						} catch (ParseException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						}
						Calendar calendarAtual = Calendar.getInstance();
						
						calendarAtual.setTime(horaAtual);
						int hourAtual = calendarAtual.get(Calendar.HOUR_OF_DAY);
						int minuteAtual = calendarAtual.get(Calendar.MINUTE);
						
						
						Calendar calendarInicioTurno = Calendar.getInstance();
						calendarInicioTurno.setTime(dateHoraInicial);
						int hourInicioTurno = calendarInicioTurno.get(Calendar.HOUR_OF_DAY);
						int minuteInicioTurno = calendarInicioTurno.get(Calendar.MINUTE);
						
						
						Calendar calendarFimTurno = Calendar.getInstance();
						calendarFimTurno.setTime(dateHoraFinal);
						int hourFimTurno = calendarFimTurno.get(Calendar.HOUR_OF_DAY);
						int minuteFimTurno = calendarFimTurno.get(Calendar.MINUTE);
						
						
						if(hourAtual >= hourInicioTurno && hourAtual <= hourFimTurno){
							if(hourAtual == hourInicioTurno && minuteAtual >= minuteInicioTurno){
								continue;
								
							}
							else if(hourAtual > hourInicioTurno && hourAtual < hourFimTurno){
								continue;
								
							}else if(hourAtual >= hourInicioTurno && hourAtual == hourFimTurno && minuteAtual <= minuteFimTurno){
								continue;
							}else{
								getFrameCatracaVirtual().getLabelTurno().setText("Turno "+turno.getDescricao()+"  finalizado. ");
								turnoAtivo = false;
							}
						}else{
							getFrameCatracaVirtual().getLabelTurno().setText("Turno "+turno.getDescricao()+"  finalizado. ");
							turnoAtivo = false;
							
						}
						
						continue;
					}
					for(Turno turno : turnos){
						String horaInicial = turno.getHoraInicial();
						String horaFinal = turno.getHoraFinal();
						
						Date dateHoraInicial = null;
						Date dateHoraFinal = null;
						SimpleDateFormat format = new SimpleDateFormat("HH:mm:ss");
						format.setLenient(false);
						try {
							dateHoraFinal = format.parse(horaFinal);
							dateHoraInicial = format.parse(horaInicial);
						} catch (ParseException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						}
						Calendar calendarAtual = Calendar.getInstance();
						
						calendarAtual.setTime(horaAtual);
						int hourAtual = calendarAtual.get(Calendar.HOUR_OF_DAY);
						int minuteAtual = calendarAtual.get(Calendar.MINUTE);
						
						
						Calendar calendarInicioTurno = Calendar.getInstance();
						calendarInicioTurno.setTime(dateHoraInicial);
						int hourInicioTurno = calendarInicioTurno.get(Calendar.HOUR_OF_DAY);
						int minuteInicioTurno = calendarInicioTurno.get(Calendar.MINUTE);
						
						
						Calendar calendarFimTurno = Calendar.getInstance();
						calendarFimTurno.setTime(dateHoraFinal);
						int hourFimTurno = calendarFimTurno.get(Calendar.HOUR_OF_DAY);
						int minuteFimTurno = calendarFimTurno.get(Calendar.MINUTE);
						
						
						if(hourAtual >= hourInicioTurno && hourAtual <= hourFimTurno){
							if(hourAtual == hourInicioTurno && minuteAtual >= minuteInicioTurno){
								getFrameCatracaVirtual().getLabelTurno().setText("Turno "+turno.getDescricao()+" iniciado");
								turnoAtual = turno;
								turnoAtivo = true;
								continue;
								
							}
							else if(hourAtual > hourInicioTurno && hourAtual < hourFimTurno){
								getFrameCatracaVirtual().getLabelTurno().setText("Turno "+turno.getDescricao()+" iniciado");
								turnoAtual = turno;
								turnoAtivo = true;
								continue;
								
							}else if(hourAtual >= hourInicioTurno && hourAtual == hourFimTurno && minuteAtual <= minuteFimTurno){
								getFrameCatracaVirtual().getLabelTurno().setText("Turno "+turno.getDescricao()+" iniciado");
								turnoAtual = turno;
								turnoAtivo = true;
								continue;
							}
						}
					}
				}
				
			}
		});
		verificando.start();
		
	}

	public void iniciarCatracaVirtual(){
		TipoDAO tipoDao = new TipoDAO();
		
		CatracaVirtualDAO catracaVirtualDAO = new CatracaVirtualDAO(tipoDao.getConexao());
		custo = catracaVirtualDAO.custo(catracaVirtual);
		this.verificandoTurnoAtual();
		listaTipos = tipoDao.lista();
		int tamanho = listaTipos.size();
		String colunas[] = new String[tamanho+3];
		colunas[0] = "Catraca Virtual";
		String dados[][] = new String[1][tamanho+3];
		int i = 1;
		for (Tipo tipo : listaTipos) {
			colunas[i] = tipo.getNome();
			dados[0][i] = "0";

			i++;
		}	
		dados[0][i] = "0";
		dados[0][i+1] = "0";
		colunas[i] = "Isento";
		colunas[i+1] = "Total";
		try {
			tipoDao.getConexao().close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		this.frameCatracaVirtual = new CatracaVirtualView(colunas, dados);
		this.frameCatracaVirtual.getNumeroCartao().setFocusable(true);
		
		this.frameCatracaVirtual.setFinanceiroAtivo(this.catracaVirtual.isFinanceiroAtivo());
		
		this.frameCatracaVirtual.getDados()[0][0] = this.catracaVirtual.getNome();
		this.frameCatracaVirtual.getTabela().updateUI();
		
		this.frameCatracaVirtual.getNomeUsuario().setText("");
		this.frameCatracaVirtual.getTipoUsuario().setText("");
		this.frameCatracaVirtual.getRefeicoesRestantes().setText("");
		this.frameCatracaVirtual.getValorCobrado().setText("");
		
		this.frameCatracaVirtual.getTabela().updateUI();

		
		this.getFrameLogin().setVisible(false);
		
		this.getFrameCatracaVirtual().setVisible(true);
		
		getFrameCatracaVirtual().getLabelTurno().setText(" Turno Inativo ");
		getFrameCatracaVirtual().getNumeroCartao().grabFocus();
		getFrameCatracaVirtual().getPanel_3().setVisible(false);
		getFrameCatracaVirtual().getPanelErro().setVisible(false);
		this.adicionarEventosCartao();
		this.verificandoTurnoAtual();
		
		adicionarEventoConfirmar();
		
	}
	
	public void sincronizacaoBasica(){
//		
//
//		try {
//			semaforo.acquire();
//			
//			UnidadeRecurso unidadeRecurso = new UnidadeRecurso();
//			unidadeRecurso.sincronizar(dao.getConexao());
//
//			CatracaRecurso catracaRecurso = new CatracaRecurso();
//			catracaRecurso.sincronizar(dao.getConexao());
//			
//			TipoRecurso tipoRecurso = new TipoRecurso();
//			tipoRecurso.sincronizar(dao.getConexao());
//					
//			TurnoRecurso turnoRecurso = new TurnoRecurso();
//			turnoRecurso.sincronizar(dao.getConexao());
//			
//			TurnoUnidadeRecurso turnoUnidade = new TurnoUnidadeRecurso();
//			turnoUnidade.sincronizar(dao.getConexao());
//
//			CartaoRecurso cartaoRecurso = new CartaoRecurso();
//			cartaoRecurso.sincronizar(dao.getConexao());
//			
//			UsuarioRecurso usuarioRecurso = new UsuarioRecurso();
//			usuarioRecurso.sincronizar();
//			
//			VinculoRecurso vinculoRecurso = new VinculoRecurso();
//			vinculoRecurso.sincronizar(dao.getConexao());
//			
//			CatracaUnidadeRecurso catracaUnidadeRecurso = new CatracaUnidadeRecurso();
//			catracaUnidadeRecurso.sincronizar(dao.getConexao());
//
//			CustoUnidadeRecurso custoRecurso = new CustoUnidadeRecurso();
//			custoRecurso.sincronizar(dao.getConexao());
//			
//			semaforo.release();
//			System.out.println("Sincronizacao Feita. ");
//		} catch (InterruptedException e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		}

		
		
		
	}
	public void verificarNomeDaCatraca(){
		boolean passou = false;
		do{
			if(this.dao.retornaCatracaPorNome(this.catracaVirtual) == null){
				this.frameLogin.getLabelMensagem().setText("Cadastre a catraca virtual");
				try {
					Thread.sleep(2000);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				
				CatracaRecurso catracaRecurso = new CatracaRecurso();
				catracaRecurso.sincronizar(this.dao.getConexao());
			}else{
				passou = true;
				this.frameLogin.getLabelMensagem().setText("Catraca Virtual: "+catracaVirtual.getNome());
				
			}	
		}while(!passou);
	}
	public void verificarUnidadeDaCatraca(){
		boolean passou = false;
		do{
			this.unidade = this.dao.unidadeDaCatraca(this.catracaVirtual);
			if(this.unidade == null){
				this.frameLogin.getLabelMensagem().setText("Cadastre a catraca em alguma unidade academica");
				try {
					Thread.sleep(2000);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}

				UnidadeRecurso unidadeRecurso = new UnidadeRecurso();
				unidadeRecurso.sincronizar(this.dao.getConexao());
				CatracaUnidadeRecurso recurso = new CatracaUnidadeRecurso();
				recurso.sincronizar(this.dao.getConexao());
			}else{
				this.frameLogin.getLabelMensagem().setText("Unidade: "+unidade.getNome());
				passou = true;
			}
		}while(!passou);
	}
	public void verificarTurnosDaCatraca(){
		boolean passou = false;
		do{
			this.turnos = this.dao.turnosDaUnidade(this.unidade);
			if(this.turnos == null || this.turnos.size() == 0){
				this.frameLogin.getLabelMensagem().setText("Adicione turnos na Unidade Academica");
				try {
					Thread.sleep(2000);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				TurnoUnidadeRecurso recurso = new TurnoUnidadeRecurso();
				recurso.sincronizar(this.dao.getConexao());
			}else{
				this.frameLogin.getLabelMensagem().setText("");
				passou = true;
			}
			
		}while(!passou);
	}
	
	
	public LoginView getFrameLogin() {
		return frameLogin;
	}
	public CatracaVirtualView getFrameCatracaVirtual() {
		return frameCatracaVirtual;
	}
	
	
}
