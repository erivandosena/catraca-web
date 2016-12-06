package br.edu.unilab.catraca.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import br.edu.unilab.unicafe.model.CustoRefeicao;

public class CustoRefeicaoDAO extends DAO{
	
	public CustoRefeicaoDAO(){
		super();
	}
	public CustoRefeicaoDAO(int tipoDeConexao){
		super(tipoDeConexao);
		
	}
	public CustoRefeicaoDAO(Connection conexao){
		super(conexao);
	}

	
	public boolean limpar(){
		
		PreparedStatement ps2;
		try {
			ps2 = this.getConexao().prepareStatement("DELETE FROM custo_refeicao");
			ps2.executeUpdate();
			return true;
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return false;
		
		
	}
	

	public boolean inserir(CustoRefeicao custoRefeicao){
		try {
			
			PreparedStatement ps2 = this.getConexao().prepareStatement("INSERT INTO custo_refeicao(cure_id, cure_valor, cure_data) VALUES(?, ?, ?)");
			
			ps2.setInt(1, custoRefeicao.getId());
			ps2.setDouble(2, custoRefeicao.getValor());
			ps2.setString(3, custoRefeicao.getData());
			
			ps2.executeUpdate();
			return true;
					
			
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return false;
		}		
		
		
	}

}
