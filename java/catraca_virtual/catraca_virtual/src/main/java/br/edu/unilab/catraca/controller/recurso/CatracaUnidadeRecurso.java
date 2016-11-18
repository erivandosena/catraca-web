package br.edu.unilab.catraca.controller.recurso;

import java.util.ArrayList;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.ClientResponse;
import com.sun.jersey.api.client.WebResource;

import br.edu.unilab.catraca.dao.CatracaUnidadeDAO;
import br.edu.unilab.catraca.dao.CustoUnidadeDAO;
import br.edu.unilab.unicafe.model.CatracaUnidade;
import br.edu.unilab.unicafe.model.CustoUnidade;
import sun.misc.BASE64Encoder;

public class CatracaUnidadeRecurso extends Recurso{
	
	
	private CatracaUnidadeDAO dao;
	
	public void sincronizar(){
		this.dao = new CatracaUnidadeDAO();
		
		this.dao.limpar();
		ArrayList<CatracaUnidade> lista = this.obterLista();
		for (CatracaUnidade elemento : lista) {
			dao.inserir(elemento);
			
		}
	}
	public ArrayList<CatracaUnidade> obterLista(){
		ArrayList<CatracaUnidade> lista = new ArrayList<CatracaUnidade>();
		
		String url = URL+"catraca_unidade/jcatraca_unidade";
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
			
			projectArray = new JSONArray(output.substring(20));
			for (int i = 0; i < projectArray.length(); i++) {
	            JSONObject proj = projectArray.getJSONObject(i);
	            
	            CatracaUnidade elemento = new CatracaUnidade();
	            elemento.setId(proj.getInt("caun_id"));
	            elemento.setIdCatraca(proj.getInt("catr_id"));
	            elemento.setIdUnidade(proj.getInt("unid_id"));
	            lista.add(elemento);
	            
	        }
			return lista;
			
		} catch (JSONException e) {
			e.printStackTrace();
			return null;
		}
		
	}

}
