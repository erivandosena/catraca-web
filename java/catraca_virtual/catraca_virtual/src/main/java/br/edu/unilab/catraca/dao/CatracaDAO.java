package br.edu.unilab.catraca.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import br.edu.unilab.unicafe.model.Cartao;
import br.edu.unilab.unicafe.model.Catraca;

public class CatracaDAO extends DAO{
	public CatracaDAO(){
		super();
	}
	public CatracaDAO(int tipoDeConexao){
		super(tipoDeConexao);
		
	}
	public CatracaDAO(Connection conexao){
		super(conexao);
	}
	
	
	public boolean limpar(){
		
		PreparedStatement ps2;
		try {
			ps2 = this.getConexao().prepareStatement("DELETE FROM catraca");
			ps2.executeUpdate();
			return true;
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return false;
		
		
	}
	public void mostrar(){
		try {
			
			PreparedStatement ps = this.getConexao().prepareStatement("SELECT * FROM catraca");
			ResultSet rs = ps.executeQuery();
			while(rs.next()){
				System.out.println("ID: "+rs.getString("catr_id"));
				System.out.println("NOme: "+rs.getDouble("catr_nome"));
				
				
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
	}
	
	public ArrayList<Catraca>retornaLista(){
		try {
			ArrayList<Catraca> lista = new ArrayList<Catraca>();
			PreparedStatement ps = this.getConexao().prepareStatement("SELECT * FROM catraca");
			ResultSet rs = ps.executeQuery();
			while(rs.next()){
				
				Catraca catraca = new Catraca();
				catraca.setId(rs.getInt("catr_id"));
				catraca.setNome(rs.getString("catr_nome"));
				catraca.setFinanceiroAtivo(true);
				if(rs.getInt("catr_financeiro") != 1){
					catraca.setFinanceiroAtivo(false);
					
				}
				lista.add(catraca);
				
				
			}
			return lista;
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return null;
		
	}
	
	
	public boolean inserir(Catraca catraca){
		try {
			
			PreparedStatement ps2 = this.getConexao().prepareStatement("INSERT INTO catraca(catr_id, catr_nome, catr_financeiro) VALUES(?, ?, ?)");
			
			ps2.setInt(1, catraca.getId());
			ps2.setString(2, catraca.getNome());
			int valor = 1;
			if(!catraca.isFinanceiroAtivo()){
				valor = 0;
			}
			ps2.setInt(3, valor);			
			ps2.executeUpdate();
			return true;
					
			
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return false;
		}		
		
		
	}
	
	
	
	
}
