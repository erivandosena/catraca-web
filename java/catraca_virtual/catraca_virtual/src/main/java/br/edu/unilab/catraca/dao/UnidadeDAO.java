package br.edu.unilab.catraca.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import br.edu.unilab.unicafe.model.Unidade;

public class UnidadeDAO extends DAO{
	public UnidadeDAO(){
		super();
	}
	public UnidadeDAO(int tipoDeConexao){
		super(tipoDeConexao);
		
	}
	public UnidadeDAO(Connection conexao){
		super(conexao);
	}
	
	public boolean limpar(){
		
		PreparedStatement ps2;
		try {
			ps2 = this.getConexao().prepareStatement("DELETE FROM unidade");
			ps2.executeUpdate();
			return true;
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return false;
	}
	public void mostrar(){
		try {
			
			PreparedStatement ps = this.getConexao().prepareStatement("SELECT * FROM unidade");
			ResultSet rs = ps.executeQuery();
			while(rs.next()){
				System.out.println("ID: "+rs.getString("unid_id"));
				System.out.println("NOme: "+rs.getString("unid_nome"));
				
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
	}
	
	public ArrayList<Unidade>retornaLista(){
		try {
			ArrayList<Unidade> lista = new ArrayList<Unidade>();
			PreparedStatement ps = this.getConexao().prepareStatement("SELECT * FROM unidade");
			ResultSet rs = ps.executeQuery();
			while(rs.next()){
				Unidade unidade = new Unidade();
				unidade.setId(rs.getInt("unid_id"));
				unidade.setNome(rs.getString("unid_nome"));				
				lista.add(unidade);
			}
			return lista;
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return null;
	}
	

	
	
	public boolean inserir(Unidade unidade){
		try {
			
			PreparedStatement ps2 = this.getConexao().prepareStatement("INSERT INTO unidade(unid_id, unid_nome) VALUES(?, ?)");
			
			ps2.setInt(1, unidade.getId());
			ps2.setString(2, unidade.getNome());
						
			ps2.executeUpdate();
			return true;
					
			
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return false;
		}		
		
		
	}
	
}
