package br.edu.unilab.catraca.controller.recurso;

import java.sql.Connection;
import java.util.ArrayList;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.ClientResponse;
import com.sun.jersey.api.client.WebResource;
import br.edu.unilab.catraca.dao.UsuarioDAO;
import br.edu.unilab.unicafe.model.Usuario;
import sun.misc.BASE64Encoder;

/**
 * 
 * @author Jefferson Uchoa Ponte
 *
 *
 *Objetivo desta classe é pegar os cartões do WebService e inserir na base local. 
 *
 */
@SuppressWarnings("restriction")
public class UsuarioRecurso extends Recurso{
	
	private UsuarioDAO dao;
	
	public void sincronizar(){
		this.dao = new UsuarioDAO();
		ArrayList<Usuario> lista = this.obterLista();
		this.dao.limpar();
		if(lista == null){
			return;
		}
		
		for (Usuario usuario: lista) {
			dao.inserir(usuario);
		}
	}
	public void sincronizar(Connection conexao){
		this.dao = new UsuarioDAO(conexao);
		ArrayList<Usuario> lista = this.obterLista();
		if(lista == null){
			return;
		}
		this.dao.limpar();
		
		for (Usuario usuario: lista) {
			dao.inserir(usuario);
		}
	}
	public ArrayList<Usuario> obterLista(){
		ArrayList<Usuario> lista = new ArrayList<Usuario>();
		String url = URL+"usuario/usuarios";
        String authString = USUARIO + ":" + SENHA;
		String authStringEnc = new BASE64Encoder().encode(authString.getBytes());
        Client restClient = Client.create();
        WebResource webResource = restClient.resource(url);
        ClientResponse resp = webResource.accept("application/json")
                                         .header("Authorization", "Basic " + authStringEnc)
                                         .get(ClientResponse.class);
        if(resp.getStatus() != 200){
        	
            System.err.println("Unable to connect to the server");
            return null;
        }
        
        String output = resp.getEntity(String.class);     
        JSONArray projectArray;
		try {
			
			projectArray = new JSONArray(output.substring(12));
			for (int i = 0; i < projectArray.length(); i++) {
	            JSONObject proj = projectArray.getJSONObject(i);
	            Usuario usuario = new Usuario();
	            usuario.setId(proj.getInt("usua_id"));
	            usuario.setNome(proj.getString("usua_nome"));
	            usuario.setEmail(proj.getString("usua_email"));
	            usuario.setLogin(proj.getString("usua_login"));
	            usuario.setSenha(proj.getString("usua_senha"));
	            usuario.setNivelAcesso(proj.getInt("usua_nivel"));
	            usuario.setIdBaseExterna(proj.getInt("id_base_externa"));
	            lista.add(usuario);
	            
	        }
			return lista;
			
		} catch (JSONException e) {
			e.printStackTrace();
			return null;
		}
		
	}
	
	
	
	

}
