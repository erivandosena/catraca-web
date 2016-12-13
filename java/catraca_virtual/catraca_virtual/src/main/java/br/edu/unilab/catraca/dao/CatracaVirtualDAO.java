package br.edu.unilab.catraca.dao;

import java.sql.Connection;
import java.sql.Date;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Calendar;

import br.edu.unilab.unicafe.model.Vinculo;

public class CatracaVirtualDAO extends DAO{
	public CatracaVirtualDAO(){
		super();
	}
	public CatracaVirtualDAO(int tipoDeConexao){
		super(tipoDeConexao);
		
	}
	public CatracaVirtualDAO(Connection conexao){
		super(conexao);
	}
	
	
	public boolean verificaVinculo(Vinculo vinculo){
	

		try {
			String sql = "SELECT *, tipo.tipo_id as id_tipo FROM cartao "
					+ " INNER JOIN vinculo "
					+ " ON cartao.cart_id = vinculo.cart_id "
					+ " INNER JOIN vinculo_tipo ON vinculo_tipo.vinc_id = vinculo.vinc_id "
					+ " INNER JOIN tipo ON tipo.tipo_id = vinculo_tipo.tipo_id "
					+ " INNER JOIN usuario on vinculo.usua_id = usuario.usua_id "
					+ " WHERE (? BETWEEN vinculo.vinc_inicio AND vinculo.vinc_fim) "
					+ " AND (cartao.cart_numero = ?)";
			
			PreparedStatement ps = this.getConexao().prepareStatement(sql);
			java.sql.Date data = new java.sql.Date(new java.util.Date().getTime());
			Calendar calendarAtual = Calendar.getInstance();
			ps.setString(1, data.toString()+" "+calendarAtual.get(Calendar.HOUR_OF_DAY)+":"+calendarAtual.get(Calendar.MINUTE)+":00");
			ps.setString(2, vinculo.getCartao().getNumero());
			ResultSet rs = ps.executeQuery();
			while(rs.next()){
				vinculo.getResponsavel().setNome(rs.getString("usua_nome"));
				vinculo.getCartao().getTipo().setNome(rs.getString("tipo_nome"));
				vinculo.getCartao().getTipo().setValorCobrado(rs.getDouble("tipo_valor"));
				vinculo.getCartao().getTipo().setId(rs.getInt("id_tipo"));
				return true;
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
		return false;
	}
	

	
}
