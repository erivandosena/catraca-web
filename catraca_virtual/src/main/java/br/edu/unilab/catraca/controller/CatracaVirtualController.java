package br.edu.unilab.catraca.controller;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.sql.SQLException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;

import javax.swing.JFrame;

import br.edu.unilab.catraca.dao.CatracaDAO;
import br.edu.unilab.catraca.dao.CatracaVirtualDAO;
import br.edu.unilab.catraca.dao.DAO;
import br.edu.unilab.catraca.dao.TipoDAO;
import br.edu.unilab.catraca.dao.TurnoDAO;
import br.edu.unilab.catraca.dao.UsuarioDAO;
import br.edu.unilab.catraca.recurso.CartaoRecurso;
import br.edu.unilab.catraca.recurso.CatracaRecurso;
import br.edu.unilab.catraca.recurso.CatracaUnidadeRecurso;
import br.edu.unilab.catraca.recurso.CustoRefeicaoRecurso;
import br.edu.unilab.catraca.recurso.CustoUnidadeRecurso;
import br.edu.unilab.catraca.recurso.TipoRecurso;
import br.edu.unilab.catraca.recurso.TurnoRecurso;
import br.edu.unilab.catraca.recurso.TurnoUnidadeRecurso;
import br.edu.unilab.catraca.recurso.UnidadeRecurso;
import br.edu.unilab.catraca.recurso.UsuarioRecurso;
import br.edu.unilab.catraca.recurso.VinculoRecurso;
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
/**
 * 
 * @author Jefferson Uchoa Ponte
 *
 */
public class CatracaVirtualController {
	private ArrayList<Turno>turnos;
	private Turno turnoAtual;
	private boolean turnoAtivo;
	
	private LoginView frameLogin;

	private Catraca catracaVirtual;
	private CatracaDAO dao;
	private Unidade unidade;
	
	private Usuario operador;
	private double custo;
	
