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
public class CartaoRecurso extends Recurso{
	
	public CartaoDAO dao;
	
	public void sincronizar(){
		this.dao = new CartaoDAO();
		this.dao.limpar();
		ArrayList<Cartao> cartoes = this.obterLista();
		
		for (Cartao cartao : cartoes) {
			
			if(!this.dao.inserir(cartao)){
				System.out.println("Erro ao tentar inserir: "+cartao.getNumero());	
			}
		}
		
	}
	
	public ArrayList<Cartao> obterLista(){
		ArrayList<Cartao> lista = new ArrayList<Cartao>();
		
		String url = URL+"cartao/jcartao";
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
			projectArray = new JSONArray(output.substring(11));
			for (int i = 0; i < projectArray.length(); i++) {
	            JSONObject proj = projectArray.getJSONObject(i);
	            Cartao cartao = new Cartao();
	            cartao.setId(proj.getInt("cart_id"));
	            cartao.setNumero(proj.getString("cart_numero"));
	            cartao.setCreditos(proj.getDouble("cart_creditos"));
	            lista.add(cartao);
	        }
			
			return lista;
			
			
		} catch (JSONException e) {
			e.printStackTrace();
			return null;
		}
		
	}
	

}
