package br.edu.unilab.catraca.view;

import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import java.awt.SystemColor;
import java.awt.Toolkit;
import javax.swing.JTable;
import javax.swing.JLabel;
import javax.swing.ImageIcon;
import java.awt.Color;
import java.awt.Font;

public class CatracaVirtualView extends JFrame {

	private JPanel contentPane;
	private JTable table;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					CatracaVirtualView frame = new CatracaVirtualView();
					frame.setVisible(true);
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
		Toolkit tk = Toolkit.getDefaultToolkit();
	    Dimension d = tk.getScreenSize();
	   
		setUndecorated(true);
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
		labelLogoUnilab.setIcon(new ImageIcon("C:\\projetos\\merge_alan_20_10_16\\catracas\\java\\catraca_virtual\\catraca_virtual\\src\\main\\resources\\images\\logo-unilab-branco.png"));
		labelLogoUnilab.setBounds(d.width-253, 11, 253, 105);
		panel.add(labelLogoUnilab);
		
		JLabel labelLogoDti = new JLabel("");
		labelLogoDti.setIcon(new ImageIcon("C:\\projetos\\merge_alan_20_10_16\\catracas\\java\\catraca_virtual\\catraca_virtual\\src\\main\\resources\\images\\logo_h-site.png"));
		labelLogoDti.setBounds(41, 30, 288, 62);
		panel.add(labelLogoDti);
		
		JLabel labelTitulo = new JLabel("<html><body><center>CATRACA <br/> Controle Administrativo de Tráfego Acadêmico Automatizado</center></body></html>");
		labelTitulo.setFont(new Font("Tahoma", Font.PLAIN, 18));
		labelTitulo.setForeground(Color.WHITE);
		
		labelTitulo.setBounds(d.width/2-488/2, 53, 488, 46);
		panel.add(labelTitulo);
		
		JPanel panel_1 = new JPanel();
		panel_1.setBackground(Color.WHITE);
		panel_1.setBounds(0, 190, d.width, 680);
		contentPane.add(panel_1);
		
		
	}
}
