package br.edu.unilab.catraca.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import br.edu.unilab.unicafe.model.Tipo;
import br.edu.unilab.unicafe.model.Turno;

public class TipoDAO extends DAO{
	public TipoDAO(){
		super();
	}
	public TipoDAO(int tipoDeConexao){
		super(tipoDeConexao);
		
	}
	public TipoDAO(Connection conexao){
		super(conexao);
	}
	
	
	public boolean limpar(){
		
		PreparedStatement ps2;
		try {
			ps2 = this.getConexao().prepareStatement("DELETE FROM tipo");
			ps2.executeUpdate();
			return true;
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return false;
		
		
	}
	public boolean inserir(Tipo elemento){
		try {
			
			PreparedStatement ps2 = this.getConexao().prepareStatement("INSERT INTO tipo(tipo_id, tipo_nome, tipo_valor) VALUES(?, ?, ?)");
			
			ps2.setInt(1, elemento.getId());
			ps2.setString(2, elemento.getNome());
			ps2.setDouble(3, elemento.getValorCobrado());
			
			ps2.executeUpdate();
			return true;
					
			
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return false;
		}		
		
		
	}
}
