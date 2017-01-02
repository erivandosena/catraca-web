package br.edu.unilab.catraca.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/**
 * 
 * @author Jefferson
 *
 */
public class DAO {
	
	private int tipoDeConexao;
	public void setTipoDeConexao(int tipoDeConexao){
		this.tipoDeConexao = tipoDeConexao;
	}
	
	public DAO(int tipoDeConexao) {
		this.tipoDeConexao = tipoDeConexao;
		novaConexao();
	}

	public DAO() {
		this.tipoDeConexao = TIPO_CONEXAO_DEFAULT;
		novaConexao();
	}

	public DAO(Connection conexao) {
		this.conexao = conexao;
	}

	public void novaConexao(){
		this.conexao = null;
		try {
			switch (tipoDeConexao) {
			case TIPO_POSTGRESQL:
				Class.forName(DRIVER_POSTGRES);
				this.conexao = DriverManager.getConnection(JDBC_BANCO_POSTGRES+ "//" + HOST_POSTGRES + "/" + BANCO_POSTGRES,USUARIO_POSTGRES, SENHA_POSTGRES);
				break;
				
			case TIPO_MYSQL:
				Class.forName(DRIVER_MYSQL);
				this.conexao=DriverManager.getConnection(JDBC_BANCO_MYSQL+"//"+IP_MYSQL+"/"+BANCO_MYSQL,USUARIO_MYSQL,SENHA_MYSQL);
				break;
			case TIPO_SQLITE:
				Class.forName(DRIVER_SQLITE);
				this.conexao = DriverManager.getConnection(JDBC_BANCO_SQLITE);
				break;
			default:
				Class.forName(DRIVER_SQLITE);
				this.conexao = DriverManager.getConnection(JDBC_BANCO_SQLITE);
				break;
			}
		} catch (ClassNotFoundException e1) {
			e1.printStackTrace();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
	
	private Connection conexao;

	public Connection getConexao() {
		return conexao;
	}

	public void setConexao(Connection conexao) {
		this.conexao = conexao;
	}

	


	
	
	public static final String USUARIO_POSTGRES = "postgres";
	public  static final String HOST_POSTGRES = "localhost:5432";	
	public  static final String SENHA_POSTGRES = "senhaPostgres";
	public  static final String BANCO_POSTGRES = "bancoPostgres";
	public  static final String DRIVER_POSTGRES = "org.postgresql.Driver";
	public  static final String JDBC_BANCO_POSTGRES = "jdbc:postgresql:";
	public static final String DRIVER_SQLITE = "org.sqlite.JDBC";
	public static final String JDBC_BANCO_SQLITE = "jdbc:sqlite:banco.bd";

	
	public static final String USUARIO_MYSQL = "root";
	public static final String SENHA_MYSQL = "senhaMyql";
	public static final String IP_MYSQL = "127.0.0.1";
	public static final String BANCO_MYSQL = "banco_mysql";
	public static final String DRIVER_MYSQL = "com.mysql.jdbc.Driver";
	public static final String JDBC_BANCO_MYSQL = "jdbc:mysql:";
	
	
	
	public static final int TIPO_SQLITE = 0;
	/**
	 * Esta conexao serve para os dados que nao puderam ser sincronizados. 
	 */
	public static final int TIPO_SQLITE_SECUNDARIO = 3;
	public static final int TIPO_MYSQL = 1;
	public static final int TIPO_POSTGRESQL = 2;

	
	public static final int TIPO_CONEXAO_DEFAULT = TIPO_SQLITE;
	public static final int TIPO_CONEXAO_AUTENTICACAO = TIPO_SQLITE;
	
	

}
