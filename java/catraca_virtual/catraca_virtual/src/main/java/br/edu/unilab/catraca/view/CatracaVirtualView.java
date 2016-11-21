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

	public String dados[][] = new String[1][7];
	private JPanel contentPane;
	private JTable tabela;
	private JButton btnConfirmar;
	private JLabel nomeUsuario;
	private JLabel tipoUsuario;
	private JLabel refeicoesRestantes;
	private JLabel valorCobrado;
	private JTextField numeroCartao;
	private JLabel financeiro;
	private JLabel turnoAtivo;

	
	
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
		return financeiro;
	}
	public void setFinanceiro(JLabel financeiro) {
		this.financeiro = financeiro;
	}
	public JLabel getTurnoAtivo() {
		return turnoAtivo;
	}
	public void setTurnoAtivo(JLabel turnoAtivo) {
		this.turnoAtivo = turnoAtivo;
	}
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					CatracaVirtualView frame = new CatracaVirtualView();
					frame.setVisible(true);
					frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}	
	/**
	 * Create the frame.
	 */
	public CatracaVirtualView() {
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
		
		String[] colunas = {"Unidade", "Visitante","Terceirizado", "Servidor TAE","Servidor Docente", "Aluno", "Total"};
		this.dados[0][0] = "Liberdade";
		this.dados[0][1] = "2";
		this.dados[0][2] = "3";
		this.dados[0][3] = "4";
		this.dados[0][4] = "5";
		this.dados[0][5] = "6";
		this.dados[0][6] = "7";		
		
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
		
		tabela = new JTable(dados, colunas){
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
		
		financeiro = new JLabel("Modulo Financeiro Habilitado");
		financeiro.setOpaque(true);
		financeiro.setBackground(new Color(43, 186, 40));
		financeiro.setFont(new Font("Tahoma", Font.PLAIN, 16));
		financeiro.setForeground(new Color(255, 255, 255));
		financeiro.setHorizontalAlignment(SwingConstants.CENTER);
		financeiro.setBounds((panel_2.getWidth()-246)/2, 22, 246, 32);
		panel_2.add(financeiro);
		
		turnoAtivo = new JLabel("Turno Merenda Ativo");
		turnoAtivo.setHorizontalAlignment(SwingConstants.CENTER);
		turnoAtivo.setFont(new Font("Tahoma", Font.PLAIN, 16));
		turnoAtivo.setBounds(473, 22, 197, 32);
		panel_2.add(turnoAtivo);
		
		SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
		
		JLabel label = new JLabel(sdf.format(new Date()));
		label.setHorizontalAlignment(SwingConstants.CENTER);
		label.setFont(new Font("Tahoma", Font.PLAIN, 16));
		label.setBounds(10, 22, 197, 32);
		panel_2.add(label);
		
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
		
		JPanel panel_3 = new JPanel();
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

		
		
	}
}
