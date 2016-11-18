package br.edu.unilab.unicafe.model;

import java.net.InetAddress;
import java.net.UnknownHostException;

public class Catraca {
	private int id;
	private String nome;
	private boolean financeiroAtivo;
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public boolean isFinanceiroAtivo() {
		return financeiroAtivo;
	}
	public void setFinanceiroAtivo(boolean financeiroAtivo) {
		this.financeiroAtivo = financeiroAtivo;
	}
	
	public void maquinaLocal() throws UnknownHostException{
		InetAddress ia = null;
		ia = InetAddress.getLocalHost();
		this.nome = ia.getHostName().toString();
	}
	

}
