package br.edu.unilab.catraca.view;

import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.EventQueue;
import java.awt.Toolkit;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

public class FrameOnlineView extends JFrame {

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					FrameOnlineView frame = new FrameOnlineView();
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
	public FrameOnlineView() {
		Toolkit toolkit = Toolkit.getDefaultToolkit();
		Dimension tamanhoTela = toolkit.getScreenSize();
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setUndecorated(true);
		setBounds((int)tamanhoTela.getWidth()-200, 30, 200, 100);
		
		
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JButton btnCatracaOffline = new JButton("Catraca Offline");
		btnCatracaOffline.setBounds(10, 37, 160, 23);
		contentPane.add(btnCatracaOffline);
	}
}
