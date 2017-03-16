package br.edu.unilab.catraca.view;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.EventQueue;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

public class FrameSplash extends JFrame {
	
	private static final long serialVersionUID = 1L;
	private JPanel contentPane;
	
	
	public FrameSplash() {
		setAlwaysOnTop(true);
		contentPane = new JPanel();
		contentPane.setBackground(Color.WHITE);
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setSize(800, 350);
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel label = new JLabel("");
		label.setIcon(new ImageIcon(this.getClass().getResource("/images/logo-unilab.png")));
		
		label.setBounds(100, 107, 600, 136);
		contentPane.add(label);
		setLocationRelativeTo(null);  
		setUndecorated(true);
		setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
		
	}
	
}
