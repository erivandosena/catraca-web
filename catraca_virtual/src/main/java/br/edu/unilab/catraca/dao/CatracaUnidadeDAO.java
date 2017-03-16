package br.edu.unilab.catraca.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import br.edu.unilab.unicafe.model.CatracaUnidade;

public class CatracaUnidadeDAO extends DAO{
	
	public CatracaUnidadeDAO(){
		super();
	}
	public CatracaUnidadeDAO(int tipoDeConexao){
		super(tipoDeConexao);
		
	}
	public CatracaUnidadeDAO(Connection conexao){
		super(conexao);
	}
	

	public boolean limpar(){
		
		PreparedStatement ps2;
		try {
			ps2 = this.getConexao().prepareStatement("DELETE FROM catraca_unidade");
			ps2.executeUpdate();
			return true;
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return false;
		
		
	}

	
	public boolean inserir(CatracaUnidade elemento){
		try {
			
			PreparedStatement ps2 = this.getConexao().prepareStatement("INSERT INTO catraca_unidade(caun_id, catr_id, unid_id) VALUES(?, ?, ?)");
			
			ps2.setInt(1, elemento.getId());
			ps2.setInt(2, elemento.getIdCatraca());
			ps2.setInt(3, elemento.getIdUnidade());
			ps2.executeUpdate();
			return true;
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return false;
		}		
		
		
	}
	

}
