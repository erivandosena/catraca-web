package br.edu.unilab.catraca.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

import br.edu.unilab.unicafe.model.Catraca;
import br.edu.unilab.unicafe.model.Registro;
import br.edu.unilab.unicafe.model.Tipo;
import br.edu.unilab.unicafe.model.Turno;
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
	public double custo(Catraca catraca){
		double custo = 0;
		try {
			PreparedStatement ps = this.getConexao().prepareStatement("SELECT cure_valor FROM custo_refeicao"
					+ " INNER JOIN custo_unidade "
					+ " ON custo_unidade.cure_id = custo_refeicao.cure_id "
					+ "	INNER JOIN unidade "
					+ " ON unidade.unid_id = custo_unidade.unid_id INNER JOIN catraca_unidade ON catraca_unidade.unid_id = unidade.unid_id"
					+ " WHERE catraca_unidade.catr_id = ?"
					+ " ORDER BY custo_unidade.cure_id DESC LIMIT 1");
			ps.setInt(1, catraca.getId());
			ResultSet rs = ps.executeQuery();
			while(rs.next()){
				
				custo = rs.getDouble("cure_valor");
				
			}

		} catch (SQLException e) {
			e.printStackTrace();
		}
		return custo;
	}
	
	public boolean verificaVinculo(Vinculo vinculo){

		try {
			String sql = "SELECT *, cartao.cart_id as id_cartao, vinculo.vinc_id as id_vinculo,  tipo.tipo_id as id_tipo FROM cartao "
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
			ps.setString(1, data.toString()+" "+String.format("%02d", Integer.parseInt(calendarAtual.get(Calendar.HOUR_OF_DAY)+""))+":"+String.format("%02d", Integer.parseInt(calendarAtual.get(Calendar.MINUTE)+""))+":00");
			ps.setString(2, vinculo.getCartao().getNumero());

			ResultSet rs = ps.executeQuery();
			while(rs.next()){
				vinculo.setId(rs.getInt("id_vinculo"));
				vinculo.getResponsavel().setNome(rs.getString("usua_nome"));
				vinculo.getCartao().getTipo().setNome(rs.getString("tipo_nome"));
				vinculo.getCartao().setId(rs.getInt("id_cartao"));
				vinculo.getCartao().getTipo().setValorCobrado(rs.getDouble("tipo_valor"));
				vinculo.getCartao().getTipo().setId(rs.getInt("id_tipo"));
				vinculo.setQuantidadeDeAlimentosPorTurno(rs.getInt("vinc_refeicoes"));
				return true;
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
		return false;
	}
	
	public boolean podeContinuarComendo(Vinculo vinculo, Turno turno){
		int i = 0;
		
		
		try {
			
			String sql = "select * from registro WHERE registro.regi_data BETWEEN ? AND ? AND vinc_id = ? ORDER BY regi_id DESC LIMIT ?;";
			PreparedStatement ps = this.getConexao().prepareStatement(sql);
			java.sql.Date data = new java.sql.Date(new java.util.Date().getTime());
			Date dateHoraInicial = null;
			Date dateHoraFinal = null;
			SimpleDateFormat format = new SimpleDateFormat("HH:mm:ss");
			format.setLenient(false);
			dateHoraFinal = format.parse(turno.getHoraFinal());
			dateHoraInicial = format.parse(turno.getHoraInicial());
			Calendar calendarInicio = Calendar.getInstance();
			Calendar calendarFinal = Calendar.getInstance();
			calendarInicio.setTime(dateHoraInicial);
			calendarFinal.setTime(dateHoraFinal);
			ps.setString(1, data.toString()+" "+String.format("%02d", Integer.parseInt(calendarInicio.get(Calendar.HOUR_OF_DAY)+""))+":"+String.format("%02d", Integer.parseInt(calendarInicio.get(Calendar.MINUTE)+""))+":00");
			ps.setString(2, data.toString()+" "+String.format("%02d", Integer.parseInt(calendarFinal.get(Calendar.HOUR_OF_DAY)+""))+":"+String.format("%02d", Integer.parseInt(calendarFinal.get(Calendar.MINUTE)+""))+":00");
			
			ps.setInt(3, vinculo.getId());
			ps.setInt(4, vinculo.getQuantidadeDeAlimentosPorTurno());
			ResultSet rs = ps.executeQuery();
			
			while(rs.next()){
				i++;
			}
			vinculo.setRefeicoesRestantes(vinculo.getQuantidadeDeAlimentosPorTurno()-i);
			
			if(i < vinculo.getQuantidadeDeAlimentosPorTurno()){
				return true;
			}
			return false;
			
		} catch (SQLException | ParseException e) {
			e.printStackTrace();
		}
		return false;
	}
	
	
	public boolean vinculoEhIsento(Vinculo vinculo){

		try {
			String sql ="SELECT * FROM vinculo LEFT JOIN cartao ON cartao.cart_id = vinculo.cart_id"
					+ " INNER JOIN isencao ON cartao.cart_id = isencao.cart_id"
					+ " WHERE (vinculo.vinc_id = $idVinculo)"
					+ " AND  ('$dataTimeAtual' < isencao.isen_fim);";
			
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
				vinculo.setQuantidadeDeAlimentosPorTurno(rs.getInt("vinc_refeicoes"));
				
				return true;
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
		return false;
	}
	public boolean inserirRegistro(Registro registro){

		try {
			
			PreparedStatement ps2 = this.getConexao().prepareStatement("INSERT "
					+ " INTO registro(regi_data, regi_valor_pago, regi_valor_custo, cart_id, catr_id, vinc_id) "
					+ " VALUES(?, ?, ?, ?, ?, ?)");
			Calendar calendarAtual = Calendar.getInstance();
			java.sql.Date data = new java.sql.Date(new java.util.Date().getTime());
			registro.setData(data.toString()+" "+String.format("%02d", Integer.parseInt(calendarAtual.get(Calendar.HOUR_OF_DAY)+""))+":"+String.format("%02d", Integer.parseInt(calendarAtual.get(Calendar.MINUTE)+""))+":00");
			ps2.setString(1, registro.getData());
			ps2.setDouble(2, registro.getValorPago());			
			ps2.setDouble(3, registro.getValorCusto());
			ps2.setDouble(4, registro.getCartao().getId());
			ps2.setInt(5, registro.getCatraca().getId());
			ps2.setInt(6, registro.getVinculo().getId());
			
			ps2.executeUpdate();
			return true;
	
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return false;
		}		
		
	}

	public int totalGiroTurnoAtualNaoIsento(Catraca catraca, Tipo tipo, Turno turno){
		int resultado = 0;

		try {
			String sql = "SELECT sum(1) as resultado FROM registro INNER JOIN catraca ON registro.catr_id = catraca.catr_id"
					+ " INNER JOIN cartao ON cartao.cart_id = registro.cart_id "
					+ " INNER JOIN vinculo ON registro.vinc_id = vinculo.vinc_id "
					+ " INNER JOIN vinculo_tipo ON vinculo_tipo.vinc_id = vinculo.vinc_id"
					+ " WHERE (catraca.catr_id = ?)"
					+ " AND (registro.regi_data BETWEEN ? AND ?) AND (vinculo_tipo.tipo_id = ?) AND "
					+ " (regi_valor_pago > 0) ;";
			
			PreparedStatement ps = this.getConexao().prepareStatement(sql);
			ps.setInt(1, catraca.getId());
			java.sql.Date data = new java.sql.Date(new java.util.Date().getTime());
			
			ps.setString(2, data.toString()+" "+turno.getHoraInicial());
			ps.setString(3, data.toString()+" "+turno.getHoraFinal());
			ps.setInt(4, tipo.getId());
			
			ResultSet rs = ps.executeQuery();
			while(rs.next()){
				resultado = rs.getInt("resultado");
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
		return resultado;
	}
	public int totalGiroTurnoAtualIsento(Catraca catraca, Turno turno){
		int resultado = 0;

		try {
			String sql = "SELECT sum(1) as resultado FROM registro INNER JOIN catraca ON registro.catr_id = catraca.catr_id"
					+ " INNER JOIN cartao ON cartao.cart_id = registro.cart_id "
					+ " INNER JOIN vinculo ON registro.vinc_id = vinculo.vinc_id "
					+ " INNER JOIN vinculo_tipo ON vinculo_tipo.vinc_id = vinculo.vinc_id"
					+ " WHERE (catraca.catr_id = ?)"
					+ " AND (registro.regi_data BETWEEN ? AND ?) AND "
					+ " (regi_valor_pago = 0) ;";
			
			PreparedStatement ps = this.getConexao().prepareStatement(sql);
			ps.setInt(1, catraca.getId());
			java.sql.Date data = new java.sql.Date(new java.util.Date().getTime());
			
			ps.setString(2, data.toString()+" "+turno.getHoraInicial());
			ps.setString(3, data.toString()+" "+turno.getHoraFinal());
			
			ResultSet rs = ps.executeQuery();
			while(rs.next()){
				resultado = rs.getInt("resultado");
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
		return resultado;
	}
	
	public boolean vinculoEhIsento(){
		return false;
	}
	
}
