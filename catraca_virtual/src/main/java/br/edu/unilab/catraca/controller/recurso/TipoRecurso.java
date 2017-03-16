package br.edu.unilab.catraca.controller.recurso;

import java.sql.Connection;
import java.util.ArrayList;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.ClientResponse;
import com.sun.jersey.api.client.WebResource;

import br.edu.unilab.catraca.dao.TipoDAO;
import br.edu.unilab.unicafe.model.Tipo;
import sun.misc.BASE64Encoder;

@SuppressWarnings("restriction")
public class TipoRecurso extends Recurso{
	
	private TipoDAO dao;
	public void sincronizar(Connection conexao){
		this.dao = new TipoDAO(conexao);
		this.dao.limpar();
		ArrayList<Tipo> lista = this.obterLista();
		for (Tipo elemento : lista) {
			dao.inserir(elemento);
		}
	}
	public void sincronizar(){
		this.dao = new TipoDAO();
		this.dao.limpar();
		ArrayList<Tipo> lista = this.obterLista();
		for (Tipo elemento : lista) {
			dao.inserir(elemento);
		}
	}
	public ArrayList<Tipo> obterLista(){
		ArrayList<Tipo> lista = new ArrayList<Tipo>();
		
		String url = URL+"tipo/tipos";
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
			
			projectArray = new JSONArray(output.substring(9));
			for (int i = 0; i < projectArray.length(); i++) {
	            JSONObject proj = projectArray.getJSONObject(i);
	            Tipo elemento = new Tipo();
	            elemento.setId(proj.getInt("tipo_id"));
	            elemento.setNome(proj.getString("tipo_nome"));
	            elemento.setValorCobrado(proj.getDouble("tipo_valor"));
	            lista.add(elemento);
	            
	        }
			return lista;
			
		} catch (JSONException e) {
			e.printStackTrace();
			return null;
		}
		
	}
	
	

}
