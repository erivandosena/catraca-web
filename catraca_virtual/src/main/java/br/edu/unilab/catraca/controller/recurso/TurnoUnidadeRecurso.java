package br.edu.unilab.catraca.controller.recurso;

import java.sql.Connection;
import java.util.ArrayList;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.ClientResponse;
import com.sun.jersey.api.client.WebResource;

import br.edu.unilab.catraca.dao.CatracaDAO;
import br.edu.unilab.catraca.dao.CatracaUnidadeDAO;
import br.edu.unilab.catraca.dao.TurnoUnidadeDAO;
import br.edu.unilab.unicafe.model.TurnoUnidade;
import sun.misc.BASE64Encoder;

@SuppressWarnings("restriction")
public class TurnoUnidadeRecurso extends Recurso{

	private TurnoUnidadeDAO dao;
	
	public void sincronizar(Connection conexao){
		this.dao = new TurnoUnidadeDAO(conexao);
		ArrayList<TurnoUnidade> lista = this.obterLista();
		this.dao.limpar();
		if(lista == null)
			return;
		for (TurnoUnidade turnoUnidade : lista) {
			dao.inserir(turnoUnidade);
			
		}
	}
	

	public void sincronizar(){
		this.dao = new TurnoUnidadeDAO();

		
		this.dao.limpar();
		ArrayList<TurnoUnidade> lista = this.obterLista();
		for (TurnoUnidade turnoUnidade : lista) {
			dao.inserir(turnoUnidade);
			
		}
	}
	public ArrayList<TurnoUnidade> obterLista(){
		ArrayList<TurnoUnidade> lista = new ArrayList<TurnoUnidade>();
		
		String url = URL+"unidade_turno/unidades_turno";
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
			
			projectArray = new JSONArray(output.substring(18));
			for (int i = 0; i < projectArray.length(); i++) {
	            JSONObject proj = projectArray.getJSONObject(i);
	            TurnoUnidade turnoUnidade= new TurnoUnidade();
	            turnoUnidade.setId(proj.getInt("untu_id"));
	            turnoUnidade.setIdTurno(proj.getInt("turn_id"));
	            turnoUnidade.setIdUnidade(proj.getInt("unid_id"));
	            
	            lista.add(turnoUnidade);
	            
	        }
			return lista;
			
		} catch (JSONException e) {
			e.printStackTrace();
			return null;
		}
		
	}
	
}
