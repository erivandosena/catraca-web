package br.edu.unilab.catraca.controller.recurso;

import java.sql.Connection;
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
@SuppressWarnings("restriction")
public class CartaoRecurso extends Recurso{
	
	public CartaoDAO dao;
	
	public void sincronizar(){
		this.dao = new CartaoDAO();
		ArrayList<Cartao> cartoes = this.obterLista();
		this.dao.limpar();
		if(cartoes == null){
			return;
		}
		for (Cartao cartao : cartoes) {
			
			if(!this.dao.inserir(cartao)){
				System.out.println("Erro ao tentar inserir: "+cartao.getNumero());	
			}
		}
		
	}
	public void sincronizar(Connection conexao){
		this.dao = new CartaoDAO(conexao);
		ArrayList<Cartao> cartoes = this.obterLista();
		if(cartoes == null){
			return;
		}
		this.dao.limpar();
		for (Cartao cartao : cartoes) {
			
			if(!this.dao.inserir(cartao)){
				System.out.println("Erro ao tentar inserir: "+cartao.getNumero());	
			}
		}
		
	}
	public ArrayList<Cartao> obterLista(){
		ArrayList<Cartao> lista = new ArrayList<Cartao>();
		
		String url = URL+"cartao/cartoes";
        System.out.println(url);
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
			output = jo.getString("cartoes");

		} catch (JSONException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
        JSONArray projectArray;

		try {
			projectArray = new JSONArray(output);
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
