package br.edu.unilab.catraca.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import br.edu.unilab.unicafe.model.TurnoUnidade;

public class TurnoUnidadeDAO extends DAO{

	public TurnoUnidadeDAO(){
		super();
	}
	public TurnoUnidadeDAO(int tipoDeConexao){
		super(tipoDeConexao);
		
	}
	public TurnoUnidadeDAO(Connection conexao){
		super(conexao);
	}
	
	
	public boolean limpar(){
		
		PreparedStatement ps2;
		try {
			ps2 = this.getConexao().prepareStatement("DELETE FROM unidade_turno");
			ps2.executeUpdate();
			return true;
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return false;
		
		
	}
	
	public ArrayList<TurnoUnidade>retornaLista(){
		try {
			ArrayList<TurnoUnidade> lista = new ArrayList<TurnoUnidade>();
			PreparedStatement ps = this.getConexao().prepareStatement("SELECT * FROM unidade_turno");
			ResultSet rs = ps.executeQuery();
			while(rs.next()){
				
				TurnoUnidade turnoUnidade = new TurnoUnidade();
				turnoUnidade.setId(rs.getInt("untu_id"));
				turnoUnidade.setIdTurno(rs.getInt("turn_id"));
				turnoUnidade.setIdUnidade(rs.getInt("unid_id"));
				lista.add(turnoUnidade);
				
				
			}
			return lista;
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return null;
		
	}
	
	
	public boolean inserir(TurnoUnidade turnoUnidade){
		try {
			
			PreparedStatement ps2 = this.getConexao().prepareStatement("INSERT INTO unidade_turno(untu_id, turn_id, unid_id) VALUES(?, ?, ?)");
			
			ps2.setInt(1, turnoUnidade.getId());
			ps2.setInt(2, turnoUnidade.getIdTurno());
			ps2.setInt(3, turnoUnidade.getIdUnidade());			
			ps2.executeUpdate();
			return true;
					
			
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return false;
		}		
		
		
	}
	
}
