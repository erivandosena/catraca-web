package br.edu.unilab.catraca.controller.recurso;

import java.sql.Connection;
import java.util.ArrayList;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.ClientResponse;
import com.sun.jersey.api.client.WebResource;

import br.edu.unilab.catraca.dao.CustoUnidadeDAO;
import br.edu.unilab.unicafe.model.CustoUnidade;
import sun.misc.BASE64Encoder;

@SuppressWarnings("restriction")
public class CustoUnidadeRecurso extends Recurso{
	
	
	private CustoUnidadeDAO dao;
	
	public void sincronizar(){
		this.dao = new CustoUnidadeDAO();
		
		this.dao.limpar();
		ArrayList<CustoUnidade> lista = this.obterLista();
		for (CustoUnidade elemento : lista) {
			dao.inserir(elemento);
			
		}
	}
	
	public void sincronizar(Connection conexao){
		this.dao = new CustoUnidadeDAO(conexao);
		
		this.dao.limpar();
		ArrayList<CustoUnidade> lista = this.obterLista();
		for (CustoUnidade elemento : lista) {
			dao.inserir(elemento);
			
		}
	}
	
	public ArrayList<CustoUnidade> obterLista(){
		ArrayList<CustoUnidade> lista = new ArrayList<CustoUnidade>();
		
		String url = URL+"custo_unidade/custos_unidade";
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
        try {
			JSONObject jo = new JSONObject(output);
			output = jo.getString("custos_unidade");

		} catch (JSONException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
        JSONArray projectArray;
		try {
			
			projectArray = new JSONArray(output);
			for (int i = 0; i < projectArray.length(); i++) {
	            JSONObject proj = projectArray.getJSONObject(i);
	            
	            CustoUnidade elemento = new CustoUnidade();
	            elemento.setId(proj.getInt("cuun_id"));
	            elemento.setIdUnidade(proj.getInt("unid_id"));
	            elemento.setIdCusto(proj.getInt("cure_id"));
	            lista.add(elemento);
	            
	        }
			return lista;
			
		} catch (JSONException e) {
			e.printStackTrace();
			return null;
		}
		
	}
	

}
