package br.edu.unilab.catraca.controller.recurso;

import java.sql.Connection;
import java.util.ArrayList;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.ClientResponse;
import com.sun.jersey.api.client.WebResource;

import br.edu.unilab.catraca.dao.UnidadeDAO;
import br.edu.unilab.unicafe.model.Unidade;
import sun.misc.BASE64Encoder;

@SuppressWarnings("restriction")
public class UnidadeRecurso extends Recurso{
	
	
	private UnidadeDAO dao;
	
	public void sincronizar(){
		this.dao = new UnidadeDAO();
		ArrayList<Unidade> lista = this.obterLista();
		this.dao.limpar();
		if(lista == null){
			return;
		}
		
		for (Unidade unidade : lista) {
			
			if(!this.dao.inserir(unidade)){
				System.out.println("Erro ao tentar inserir Unidade: "+unidade.getNome());	
			}
		}
		
	}
	public void sincronizar(Connection conexao){
		this.dao = new UnidadeDAO(conexao);
		ArrayList<Unidade> lista = this.obterLista();
		if(lista == null){
			return;
			
		}
		this.dao.limpar();
		for (Unidade unidade : lista) {
			
			if(!this.dao.inserir(unidade)){
				System.out.println("Erro ao tentar inserir Unidade: "+unidade.getNome());	
			}
		}
		
	}
	public ArrayList<Unidade> obterLista(){
		ArrayList<Unidade> lista = new ArrayList<Unidade>();
		
		String url = URL+"unidade/unidades";
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
	            Unidade unidade = new Unidade();
	            unidade.setId(proj.getInt("unid_id"));
	            unidade.setNome(proj.getString("unid_nome"));
	            lista.add(unidade);
	        }			
			return lista;
			
			
		} catch (JSONException e) {
			e.printStackTrace();
			return null;
		}
		
	}

}
