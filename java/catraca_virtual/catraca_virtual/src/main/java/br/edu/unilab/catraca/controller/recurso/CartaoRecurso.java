package br.edu.unilab.catraca.controller.recurso;

import java.util.ArrayList;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.ClientResponse;
import com.sun.jersey.api.client.WebResource;

import br.edu.unilab.catraca.dao.CartaoDAO;
import br.edu.unilab.unicafe.model.Cartao;
import sun.misc.BASE64Encoder;

/**
 * 
 * @author Jefferson Uchoa Ponte
 *
 *
 *Objetivo desta classe é pegar os cartões do WebService e inserir na base local. 
 *
 */
public class CartaoRecurso {
	public CartaoDAO dao;
	
	
	public ArrayList<Cartao> obterLista(){
		ArrayList<Cartao> lista = new ArrayList<Cartao>();
		
		String url = "http://10.5.0.123:27289/api/cartao/jcartao";
        String name = "catraca";
        String password = "CaTr@CaUniLab2015";
        String authString = name + ":" + password;
        @SuppressWarnings("restriction")
		String authStringEnc = new BASE64Encoder().encode(authString.getBytes());

        Client restClient = Client.create();
        WebResource webResource = restClient.resource(url);
        ClientResponse resp = webResource.accept("application/json")
                                         .header("Authorization", "Basic " + authStringEnc)
                                         .get(ClientResponse.class);
        if(resp.getStatus() != 200){
            System.err.println("Unable to connect to the server");
        }
        
        String output = resp.getEntity(String.class);        
        JSONArray projectArray;
		try {
			projectArray = new JSONArray(output.substring(11));
			
			for (int i = 0; i < projectArray.length(); i++) {
	            JSONObject proj = projectArray.getJSONObject(i);
	            Cartao cartao = new Cartao();
	            cartao.setId(proj.getInt("cart_id"));
	            cartao.setNumero(proj.getString("cart_numero"));
	            lista.add(cartao);
	        }
			return lista;
			
		} catch (JSONException e) {
			e.printStackTrace();
			return null;
		}
		
	}
	
	
	
	

}
