package br.edu.unilab.catraca.dao;

import java.io.UnsupportedEncodingException;
import java.security.MessageDigest;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import br.edu.unilab.unicafe.model.Usuario;

public class UsuarioDAO extends DAO {

	public UsuarioDAO(){
		super();
	}
	public UsuarioDAO(int tipoDeConexao){
		super(tipoDeConexao);
		
	}
	public UsuarioDAO(Connection conexao){
		super(conexao);
	}
	
	
	public boolean limpar(){
		
		PreparedStatement ps2;
		try {
			ps2 = this.getConexao().prepareStatement("DELETE FROM usuario");
			ps2.executeUpdate();
			return true;
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return false;
		
		
	}
	

	public boolean inserir(Usuario usuario){
		try {
			
			PreparedStatement ps2 = this.getConexao().prepareStatement("INSERT INTO usuario(usua_id, usua_nome, usua_email, usua_login, usua_senha, usua_nivel, id_base_externa) VALUES(?, ?, ?, ?, ?, ?, ?)");
			ps2.setInt(1, usuario.getId());
			ps2.setString(2, usuario.getNome());
			ps2.setString(3, usuario.getEmail());
			ps2.setString(4, usuario.getLogin());
			
			ps2.setString(5, usuario.getSenha());
			ps2.setInt(6, usuario.getNivelAcesso());
			ps2.setInt(7, usuario.getIdBaseExterna());
			
			
			ps2.executeUpdate();
			return true;
					
			
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return false;
		}		
		
		
	}

	/**
	 * 
	 * @param usuario
	 * @return
	 */
	public  boolean autenticaLocal(Usuario usuario){
		try {
			
			PreparedStatement ps = this.getConexao().prepareStatement("SELECT * FROM usuario WHERE login = ? AND senha = ?");
			ps.setString(1, usuario.getLogin());
			ps.setString(2, usuario.getSenha());
			ResultSet rs = ps.executeQuery();
			while(rs.next()){
				usuario.setId(rs.getInt("id_usuario"));
				usuario.setNome(rs.getString("nome"));
				usuario.setEmail(rs.getString("email"));
				return true;
			}
		} catch (SQLException e) {
			
			e.printStackTrace();
			return false;
		}
		
		return false;
		
		
	}
	
	public  boolean autentica(Usuario usuario){
		try {
			
			PreparedStatement ps = this.getConexao().prepareStatement("SELECT * FROM usuario WHERE usua_login = ? AND usua_senha = ?");
			ps.setString(1, usuario.getLogin());
			ps.setString(2, usuario.getSenha());
			ResultSet rs = ps.executeQuery();
			while(rs.next()){
				usuario.setId(rs.getInt("usua_id"));
				usuario.setNome(rs.getString("usua_nome"));
				usuario.setEmail(rs.getString("usua_email"));
				
				return true;
			}
		} catch (SQLException e) {
			
			e.printStackTrace();
			return false;
		}
		
		return false;
		
		
	}
	
	public Usuario logado(String login) {
		Usuario usuario = new Usuario();
		PreparedStatement ps;
		try {
			ps = this.getConexao().prepareStatement("SELECT * FROM usuario WHERE login = ? ORDER BY nome");
			ps.setString(1, login);
			ResultSet resultSet = ps.executeQuery();
			while (resultSet.next()) {
				usuario.setNome(resultSet.getString("nome"));
				usuario.setLogin(resultSet.getString("login"));
				usuario.setEmail(resultSet.getString("email"));
				usuario.setId(resultSet.getInt("id_usuario"));
				usuario.setCpf(resultSet.getString("cpf"));
				usuario.setSenha(resultSet.getString("senha"));
				usuario.setNivelAcesso(resultSet.getInt("nivel_acesso"));	
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return usuario;
	}
	
	/**
	 * Ele vai retornar verdadeiro caso o cadastro tenha dado certo e falso se o cadastro tiver dado errado. 
	 * O cadastro pode dar errado pelos seguintes motivos: 
	 * 1. O login n�o pode ser nenhum j� cadastrado no banco. 
	 * 2. O email tamb�m n�o pode se repetir. 
	 * 3. Pode ter dado um erro de SQLException. 
	 * @param usuario
	 * @return
	 */
	public boolean cadastra(Usuario usuario){
		try {
			PreparedStatement ps = this.getConexao().prepareStatement("SELECT * FROM usuario WHERE login = ? OR email = ?");
			ps.setString(1, usuario.getLogin());
			ps.setString(2, usuario.getEmail());
			ResultSet rs = ps.executeQuery();
			while(rs.next()){
			
				PreparedStatement psUpdate = this.getConexao().prepareStatement("UPDATE usuario set senha = ? WHERE login = ?");
				psUpdate.setString(1, usuario.getSenha());
				psUpdate.setString(2, usuario.getLogin());
				psUpdate.executeUpdate();
				
				usuario.setId(rs.getInt("id_usuario"));
				
				return false;
			}
			PreparedStatement ps2 = this.getConexao().prepareStatement("INSERT into usuario(nome, email, login, senha, id_base_externa) VALUES(?, ?, ?, ?, ?)");
			
			ps2.setString(1, usuario.getNome());
			ps2.setString(2, usuario.getEmail());
			ps2.setString(3, usuario.getLogin());
			ps2.setString(4, usuario.getSenha());
			ps2.setInt(5, usuario.getId());
			ps2.executeUpdate();
			cadastra(usuario);
			return true;
					
			
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return false;
		}		
	}

	public ArrayList<Usuario> retornaLista() throws SQLException{
	
		ArrayList<Usuario> lista = new ArrayList<Usuario>();
		PreparedStatement ps = this.getConexao().prepareStatement("SELECT * FROM usuario");
		ResultSet resultSet = ps.executeQuery();
		while(resultSet.next()){
			Usuario usuario = new Usuario();

			usuario.setLogin(resultSet.getString("login"));

			usuario.setId(resultSet.getInt("id_usuario"));
			usuario.setSenha(resultSet.getString("senha"));

			lista.add(usuario);
		}
		return lista;
	}
	
	public static String getMD5(String input) {
        byte[] source;
        try {
            //Get byte according by specified coding.
            source = input.getBytes("UTF-8");
        } catch (UnsupportedEncodingException e) {
            source = input.getBytes();
        }
        String result = null;
        char hexDigits[] = {'0', '1', '2', '3', '4', '5', '6', '7',
                '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            md.update(source);
            //The result should be one 128 integer
            byte temp[] = md.digest();
            char str[] = new char[16 * 2];
            int k = 0;
            for (int i = 0; i < 16; i++) {
                byte byte0 = temp[i];
                str[k++] = hexDigits[byte0 >>> 4 & 0xf];
                str[k++] = hexDigits[byte0 & 0xf];
            }
            result = new String(str);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return result;
    }
	
}