	private CatracaVirtualView frameCatracaVirtual;
	private ArrayList<Tipo> listaTipos;
	
	
	public Vinculo vinculoConsultado;
	public boolean vinculoSelecionado;
	
	
	public CatracaVirtualController(){
		this.turnoAtivo = false;
		this.catracaVirtual = new Catraca();
	}
	
	
	/**
	 * Este metodo criara um splash e deixará visível até que
	 *  consiga criar as janelas e eventos. 
	 * Ele dispara o metodo fazendoSincronia(), 
	 * Apos tudo feito, tornará o splash invisivel e 
	 * tornará a janela de login visivel. 
	 */
	public void iniciar(){
		FrameSplash splash = new FrameSplash();
		splash.setVisible(true);
		
		try {
			Thread.sleep(1000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		this.frameLogin = new LoginView();
		this.frameLogin.getLabelMensagem().setText("Aguardando informação da catraca.");
		this.frameLogin.setExtendedState(JFrame.MAXIMIZED_BOTH);
		splash.setVisible(false);
		this.frameLogin.setVisible(true);
		splash.dispose();
		this.catracaVirtual.maquinaLocal();
		this.verificarNomeDaCatraca();
		this.frameLogin.getLabelMensagem().setText("Aguardando informação da Unidade Acadêmica.");
		this.verificarUnidadeDaCatraca();
		this.frameLogin.getLabelMensagem().setText("Aguardando informação de Turnos.");
		this.verificarTurnosDaUnidade();
		this.frameLogin.getLabelMensagem().setText("Verificando Custo.");
		this.verificarCusto();
		this.frameLogin.getLabelMensagem().setText("Verificando tipos");
		this.verificaTipos();
		this.frameLogin.getLabelMensagem().setText("");
		
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
		
		this.frameCatracaVirtual = new CatracaVirtualView(colunas, dados);
		getFrameCatracaVirtual().getLabelTurno().setText(" Turno Inativo ");
		
		this.frameCatracaVirtual.getNumeroCartao().setFocusable(true);
		

		
		this.frameCatracaVirtual.setFinanceiroAtivo(this.catracaVirtual.isFinanceiroAtivo());
		
		this.frameCatracaVirtual.getDados()[0][0] = this.catracaVirtual.getNome();
		this.frameCatracaVirtual.getTabela().updateUI();
		
		this.frameCatracaVirtual.getNomeUsuario().setText("");
		this.frameCatracaVirtual.getTipoUsuario().setText("");
		this.frameCatracaVirtual.getRefeicoesRestantes().setText("");
		this.frameCatracaVirtual.getValorCobrado().setText("");
		
		this.frameCatracaVirtual.getTabela().updateUI();
		
		
		
		this.fazendoSincronia();
		
		this.adicionarEventosDeLogin();
		
		
		
	}
	
	
	
	private synchronized  void verificaTipos(){
		TipoDAO dao2 = new TipoDAO();
		do{
			this.listaTipos = dao2.lista();
			if(this.listaTipos.size() == 0){
				TipoRecurso tipoRecurso = new TipoRecurso();
				tipoRecurso.sincronizar(dao2.getConexao());
				
				try {
					Thread.sleep(2000);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				
				continue;
			}
			break;
		}while(true);
		try {
			dao2.getConexao().close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		
	}
	synchronized private void verificarCusto(){
		
		TipoDAO dao = new TipoDAO();
		
		

		do{
			CatracaVirtualDAO catracaVirtualDAO = new CatracaVirtualDAO(dao.getConexao());
			this.custo = catracaVirtualDAO.custo(catracaVirtual);
			if(this.custo == 0){
				CustoRefeicaoRecurso recurso = new CustoRefeicaoRecurso();
				recurso.sincronizar(dao.getConexao());
				CustoUnidadeRecurso recurso2 = new CustoUnidadeRecurso();
				recurso2.sincronizar(dao.getConexao());
				try {
					Thread.sleep(2000);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				
				
				continue;
			}
			break;
		}while(true);
		try {
			dao.getConexao().close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
	}
	
	synchronized private void verificarNomeDaCatraca(){
		boolean passou = false;
		this.dao = new CatracaDAO();
		do{
			if(this.dao.preencheCatracaPorNome(this.catracaVirtual) == false){
				this.frameLogin.getLabelMensagem().setText("Cadastre a catraca virtual "+this.catracaVirtual.getNome());
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
		try {
			this.dao.getConexao().close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	synchronized private void verificarUnidadeDaCatraca(){
		boolean passou = false;
		this.dao.novaConexao();
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
		try {
			this.dao.getConexao().close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	synchronized private void verificarTurnosDaUnidade(){
		boolean passou = false;
		this.dao.novaConexao();
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
				TurnoRecurso turnoRecurso = new TurnoRecurso();
				turnoRecurso.sincronizar(this.dao.getConexao());
				TurnoUnidadeRecurso recurso = new TurnoUnidadeRecurso();
				recurso.sincronizar(this.dao.getConexao());
			}else{
				this.frameLogin.getLabelMensagem().setText("");
				passou = true;
			}
			
		}while(!passou);
		try {
			this.dao.getConexao().close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	
	/**
	 * Só verificar condições de turno ativo para chamar o método que sincroniza. 
	 * Faz isso de minuto em minuto.     
	 */
	private void fazendoSincronia(){
		Thread sincronizando = new Thread(new Runnable() {
			
			@Override
			public void run() {
				do{
					try {
						//Vamos esperar um minuto e sincronizar de novo. 
						Thread.sleep(120000);
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					if(turnoAtivo){
						System.out.println("Fiz nada");
					}else{
						System.out.println("sincronizar");
						sincronizar();
					}
				}while(true);
				
			}
		});
		sincronizando.start();
		
	}
	
	private synchronized void sincronizar(){
		this.dao = new CatracaDAO();
		
		if(turnoAtivo){
			
			try {
				this.dao.getConexao().close();
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}	
			return;
		}
		this.frameLogin.getLabelMensagem().setText("Espere sincronização de usuarios.");
		UsuarioRecurso usuarioRecurso = new UsuarioRecurso();
		usuarioRecurso.sincronizar(this.dao.getConexao());
		
		
		
		if(turnoAtivo){
			try {
				this.dao.getConexao().close();
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			return;
		}
		this.frameLogin.getLabelMensagem().setText("Espere sincronização de cartões.");
		CartaoRecurso cartaoRecurso = new CartaoRecurso();
		cartaoRecurso.sincronizar(this.dao.getConexao());
		
		if(turnoAtivo){
			try {
				this.dao.getConexao().close();
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			return;
		}
		this.frameLogin.getLabelMensagem().setText("Espere sincronização de vínculos.");
		
		VinculoRecurso vinculoRecurso = new VinculoRecurso();
		vinculoRecurso.sincronizar(this.dao.getConexao());
		
		if(turnoAtivo){
			try {
				this.dao.getConexao().close();
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			return;
		}
		
		
		TurnoRecurso turnoRecurso = new TurnoRecurso();
		turnoRecurso.sincronizar(this.dao.getConexao());
		TurnoUnidadeRecurso recurso = new TurnoUnidadeRecurso();
		recurso.sincronizar(this.dao.getConexao());
		
		if(turnoAtivo){
			try {
				this.dao.getConexao().close();
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			return;
		}
		
		TipoRecurso tipoRecurso = new TipoRecurso();
		tipoRecurso.sincronizar(this.dao.getConexao());
		
		
		try {
			this.dao.getConexao().close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		this.frameLogin.getLabelMensagem().setText("Pode tentar logar.");
		
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
	
	public LoginView getFrameLogin(){
		return this.frameLogin;
	}
	
	private synchronized void tentarLogar(){
		this.operador = new Usuario();
		@SuppressWarnings("deprecation")
		String senha = UsuarioDAO.getMD5(getFrameLogin().getSenha().getText());
		this.operador.setLogin(getFrameLogin().getLogin().getText().toLowerCase().trim());
		this.operador.setSenha(senha);
		UsuarioDAO usuarioDao = new UsuarioDAO();
		this.getFrameLogin().getLogin().setText("");
		this.getFrameLogin().getSenha().setText("");
		
		
		
		if(usuarioDao.autentica(this.operador))
		{
			
			this.iniciarCatracaVirtual();
		}
		else
		{
			

			this.getFrameLogin().getLabelMensagem().setText("Errou login ou senha");

		}
		
		try {
			usuarioDao.getConexao().close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public void iniciarCatracaVirtual(){
		
		
		this.verificandoTurnoAtual();
		this.adicionarEventosCartao();
		adicionarEventoConfirmar();
				
		getFrameLogin().setVisible(false);
		getFrameCatracaVirtual().setVisible(true);
		getFrameCatracaVirtual().getNumeroCartao().grabFocus();
		getFrameCatracaVirtual().getPanel_3().setVisible(false);
		getFrameCatracaVirtual().getPanelErro().setVisible(false);
		
		
		
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

	public void adicionarEventosCartao(){
		getFrameCatracaVirtual().getNumeroCartao().addKeyListener(new KeyAdapter() {
			@Override
			public void keyPressed(KeyEvent e) {
				if(e.getKeyCode() == KeyEvent.VK_ENTER){
					String numero = getFrameCatracaVirtual().getNumeroCartao().getText();
					if(turnoAtivo){
						passarCartao(numero);
					}else{
						erroForaDoTurno();
					}
					
				}
			}
		});
				
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
		
	private synchronized void passarCartao(final String numero){
		Thread t = new Thread(new Runnable() {
			public void run() {
				getFrameCatracaVirtual().getNumeroCartao().setText("");
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
		
		t.start();

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
	
	public CatracaVirtualView getFrameCatracaVirtual() {
		return frameCatracaVirtual;
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
}
