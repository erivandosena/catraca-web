package br.edu.unilab.catraca.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import br.edu.unilab.unicafe.model.Registro;

public class RegistroDAO extends DAO{
	
	public RegistroDAO(){
		super();
	}
	public RegistroDAO(int tipoDeConexao){
		super(tipoDeConexao);
		
	}
	public RegistroDAO(Connection conexao){
		super(conexao);
	}
	
	public boolean limpar(){
		
		PreparedStatement ps2;
		try {
			ps2 = this.getConexao().prepareStatement("DELETE FROM registro");
			ps2.executeUpdate();
			return true;
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return false;
		
		
	}

	public boolean inserir(Registro registro){
		try {
			
			PreparedStatement ps2 = this.getConexao().prepareStatement("INSERT INTO registro(regi_id, regi_data, regi_valor_pago, regi_valor_custo, cart_id, catr_id, vinc_id) VALUES(?, ?, ?, ?, ?, ?, ?)");
			ps2.setInt(1, registro.getId());
			ps2.setString(2, registro.getData());
			ps2.setDouble(3, registro.getValorPago());			
			ps2.setDouble(4, registro.getValorCusto());
			ps2.setDouble(5, registro.getValorCusto());
			ps2.setInt(6, registro.getCartao().getId());
			ps2.setInt(7, registro.getVinculo().getId());
			
			ps2.executeUpdate();
			return true;
					
			
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return false;
		}		
		
		
	}
	
	
	

}
