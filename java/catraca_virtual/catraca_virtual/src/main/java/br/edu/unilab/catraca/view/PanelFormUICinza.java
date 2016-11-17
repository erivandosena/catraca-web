package br.edu.unilab.catraca.view;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.GradientPaint;
import java.awt.Graphics;
import java.awt.Graphics2D;

import javax.swing.JComponent;
import javax.swing.JPanel;
import javax.swing.plaf.basic.BasicPanelUI;

public class PanelFormUICinza extends BasicPanelUI{
	
	private Color corInicial = new Color(63, 162, 219);
	private Color corFinal = new Color(2, 0, 49);

	protected void installDefaults(JPanel p){
		p.setOpaque(true);
	}
	
	public void paint(Graphics g, JComponent c){
		Graphics2D g2 = (Graphics2D)g;
		Dimension vSize = c.getSize();
		int altura = vSize.height;
		int largura = vSize.width;
		g2.fillRect(0, 0, largura, altura);
		g2.setPaint(new GradientPaint(0,0, corInicial, 0, altura, corFinal));
		g2.fillRect(3, 0, largura-4, altura-2);
	}
	
	
}
