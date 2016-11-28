package br.edu.unilab.unicafe.model;

public class Cartao {
	
	private int id;
	private String numero;
	private double creditos;
	private Tipo tipo;
	
	public Cartao(){
		this.tipo = new Tipo();
	}
	
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	
	public String getNumero() {
		return numero;
	}
	public void setNumero(String numero) {
		this.numero = numero;
	}
	public double getCreditos() {
		return creditos;
	}
	public void setCreditos(double creditos) {
		this.creditos = creditos;
	}
	public Tipo getTipo() {
		return tipo;
	}
	public void setTipo(Tipo tipo) {
		this.tipo = tipo;
	}
}
