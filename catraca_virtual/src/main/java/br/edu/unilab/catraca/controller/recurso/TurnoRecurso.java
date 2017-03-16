package br.edu.unilab.catraca.controller.recurso;

import java.sql.Connection;
import java.util.ArrayList;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.ClientResponse;
import com.sun.jersey.api.client.WebResource;

import br.edu.unilab.catraca.dao.TurnoDAO;
import br.edu.unilab.unicafe.model.Turno;
import sun.misc.BASE64Encoder;

@SuppressWarnings("restriction")
public class TurnoRecurso extends Recurso{
	private TurnoDAO dao;
	
	
	public void sincronizar(){
		this.dao = new TurnoDAO();
		ArrayList<Turno> lista = this.obterLista();
		if(lista == null){
			return;
		}
		this.dao.limpar();
		for (Turno turno : lista) {
			dao.inserir(turno);
		}
	}
	public void sincronizar(Connection conexao){
		this.dao = new TurnoDAO();
		ArrayList<Turno> lista = this.obterLista();
		this.dao.limpar();
		if(lista == null){
			return;
		}

		for (Turno turno : lista) {
			dao.inserir(turno);
		}
	}
	public ArrayList<Turno> obterLista(){
		ArrayList<Turno> lista = new ArrayList<Turno>();
		
		String url = URL+"turno/turnos";
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
			
			projectArray = new JSONArray(output.substring(10));
			for (int i = 0; i < projectArray.length(); i++) {
	            JSONObject proj = projectArray.getJSONObject(i);
	            Turno turno = new Turno();
	            turno.setId(proj.getInt("turn_id"));
	            turno.setDescricao(proj.getString("turn_descricao"));
	            turno.setHoraInicial(proj.getString("turn_hora_inicio"));
	            turno.setHoraFinal(proj.getString("turn_hora_fim"));
	            lista.add(turno);
	            
	        }
			return lista;
			
		} catch (JSONException e) {
			e.printStackTrace();
			return null;
		}
		
	}
	
	

}
