package br.edu.unilab.unicafe.model;
/**
 * Relacionamento de um turno com unidade
 * @author Jefferson Uchoa POnte
 *
 */
public class TurnoUnidade {

	private int id;
	private int idTurno;
	private int idUnidade;
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public int getIdTurno() {
		return idTurno;
	}
	public void setIdTurno(int idTurno) {
		this.idTurno = idTurno;
	}
	public int getIdUnidade() {
		return idUnidade;
	}
	public void setIdUnidade(int idUnidade) {
		this.idUnidade = idUnidade;
	}
	
}
