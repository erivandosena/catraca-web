package br.edu.unilab.unicafe.model;

public class Registro {
	private int id;
	private String data;
	private double valorPago;
	private double valorCusto;
	private Cartao cartao;
	private Catraca catraca;
	private Vinculo vinculo;
	public Registro(){
		this.cartao = new Cartao();
		this.catraca = new Catraca();
		this.vinculo = new Vinculo();
	}
	
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getData() {
		return data;
	}
	public void setData(String data) {
		this.data = data;
	}
	public double getValorPago() {
		return valorPago;
	}
	public void setValorPago(double valorPago) {
		this.valorPago = valorPago;
	}
	public double getValorCusto() {
		return valorCusto;
	}
	public void setValorCusto(double valorCusto) {
		this.valorCusto = valorCusto;
	}
	public Cartao getCartao() {
		return cartao;
	}
	public void setCartao(Cartao cartao) {
		this.cartao = cartao;
	}
	public Catraca getCatraca() {
		return catraca;
	}
	public void setCatraca(Catraca catraca) {
		this.catraca = catraca;
	}
	public Vinculo getVinculo() {
		return vinculo;
	}
	public void setVinculo(Vinculo vinculo) {
		this.vinculo = vinculo;
	}
	

}
