package br.edu.unilab.catraca.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import br.edu.unilab.unicafe.model.CustoUnidade;

public class CustoUnidadeDAO extends DAO {
	
	
	public CustoUnidadeDAO(){
		super();
	}
	public CustoUnidadeDAO(int tipoDeConexao){
		super(tipoDeConexao);
		
	}
	public CustoUnidadeDAO(Connection conexao){
		super(conexao);
	}
	

	public boolean limpar(){
		
		PreparedStatement ps2;
		try {
			ps2 = this.getConexao().prepareStatement("DELETE FROM custo_unidade");
			ps2.executeUpdate();
			return true;
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return false;
		
		
	}

	
	public boolean inserir(CustoUnidade elemento){
		try {
			
			PreparedStatement ps2 = this.getConexao().prepareStatement("INSERT INTO custo_unidade(cuun_id, unid_id, cure_id) VALUES(?, ?, ?)");
			
			ps2.setInt(1, elemento.getId());
			ps2.setInt(2, elemento.getIdUnidade());
			ps2.setInt(3, elemento.getIdCusto());
			ps2.executeUpdate();
			return true;
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return false;
		}		
		
		
	}
	
	
}
