package br.edu.unilab.catraca.controller.recurso;

import java.util.ArrayList;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.ClientResponse;
import com.sun.jersey.api.client.WebResource;

import br.edu.unilab.catraca.dao.CartaoDAO;
import br.edu.unilab.catraca.dao.CatracaDAO;
import br.edu.unilab.unicafe.model.Cartao;
import br.edu.unilab.unicafe.model.Catraca;
import sun.misc.BASE64Encoder;


public class CatracaRecurso extends Recurso{

	private CatracaDAO dao;
	
	public void sincronizar(){
		this.dao = new CatracaDAO();
		
		this.dao.limpar();
		ArrayList<Catraca> catracas = this.obterLista();
		for (Catraca catraca : catracas) {
			if(!dao.inserir(catraca)){
				System.out.println("Erro ao tentar inserir catraca: "+catraca.getNome());
			}
		}
	}
	
	public ArrayList<Catraca> obterLista(){
		ArrayList<Catraca> lista = new ArrayList<Catraca>();
		
		String url = URL+"catraca/jcatraca";
        String authString = USUARIO + ":" + SENHA;
        
        @SuppressWarnings("restriction")
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
			
			projectArray = new JSONArray(output.substring(13));
			for (int i = 0; i < projectArray.length(); i++) {
	            JSONObject proj = projectArray.getJSONObject(i);
	            Catraca catraca = new Catraca();
	            catraca.setId(proj.getInt("catr_id"));
	            catraca.setNome(proj.getString("catr_nome"));
	            catraca.setFinanceiroAtivo(proj.getBoolean("catr_financeiro"));
	            lista.add(catraca);
	            
	        }
			return lista;
			
		} catch (JSONException e) {
			e.printStackTrace();
			return null;
		}
		
	}
}
