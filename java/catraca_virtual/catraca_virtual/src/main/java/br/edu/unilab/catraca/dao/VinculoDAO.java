package br.edu.unilab.catraca.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import br.edu.unilab.unicafe.model.Vinculo;

public class VinculoDAO extends DAO{
	
	public VinculoDAO(){
		super();
	}
	public VinculoDAO(int tipoDeConexao){
		super(tipoDeConexao);
		
	}
	public VinculoDAO(Connection conexao){
		super(conexao);
	}
	
	
	public boolean limpar(){
		
		PreparedStatement ps2;
		PreparedStatement ps3;
		try {
			ps2 = this.getConexao().prepareStatement("DELETE FROM vinculo");
			ps2.executeUpdate();
			ps3 = this.getConexao().prepareStatement("DELETE FROM vinculo_tipo");
			ps3.executeUpdate();
			return true;
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return false;
		
		
	}
	public void mostrar(){
		try {
			
			PreparedStatement ps = this.getConexao().prepareStatement("SELECT * FROM vinculo");
			ResultSet rs = ps.executeQuery();
			while(rs.next()){
				System.out.println("Teste");
				
				
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
	}
	
	public boolean inserir(Vinculo elemento){
		try {
			
			PreparedStatement ps2 = this.getConexao().prepareStatement("INSERT INTO vinculo(vinc_id, vinc_avulso, vinc_inicio, vinc_fim, vinc_descricao, vinc_refeicoes, cart_id, usua_id) VALUES(?, ?, ?, ?, ?, ?, ?, ?)");
			
			ps2.setInt(1, elemento.getId());
			int valor = 1;
			if(!elemento.isAvulso()){
				valor = 0;
			}
			ps2.setInt(2, valor);
			ps2.setString(3, elemento.getInicioValidade());
			ps2.setString(4, elemento.getFinalValidade());
			ps2.setString(5,  elemento.getDescricao());
			ps2.setInt(6, elemento.getQuantidadeDeAlimentosPorTurno());
			ps2.setInt(7, elemento.getCartao().getId());
			ps2.setInt(8, elemento.getResponsavel().getId());
			
			
			
			ps2.executeUpdate();
			
			PreparedStatement ps3 = this.getConexao().prepareStatement("INSERT into vinculo_tipo(vinc_id, tipo_id) VALUES(?, ?)");
			ps3.setInt(1, elemento.getId());
			ps3.setInt(2, elemento.getCartao().getTipo().getId());
			ps3.executeUpdate();
			return true;
					
			
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return false;
		}		
		
		
	}
	

}
