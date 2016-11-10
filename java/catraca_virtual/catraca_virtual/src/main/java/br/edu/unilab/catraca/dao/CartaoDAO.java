package br.edu.unilab.catraca.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

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
	
	
	public void mostrar(){
		try {
			
			PreparedStatement ps = this.getConexao().prepareStatement("SELECT * FROM cartao");
			ResultSet rs = ps.executeQuery();
			while(rs.next()){
				System.out.println(rs.getString("cart_numero"));
				
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
		
		
	}
	
	public boolean inserir(){
		
		return true;
	}
	
	
	
	

}
