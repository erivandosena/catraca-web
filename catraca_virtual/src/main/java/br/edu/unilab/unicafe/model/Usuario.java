package br.edu.unilab.unicafe.model;

/**
 * 
 * @author Jefferson
 *
 */

public class Usuario {
	private int id;
	private String nome;
	private String email;
	private String login;
	private String senha;
	private int nivelAcesso;
	private String cpf;
	private int idBaseExterna;

	
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

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getLogin() {
		return login;
	}

	public void setLogin(String login) {
		this.login = login;
	}

	public String getSenha() {

		return senha;
	}

	public void setSenha(String senha) {
		this.senha = senha;
	}



	public Usuario(String nome, String email, String login, String senha, int nivelAcesso, String cpf) {

		this.nome = nome;
		this.email = email;
		this.login = login;
		this.senha = senha;
		this.setNivelAcesso(nivelAcesso);
		this.setCpf(cpf);
	}

	public Usuario(int id, String nome, String email, String login, String senha, int nivelAcesso, String cpf) {
		super();
		this.id = id;
		this.nome = nome;
		this.email = email;
		this.login = login;
		this.senha = senha;
		this.setNivelAcesso(nivelAcesso);
		this.setCpf(cpf);
	}

	public int getNivelAcesso() {
		return nivelAcesso;
	}

	public void setNivelAcesso(int nivelAcesso) {
		this.nivelAcesso = nivelAcesso;
	}

	public String getCpf() {
		return cpf;
	}

	public void setCpf(String cpf) {
		this.cpf = cpf;
	}

	public Usuario() {
	}

	@Override
	public String toString() {
		// return "Usuario: id=" + id + "\n" + "nome=" + nome + "\n" + "email=" + email + "\n" + "login=" + login + "\n" + "senha=" + senha + "\n" + "nivelAcesso=" + nivelAcesso + "\n" + "cpf=" + cpf;
		return login;
	}

	public int getIdBaseExterna() {
		return idBaseExterna;
	}

	public void setIdBaseExterna(int idBaseExterna) {
		this.idBaseExterna = idBaseExterna;
	}

}
