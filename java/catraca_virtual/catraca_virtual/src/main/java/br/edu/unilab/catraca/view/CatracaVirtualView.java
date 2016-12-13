package br.edu.unilab.catraca.view;

import java.awt.Dimension;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.border.Border;
import javax.swing.border.EmptyBorder;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.DefaultTableModel;

import java.awt.Toolkit;
import java.text.SimpleDateFormat;
import java.util.Date;

import javax.swing.JTable;
import javax.swing.JLabel;
import javax.swing.ImageIcon;
import java.awt.Color;
import java.awt.Component;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Insets;

import javax.swing.border.LineBorder;
import javax.swing.border.EtchedBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.ScrollPaneConstants;
import javax.swing.SwingConstants;

public class CatracaVirtualView extends JFrame {

	private String dados[][];
	public String[][] getDados() {
		return dados;
	}
	public void setDados(String[][] dados) {
		this.dados = dados;
	}
	private JPanel panel_3;
	public JPanel getPanel_3() {
		return panel_3;
	}
	public void setPanel_3(JPanel panel_3) {
		this.panel_3 = panel_3;
	}
	private JLabel lblErro;
	private JPanel panelErro; 
	private JPanel contentPane;
	private JTable tabela;
	private JButton btnConfirmar;
	private JLabel nomeUsuario;
	public JLabel getLblErro() {
		return lblErro;
	}
	public void setLblErro(JLabel lblErro) {
		this.lblErro = lblErro;
	}
	private JLabel tipoUsuario;
	private JLabel refeicoesRestantes;
	private JLabel valorCobrado;
	private JTextField numeroCartao;
	private JLabel labelDataHora;
	public JLabel getLabelDataHora() {
		return labelDataHora;
	}
	public void setLabelDataHora(JLabel labelDataHora) {
		this.labelDataHora = labelDataHora;
	}

	private JLabel labelFinanceiro;
	public void setFinanceiroAtivo(boolean financeiro){
		if(financeiro){
			this.labelFinanceiro.setText("Financeiro Habilitado");
			this.labelFinanceiro.setBackground(new Color(43, 186, 40));
		}else{
			this.labelFinanceiro.setBackground(new Color(255, 0, 0));
			this.labelFinanceiro.setText("Financeiro Desabilitado");
		}
	}
	
	public JLabel getLabelFinanceiro() {
		return labelFinanceiro;
	}
	public void setLabelFinanceiro(JLabel labelFinanceiro) {
		this.labelFinanceiro = labelFinanceiro;
	}
	public JLabel getLabelTurno() {
		return labelTurno;
	}
	public void setLabelTurno(JLabel labelTurno) {
		this.labelTurno = labelTurno;
	}

	private JLabel labelTurno;

	private String[] colunas = {"Unidade", "Teste","Terceirizado", "Servidor TAE","Servidor Docente", "Aluno", "Total"};
	
	public String[] getColunas() {
		return colunas;
	}
	public void setColunas(String[] colunas) {
		this.colunas = colunas;
	}
	public JTable getTabela() {
		return tabela;
	}
	public void setTabela(JTable tabela) {
		this.tabela = tabela;
	}
	public JButton getBtnConfirmar() {
		return btnConfirmar;
	}
	public void setBtnConfirmar(JButton btnConfirmar) {
		this.btnConfirmar = btnConfirmar;
	}
	public JLabel getNomeUsuario() {
		return nomeUsuario;
	}
	public void setNomeUsuario(JLabel nomeUsuario) {
		this.nomeUsuario = nomeUsuario;
	}
	public JLabel getTipoUsuario() {
		return tipoUsuario;
	}
	public void setTipoUsuario(JLabel tipoUsuario) {
		this.tipoUsuario = tipoUsuario;
	}
	public JLabel getRefeicoesRestantes() {
		return refeicoesRestantes;
	}
	public void setRefeicoesRestantes(JLabel refeicoesRestantes) {
		this.refeicoesRestantes = refeicoesRestantes;
	}
	public JLabel getValorCobrado() {
		return valorCobrado;
	}
	public void setValorCobrado(JLabel valorCobrado) {
		this.valorCobrado = valorCobrado;
	}
	public JTextField getNumeroCartao() {
		return numeroCartao;
	}
	public void setNumeroCartao(JTextField numeroCartao) {
		this.numeroCartao = numeroCartao;
	}
	public JLabel getFinanceiro() {
		return labelFinanceiro;
	}
	public void setFinanceiro(JLabel financeiro) {
		this.labelFinanceiro = financeiro;
	}
	public JLabel getTurnoAtivo() {
		return labelTurno;
	}
	public void setTurnoAtivo(JLabel turnoAtivo) {
		this.labelTurno = turnoAtivo;
	}
	
