package br.edu.unilab.catraca.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import br.edu.unilab.unicafe.model.Turno;

public class TurnoDAO extends DAO{
	public TurnoDAO(){
		super();
	}
	public TurnoDAO(int tipoDeConexao){
		super(tipoDeConexao);
		
	}
	public TurnoDAO(Connection conexao){
		super(conexao);
	}
	
	
	public boolean limpar(){
		
		PreparedStatement ps2;
		try {
			ps2 = this.getConexao().prepareStatement("DELETE FROM turno");
			ps2.executeUpdate();
			return true;
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return false;
		
		
	}
	public void mostrar(){
		try {
			
			PreparedStatement ps = this.getConexao().prepareStatement("SELECT * FROM turno");
			ResultSet rs = ps.executeQuery();
			while(rs.next()){
				System.out.println("ID: "+rs.getString("turn_id"));
				System.out.println("Descricao: "+rs.getDouble("turn_descricao"));
				
				
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
	}
	public ArrayList<Turno>retornaLista(){
		try {
			ArrayList<Turno> lista = new ArrayList<Turno>();
			PreparedStatement ps = this.getConexao().prepareStatement("SELECT * FROM turno");
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
	
	
	public boolean inserir(Turno turno){
		try {
			
			PreparedStatement ps2 = this.getConexao().prepareStatement("INSERT INTO turno(turn_id, turn_hora_inicio, turn_hora_fim, turn_descricao) VALUES(?, ?, ?, ?)");
			
			ps2.setInt(1, turno.getId());
			ps2.setString(2, turno.getHoraInicial());
			ps2.setString(3, turno.getHoraFinal());
			ps2.setString(4, turno.getDescricao());
			
			ps2.executeUpdate();
			return true;
					
			
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return false;
		}		
		
		
	}
	
	

}
