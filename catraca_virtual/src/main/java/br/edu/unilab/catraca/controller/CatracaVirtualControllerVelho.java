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

import br.edu.unilab.catraca.dao.CatracaDAO;
import br.edu.unilab.catraca.dao.CatracaVirtualDAO;
import br.edu.unilab.catraca.dao.TipoDAO;
import br.edu.unilab.catraca.dao.UsuarioDAO;
import br.edu.unilab.catraca.dao.VinculoDAO;
import br.edu.unilab.catraca.recurso.CartaoRecurso;
import br.edu.unilab.catraca.recurso.CatracaRecurso;
import br.edu.unilab.catraca.recurso.CatracaUnidadeRecurso;
import br.edu.unilab.catraca.recurso.CustoUnidadeRecurso;
import br.edu.unilab.catraca.recurso.RegistroRecurso;
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

public class CatracaVirtualControllerVelho {
	
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
		
		try {
			tipoDao.getConexao().close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
	

		
		this.getFrameLogin().setVisible(false);
		
		this.getFrameCatracaVirtual().setVisible(true);
		

		getFrameCatracaVirtual().getNumeroCartao().grabFocus();
		getFrameCatracaVirtual().getPanel_3().setVisible(false);
		getFrameCatracaVirtual().getPanelErro().setVisible(false);

		this.verificandoTurnoAtual();
		
		this.adicionarEventosCartao();
		adicionarEventoConfirmar();
		
	}
	
	public void sincronizacaoBasica(){
		
		
	}
	
	
	public LoginView getFrameLogin() {
		return frameLogin;
	}
	public CatracaVirtualView getFrameCatracaVirtual() {
		return frameCatracaVirtual;
	}
	
	
}
