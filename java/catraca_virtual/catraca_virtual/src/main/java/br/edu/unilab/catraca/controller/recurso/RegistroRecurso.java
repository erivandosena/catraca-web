package br.edu.unilab.catraca.controller.recurso;

import java.sql.Connection;
import java.util.ArrayList;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.ClientResponse;
import com.sun.jersey.api.client.WebResource;

import br.edu.unilab.catraca.dao.RegistroDAO;
import br.edu.unilab.unicafe.model.Registro;
import sun.misc.BASE64Encoder;

@SuppressWarnings("restriction")
public class RegistroRecurso extends Recurso{
	private RegistroDAO dao;
	
	public boolean enviar(Registro registro){
		JSONObject jsonObject = new JSONObject();
		try {
			jsonObject.put("Teste", "Teste");
		} catch (JSONException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		System.out.println(jsonObject.toString());
		return true;
		
	}
	
	
	public void sincronizar(){
		this.dao = new RegistroDAO();
		
		this.dao.limpar();
		ArrayList<Registro> lista = this.obterLista();
		for (Registro elemento : lista) {
			dao.inserir(elemento);
		}
	}
	public void sincronizar(Connection conexao){
		this.dao = new RegistroDAO(conexao);
		ArrayList<Registro> lista = this.obterLista();
		this.dao.limpar();
		if(lista == null){
			return;
		}

		
		for (Registro elemento : lista) {
			dao.inserir(elemento);
		}
	}
	public ArrayList<Registro> obterLista(){
		ArrayList<Registro> lista = new ArrayList<Registro>();
		
		String url = URL+"registro/20161116%20110000/20161116%20130000";
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
			
			projectArray = new JSONArray(output.substring(13));
			for (int i = 0; i < projectArray.length(); i++) {
	            JSONObject proj = projectArray.getJSONObject(i);
	            Registro elemento = new Registro();
	            elemento.setId(proj.getInt("regi_id"));
	            elemento.setData(proj.getString("regi_data"));
	            elemento.setValorPago(proj.getDouble("regi_valor_pago"));
	            elemento.setValorCusto(proj.getDouble("regi_valor_custo"));
	            elemento.getCartao().setId(proj.getInt("cart_id"));
	            elemento.getVinculo().setId(proj.getInt("vinc_id"));
	            lista.add(elemento);
	        }
			return lista;
			
		} catch (JSONException e) {
			e.printStackTrace();
			return null;
		}
		
	}
	
	
	

}
