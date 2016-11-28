package br.edu.unilab.unicafe.model;

public class Vinculo {
	private int id;
	private boolean avulso;
	private Usuario responsavel;
	private String inicioValidade;
	private String finalValidade;
	private int quantidadeDeAlimentosPorTurno;
	private String descricao;
	private Cartao cartao;
	private int refeicoesRestantes;
	
	
	public Vinculo(){
		this.cartao = new Cartao();
		this.responsavel = new Usuario();
	}
	
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public boolean isAvulso() {
		return avulso;
	}
	public void setAvulso(boolean avulso) {
		this.avulso = avulso;
	}
	public Usuario getResponsavel() {
		return responsavel;
	}
	public void setResponsavel(Usuario responsavel) {
		this.responsavel = responsavel;
	}
	public String getInicioValidade() {
		return inicioValidade;
	}
	public void setInicioValidade(String inicioValidade) {
		this.inicioValidade = inicioValidade;
	}
	public String getFinalValidade() {
		return finalValidade;
	}
	public void setFinalValidade(String finalValidade) {
		this.finalValidade = finalValidade;
	}
	public int getQuantidadeDeAlimentosPorTurno() {
		return quantidadeDeAlimentosPorTurno;
	}
	public void setQuantidadeDeAlimentosPorTurno(int quantidadeDeAlimentosPorTurno) {
		this.quantidadeDeAlimentosPorTurno = quantidadeDeAlimentosPorTurno;
	}
	public String getDescricao() {
		return descricao;
	}
	public void setDescricao(String descricao) {
		this.descricao = descricao;
	}
	public Cartao getCartao() {
		return cartao;
	}
	public void setCartao(Cartao cartao) {
		this.cartao = cartao;
	}
	public int getRefeicoesRestantes() {
		return refeicoesRestantes;
	}
	public void setRefeicoesRestantes(int refeicoesRestantes) {
		this.refeicoesRestantes = refeicoesRestantes;
	}
	
	
}
