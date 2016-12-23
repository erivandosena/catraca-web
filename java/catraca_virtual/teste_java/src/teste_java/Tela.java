package teste_java;

import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.ImageIcon;
import javax.swing.JTable;

public class Tela extends JFrame {

	private JPanel contentPane;
	private JTable table;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
//		int sb = 2;
		int sb = 9;
		String formatado = String.format("%02d", Integer.parseInt(sb+""));
		System.out.println(formatado);
		
	}
	

	public String dados[][] = new String[2][2];
	public String[] colunas = new String[2];
	/**
	 * Create the frame.
	 */
	public Tela() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		this.colunas[0] = "Teste";
		this.colunas[1] = "Teste2";
		
				
		this.dados[0][0] = "1";
		this.dados[0][1] = "1";
		this.dados[1][0] = "1";
		this.dados[1][1] = "2";
		
		
		
		table = new JTable(dados, colunas){
			public boolean isCellEditable(int dados, int colunas){
				return false;
			}
		};
		
		Thread trede = new Thread(new Runnable() {
			@Override
			public void run() {
				int i = 10;
				while(true){
					i++;
					try {
						table = new JTable(dados, colunas){
							public boolean isCellEditable(int dados, int colunas){
								return false;
							}
						};
						table.setPreferredScrollableViewportSize(new Dimension(450,63));
						table.setFillsViewportHeight(true);
						JScrollPane jsp = new JScrollPane(table);
						jsp.setBounds(10, 27, 241, 56);
						contentPane.add(jsp);
						Thread.sleep(1000);
						dados[0][1] = ""+i;
						colunas[1] = ""+i;
						table.updateUI();
						System.out.println("Teste");
						
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
			}
		});
		trede.start();
	}
}
