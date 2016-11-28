package br.edu.unilab.catraca.view;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.EventQueue;
import java.awt.Toolkit;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JLabel;
import javax.swing.GrayFilter;
import javax.swing.ImageIcon;
import javax.swing.border.LineBorder;
import java.awt.Font;
import java.awt.GradientPaint;
import java.awt.Graphics;
import java.awt.Graphics2D;

import javax.swing.SwingConstants;
import javax.swing.JTextField;
import javax.swing.JPasswordField;
import javax.swing.JButton;
import javax.swing.JComponent;

public class LoginView extends JFrame {

	private JPanel contentPane;
	private JTextField login;
	private JPasswordField senha;
	private JButton btnEntrar;
	private JLabel labelMensagem;
	
	
	public JLabel getLabelMensagem(){
		return this.labelMensagem;
	}
	
	public JTextField getLogin() {
		return login;
	}

	public void setLogin(JTextField login) {
		this.login = login;
	}

	public JPasswordField getSenha() {
		return senha;
	}

	public void setSenha(JPasswordField senha) {
		this.senha = senha;
	}

	public JButton getBtnEntrar() {
		return btnEntrar;
	}

	public void setBtnEntrar(JButton btnEntrar) {
		this.btnEntrar = btnEntrar;
	}

	/**
	 * Launch the application.
	 */
	
	
	public LoginView() {
		setResizable(false);
		
		Toolkit tk = Toolkit.getDefaultToolkit();
	    Dimension d = tk.getScreenSize();
	    setExtendedState(JFrame.MAXIMIZED_BOTH);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, d.width,  d.height);
		contentPane = new JPanel();
		contentPane.setUI(new PanelFormUICinza());
		setContentPane(contentPane);
		
		//contentPane.setBackground(new Color(2, 77, 209));
		contentPane.setLayout(null);
		
		JPanel panel = new JPanel();
		panel.setBackground(Color.WHITE);
		panel.setBounds(770, 385, 380, 297);
		panel.setBorder(new LineBorder(new Color(0, 0, 0), 2, true));		
		contentPane.add(panel);
		panel.setLayout(null);
		
		labelMensagem = new JLabel("Usuário ou Senha Inválido");
		labelMensagem.setHorizontalAlignment(SwingConstants.CENTER);
		labelMensagem.setBounds(10, 243, 360, 38);
		labelMensagem.setBorder(new LineBorder(new Color(192, 192, 192)));
		panel.add(labelMensagem);
		
		JLabel lblUsuario = new JLabel("Usuario");
		lblUsuario.setFont(new Font("Tahoma", Font.PLAIN, 18));
		lblUsuario.setBounds(10, 74, 72, 28);
		panel.add(lblUsuario);
		
		JLabel lblSenha = new JLabel("Senha");
		lblSenha.setFont(new Font("Tahoma", Font.PLAIN, 18));
		lblSenha.setBounds(10, 138, 72, 28);
		panel.add(lblSenha);
		
		login = new JTextField();
		login.setFont(new Font("Tahoma", Font.PLAIN, 18));
		login.setBounds(10, 99, 360, 28);
		login.setBorder(new LineBorder(new Color(192, 192, 192)));		
		panel.add(login);
		login.setColumns(10);
		
		senha = new JPasswordField();
		senha.setBounds(10, 165, 360, 28);
		senha.setBorder(new LineBorder(new Color(192, 192, 192)));
		panel.add(senha);
		
		JLabel lblNewLabel_3 = new JLabel("Login");
		lblNewLabel_3.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel_3.setFont(new Font("Tahoma", Font.PLAIN, 22));
		lblNewLabel_3.setBounds(0, 0, 380, 43);
		lblNewLabel_3.setOpaque(true);
		lblNewLabel_3.setBackground(new Color(63, 162, 219, 100));
		panel.add(lblNewLabel_3);
		
		btnEntrar = new JButton("Entrar");
		btnEntrar.setFont(new Font("Tahoma", Font.PLAIN, 18));
		btnEntrar.setBounds(10, 204, 360, 28);
		panel.add(btnEntrar);
		
		JPanel panel_1 = new JPanel();
		panel_1.setBounds(0, 306, d.width, 68);
		panel_1.setBackground(new Color(0, 0, 0, 100));
		contentPane.add(panel_1);
		panel_1.setLayout(null);
		
		JLabel lblTitulo = new JLabel("<html><body><center>Controle Administrativo de Tráfego Acadêmico Automatizado</center></body></html>");
		lblTitulo.setForeground(Color.WHITE);
		lblTitulo.setBounds((d.width-589)/2, 15, 589, 37);
		panel_1.add(lblTitulo);
		lblTitulo.setHorizontalAlignment(SwingConstants.CENTER);
		lblTitulo.setFont(new Font("Tahoma", Font.PLAIN, 22));		
		
		JLabel lblNewLabel_2 = new JLabel("");
		
		lblNewLabel_2.setIcon(new ImageIcon(this.getClass().getResource("/images/logoUnilabVertical.png")));
		lblNewLabel_2.setBounds((d.width-306)/2, 22, 306, 284);
		contentPane.add(lblNewLabel_2);
		
		
		
		
		
	}
}
