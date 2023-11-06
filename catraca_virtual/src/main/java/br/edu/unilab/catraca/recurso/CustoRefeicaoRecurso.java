package br.edu.unilab.catraca.recurso;

import java.sql.Connection;
import java.util.ArrayList;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.ClientResponse;
import com.sun.jersey.api.client.WebResource;

import br.edu.unilab.catraca.dao.CustoRefeicaoDAO;
import br.edu.unilab.unicafe.model.CustoRefeicao;
import sun.misc.BASE64Encoder;

public class CustoRefeicaoRecurso extends Recurso{
	
	private CustoRefeicaoDAO dao;
	
	public void sincronizar(){
		this.dao = new CustoRefeicaoDAO();
		
		this.dao.limpar();
		ArrayList<CustoRefeicao> lista = this.obterLista();
		for (CustoRefeicao custoRefeicao : lista) {
			dao.inserir(custoRefeicao);
		}
	}
	
	public void sincronizar(Connection connection){
		this.dao = new CustoRefeicaoDAO(connection);
		this.dao.limpar();
		ArrayList<CustoRefeicao> lista = this.obterLista();
		for (CustoRefeicao custoRefeicao : lista) {
			dao.inserir(custoRefeicao);
		}
	}
	
	public ArrayList<CustoRefeicao> obterLista(){
		ArrayList<CustoRefeicao> lista = new ArrayList<CustoRefeicao>();
		
		String url = URL+"custo_refeicao/custos_refeicao";
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
			output = jo.getString("custos_refeicao");

		} catch (JSONException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
        
        JSONArray projectArray;
		try {
			
			projectArray = new JSONArray(output);
			for (int i = 0; i < projectArray.length(); i++) {
	            JSONObject proj = projectArray.getJSONObject(i);
	            CustoRefeicao custoRefeicao = new CustoRefeicao();
	            custoRefeicao.setId(proj.getInt("cure_id"));
	            custoRefeicao.setValor(proj.getDouble("cure_valor"));
	            custoRefeicao.setData(proj.getString("cure_data"));
	            lista.add(custoRefeicao);
	            
	        }
			return lista;
			
		} catch (JSONException e) {
			e.printStackTrace();
			return null;
		}
		
	}

}
