package br.edu.unilab.catraca.controller.recurso;

import java.sql.Connection;
import java.util.ArrayList;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.ClientResponse;
import com.sun.jersey.api.client.WebResource;

import br.edu.unilab.catraca.dao.VinculoDAO;
import br.edu.unilab.unicafe.model.Vinculo;
import sun.misc.BASE64Encoder;

public class VinculoRecurso extends Recurso{
	
	private VinculoDAO dao;
	
	public void sincronizar(){
		this.dao = new VinculoDAO();
		this.dao.limpar();
		ArrayList<Vinculo> lista = this.obterLista();
		
		for (Vinculo elemento : lista) {
			
			if(!this.dao.inserir(elemento)){
				System.out.println("Erro ao tentar inserir vinculo. ");
			}
		}
		
	}
	public void sincronizar(Connection conexao){
		this.dao = new VinculoDAO(conexao);
		this.dao.limpar();
		ArrayList<Vinculo> lista = this.obterLista();
		
		for (Vinculo elemento : lista) {
			
			if(!this.dao.inserir(elemento)){
				System.out.println("Erro ao tentar inserir vinculo. ");
			}
		}
		
	}
	
	
	public ArrayList<Vinculo> obterLista(){
		ArrayList<Vinculo> lista = new ArrayList<Vinculo>();
		
		String url = URL+"/vinculo/vinculos/tipo";
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
        try {
			JSONObject jo = new JSONObject(output);
			output = jo.getString("vinculos");

		} catch (JSONException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
        JSONArray projectArray;
		try {
			projectArray = new JSONArray(output);
			for (int i = 0; i < projectArray.length(); i++) {
				
	            JSONObject proj = projectArray.getJSONObject(i);
	            Vinculo elemento = new Vinculo();
	            elemento.setId(proj.getInt("vinc_id"));
	            elemento.setAvulso(proj.getBoolean("vinc_avulso"));
	            elemento.setInicioValidade(proj.getString("vinc_inicio"));
	            elemento.setFinalValidade(proj.getString("vinc_fim"));
	            elemento.setDescricao(proj.getString("vinc_descricao"));
	            elemento.setQuantidadeDeAlimentosPorTurno(proj.getInt("vinc_refeicoes"));
	            elemento.getCartao().setId(proj.getInt("cart_id"));
	            elemento.getResponsavel().setId(proj.getInt("usua_id"));
	            elemento.getCartao().getTipo().setId(proj.getInt("tipo_id"));
	            
	            
	            lista.add(elemento);
	        }			
			return lista;
			
			
		} catch (JSONException e) {
			e.printStackTrace();
			return null;
		}
		
	}
}
