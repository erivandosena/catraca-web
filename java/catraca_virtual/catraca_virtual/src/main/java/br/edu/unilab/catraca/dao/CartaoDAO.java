package br.edu.unilab.catraca.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import br.edu.unilab.unicafe.model.Cartao;

public class CartaoDAO extends DAO{
	public CartaoDAO(){
		super();
	}
	public CartaoDAO(int tipoDeConexao){
		super(tipoDeConexao);
		
	}
	public CartaoDAO(Connection conexao){
		super(conexao);
	}
	
	public boolean limpar(){
		
		PreparedStatement ps2;
		try {
			ps2 = this.getConexao().prepareStatement("DELETE FROM cartao");
			ps2.executeUpdate();
			return true;
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return false;
		
		
	}
	public void mostrar(){
		try {
			
			PreparedStatement ps = this.getConexao().prepareStatement("SELECT * FROM cartao");
			ResultSet rs = ps.executeQuery();
			while(rs.next()){
				System.out.println("Numero: "+rs.getString("cart_numero"));
				System.out.println("Creditos: "+rs.getDouble("cart_creditos"));
				
				
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
	}
	
	
	public boolean inserir(Cartao cartao){
		try {
			PreparedStatement ps2 = this.getConexao().prepareStatement("INSERT INTO cartao(cart_id, cart_numero, cart_creditos) VALUES(?, ?, ?)");
			ps2.setInt(1, cartao.getId());
			ps2.setString(2, cartao.getNumero());
			ps2.setDouble(3, cartao.getCreditos());			
			ps2.executeUpdate();
			return true;
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return false;
		}		
		
		
	}
	
	
	
	

}