	public CatracaVirtualView(String colunas[], String dados[][]) {
		
		this.dados = dados;
		this.colunas = colunas;
		setResizable(false);
		Toolkit tk = Toolkit.getDefaultToolkit();
	    Dimension d = tk.getScreenSize();
	   
		//setUndecorated(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(0, 0, d.width,  d.height);
		contentPane = new JPanel();
		contentPane.setBackground(new Color(243, 243, 243));
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JPanel panel = new JPanel();
		panel.setBackground(new Color(63, 162, 219));
		panel.setBounds(0, 0, 1920, 127);
		contentPane.add(panel);
		panel.setLayout(null);
		
		JLabel labelLogoUnilab = new JLabel("");
		labelLogoUnilab.setIcon(new ImageIcon(this.getClass().getResource("/images/logo-unilab-branco.png")));
		labelLogoUnilab.setBounds(d.width-253, 11, 253, 105);
		panel.add(labelLogoUnilab);
		
		JLabel labelLogoDti = new JLabel("");
		labelLogoDti.setIcon(new ImageIcon(this.getClass().getResource("/images/logo_h-site.png")));
		labelLogoDti.setBounds(41, 30, 288, 62);
		panel.add(labelLogoDti);
		
		JLabel labelTitulo = new JLabel("<html><body><center>CATRACA <br/> Controle Administrativo de Tráfego Acadêmico Automatizado</center></body></html>");
		labelTitulo.setFont(new Font("Tahoma", Font.PLAIN, 18));
		labelTitulo.setForeground(Color.WHITE);
		
		labelTitulo.setBounds(d.width/2-488/2, 53, 488, 46);
		panel.add(labelTitulo);
		
		JPanel panel_1 = new JPanel();
		panel_1.setBorder(new EtchedBorder(EtchedBorder.LOWERED, Color.BLACK, Color.LIGHT_GRAY));
		panel_1.setBackground(Color.WHITE);
		panel_1.setBounds((d.width-997)/2, 198, 997, 561);
		contentPane.add(panel_1);
		panel_1.setLayout(null);
		
		JScrollPane jsp = new JScrollPane();
		jsp.setHorizontalScrollBarPolicy(ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
		jsp.setBounds((panel_1.getWidth()-680)/2, 125, 680, 78);
		panel_1.add(jsp);		
		
		
//		tabela = new JTable();
//		tabela.setFont(new Font("Tahoma", Font.PLAIN, 14));		
//		DefaultTableModel model = new DefaultTableModel(dados, colunas);		
//		tabela.setModel(model);		
		
		tabela = new JTable(this.dados, this.colunas){
			public boolean isCellEditable(int dados, int colunas){
				return false;
			}
		};
		tabela.setFont(new Font("Tahoma", Font.PLAIN, 12));
		jsp.setViewportView(tabela);
		tabela.setPreferredScrollableViewportSize(new Dimension(450, 40));
		tabela.setFillsViewportHeight(true);
		
		JPanel panel_2 = new JPanel();
		panel_2.setBackground(Color.WHITE);
		panel_2.setBorder(new LineBorder(Color.LIGHT_GRAY, 2));
		panel_2.setBounds((panel_1.getWidth()-680)/2, 33, 680, 71);
		panel_1.add(panel_2);
		panel_2.setLayout(null);
		
		labelFinanceiro = new JLabel("Modulo Financeiro Habilitado");
		labelFinanceiro.setOpaque(true);
		labelFinanceiro.setBackground(new Color(43, 186, 40));
		labelFinanceiro.setFont(new Font("Tahoma", Font.PLAIN, 16));
		labelFinanceiro.setForeground(new Color(255, 255, 255));
		labelFinanceiro.setHorizontalAlignment(SwingConstants.CENTER);
		labelFinanceiro.setBounds((panel_2.getWidth()-246)/2, 22, 246, 32);
		panel_2.add(labelFinanceiro);
		
		labelTurno = new JLabel("Turno Merenda Ativo");
		labelTurno.setHorizontalAlignment(SwingConstants.CENTER);
		labelTurno.setFont(new Font("Tahoma", Font.PLAIN, 16));
		labelTurno.setBounds(473, 22, 197, 32);
		panel_2.add(labelTurno);
		
		SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
		
		labelDataHora = new JLabel(sdf.format(new Date()));
		labelDataHora.setHorizontalAlignment(SwingConstants.CENTER);
		labelDataHora.setFont(new Font("Tahoma", Font.PLAIN, 16));
		labelDataHora.setBounds(10, 22, 197, 32);
		panel_2.add(labelDataHora);
		
		numeroCartao = new JTextField();
		
		numeroCartao.setFont(new Font("Tahoma", Font.PLAIN, 14));
		numeroCartao.setBounds(220, 237, 175, 22);
		numeroCartao.setBorder(new LineBorder(new Color(192, 192, 192)));
		numeroCartao.requestFocusInWindow();
		panel_1.add(numeroCartao);
		numeroCartao.setColumns(10);
		
		JLabel lblCarto = new JLabel("Cartão:");
		lblCarto.setFont(new Font("Tahoma", Font.PLAIN, 18));
		lblCarto.setBounds(158, 235, 113, 22);
		panel_1.add(lblCarto);
		
		panel_3 = new JPanel();
		panel_3.setBorder(new EtchedBorder(EtchedBorder.LOWERED, Color.LIGHT_GRAY, new Color(0, 0, 0)));
		panel_3.setBounds((panel_1.getWidth()-680)/2, 291, 680, 206);
		panel_1.add(panel_3);
		panel_3.setLayout(null);
		
		JLabel lblNome = new JLabel("Nome:");
		lblNome.setFont(new Font("Tahoma", Font.BOLD, 14));
		lblNome.setBounds(10, 23, 61, 23);
		panel_3.add(lblNome);
		
		JLabel lblTipo = new JLabel("Tipo:");
		lblTipo.setFont(new Font("Tahoma", Font.BOLD, 14));
		lblTipo.setBounds(10, 57, 61, 23);
		panel_3.add(lblTipo);
		
		JLabel lblRefeiesRestantes = new JLabel("Refeições Restantes:");
		lblRefeiesRestantes.setFont(new Font("Tahoma", Font.BOLD, 14));
		lblRefeiesRestantes.setBounds(10, 91, 159, 23);
		panel_3.add(lblRefeiesRestantes);
		
		JLabel lblValorCobrado = new JLabel("Valor Cobrado:");
		lblValorCobrado.setFont(new Font("Tahoma", Font.BOLD, 14));
		lblValorCobrado.setBounds(10, 125, 123, 23);
		panel_3.add(lblValorCobrado);
		
		btnConfirmar = new JButton("Confirmar");
		btnConfirmar.setForeground(Color.WHITE);
		btnConfirmar.setFont(new Font("Tahoma", Font.BOLD, 14));
		btnConfirmar.setBackground(new Color(43, 186, 40));
		btnConfirmar.setBounds(231, 162, 213, 33);
		panel_3.add(btnConfirmar);
		
		nomeUsuario = new JLabel("Alan Cleber Morais Gomes");
		nomeUsuario.setFont(new Font("Tahoma", Font.PLAIN, 14));
		nomeUsuario.setBounds(65, 27, 379, 14);
		panel_3.add(nomeUsuario);
		
		tipoUsuario = new JLabel("Servidor TAE");
		tipoUsuario.setFont(new Font("Tahoma", Font.PLAIN, 14));
		tipoUsuario.setBounds(54, 61, 379, 14);
		panel_3.add(tipoUsuario);
		
		refeicoesRestantes = new JLabel("1 Refeição");
		refeicoesRestantes.setFont(new Font("Tahoma", Font.PLAIN, 14));
		refeicoesRestantes.setBounds(167, 95, 379, 14);
		panel_3.add(refeicoesRestantes);
		
		valorCobrado = new JLabel("R$ 1,60");
		valorCobrado.setFont(new Font("Tahoma", Font.PLAIN, 14));
		valorCobrado.setBounds(129, 129, 379, 14);
		panel_3.add(valorCobrado);
		
		panelErro = new JPanel();
		panelErro.setBounds(158, 277, 680, 58);
		panel_1.add(panelErro);
		panelErro.setLayout(null);
		
		lblErro = new JLabel("Erro");
		lblErro.setBounds(121, 11, 451, 17);
		panelErro.add(lblErro);
		lblErro.setFont(new Font("Tahoma", Font.BOLD, 14));

		
		
	}
	public JPanel getPanelErro() {
		return panelErro;
	}
	public void setPanelErro(JPanel panelErro) {
		this.panelErro = panelErro;
	}
}
