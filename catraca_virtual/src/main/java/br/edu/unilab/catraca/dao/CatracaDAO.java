package br.edu.unilab.catraca.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import br.edu.unilab.unicafe.model.Catraca;
import br.edu.unilab.unicafe.model.Turno;
import br.edu.unilab.unicafe.model.Unidade;

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
	
	public Catraca retornaCatracaPorNome(Catraca catraca){
		try {
			PreparedStatement ps = this.getConexao().prepareStatement("SELECT * FROM catraca WHERE catr_nome = ?");
			ps.setString(1, catraca.getNome().trim());
			ResultSet rs = ps.executeQuery();
			while(rs.next()){
				catraca.setId(rs.getInt("catr_id"));
				catraca.setNome(rs.getString("catr_nome"));
				catraca.setFinanceiroAtivo(true);
				if(rs.getInt("catr_financeiro") != 1){
					catraca.setFinanceiroAtivo(false);
					
				}
				return catraca;
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
		return null;
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
	public Unidade unidadeDaCatraca(Catraca catraca){
		try {
			PreparedStatement ps = this.getConexao().prepareStatement("SELECT unidade.unid_id,unidade.unid_nome "
					+ "FROM unidade "
					+ "INNER JOIN catraca_unidade "
					+ "ON unidade.unid_id = catraca_unidade.unid_id "
					+ "INNER JOIN catraca ON catraca_unidade.catr_id = catraca.catr_id "
					+ "WHERE catraca.catr_id = ?");
			ps.setInt(1, catraca.getId());
			ResultSet rs = ps.executeQuery();
			while(rs.next()){
				Unidade unidade = new Unidade();
				unidade.setId(rs.getInt("unid_id"));
				unidade.setNome(rs.getString("unid_nome"));				
				return unidade;
			}

		} catch (SQLException e) {
			e.printStackTrace();
		}
		return null;
	}
	
	
	public ArrayList<Turno>turnosDaUnidade(Unidade unidade){
		try {
			
			ArrayList<Turno> lista = new ArrayList<Turno>();
			PreparedStatement ps = this.getConexao().prepareStatement("SELECT turno.turn_id, turno.turn_descricao, turno.turn_hora_inicio, turno.turn_hora_fim FROM turno INNER JOIN unidade_turno ON turno.turn_id = unidade_turno.turn_id INNER JOIN unidade ON unidade.unid_id = unidade_turno.unid_id WHERE unidade.unid_id = ?");
			ps.setInt(1, unidade.getId());
			
			ResultSet rs = ps.executeQuery();
			while(rs.next()){
				
				Turno turno = new Turno();
				turno.setId(rs.getInt("turn_id"));
				turno.setDescricao(rs.getString("turn_descricao"));
				turno.setHoraInicial(rs.getString("turn_hora_inicio"));
				turno.setHoraFinal(rs.getString("turn_hora_fim"));
				lista.add(turno);
				
				
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
