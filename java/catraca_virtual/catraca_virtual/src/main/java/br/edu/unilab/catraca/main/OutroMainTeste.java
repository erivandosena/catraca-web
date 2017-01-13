package br.edu.unilab.catraca.main;

import org.json.JSONException;
import org.json.JSONObject;

import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.ClientResponse;
import com.sun.jersey.api.client.WebResource;

import br.edu.unilab.catraca.controller.recurso.RegistroRecurso;
import br.edu.unilab.unicafe.model.Registro;
import sun.misc.BASE64Encoder;

public class OutroMainTeste {

	public static void main(String[] args) {
		RegistroRecurso recurso = new RegistroRecurso();
		recurso.enviar(new Registro());
		try {

			String url = URL;
	        String authString = USUARIO + ":" + SENHA;
			
	        @SuppressWarnings("restriction")
			String authStringEnc = new BASE64Encoder().encode(authString.getBytes());
	        
			Client client = Client.create();
			WebResource webResource = client.resource(url);
			
			String input = "{\"regi_data\":\"2017-01-09 09:41:30\",\"regi_valor_pago\":\"2\", \" regi_valor_custo\":\"3\", \"catr_id\":\"1\", \"cart_id\":\"52\", \"vinc_id\":\"52\"}";
			JSONObject jsonObject = new JSONObject();
			try {
				jsonObject.put("regi_data", "2017-01-09 09:41:30");
				
			} catch (JSONException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			System.out.println(jsonObject.toString());
			
			
			
			System.out.println(input);
	        System.out.println(url);
	        
			ClientResponse response = webResource.accept("application/json").header("Authorization", "Basic " + authStringEnc).put(ClientResponse.class, input);
	
			
			if (response.getStatus() != 200) {
				throw new RuntimeException("Failed : HTTP error code : " + response.getStatus());
			}

			System.out.println("Output from Server .... \n");
			String output = response.getEntity(String.class);
			System.out.println(output);

		} catch (Exception e) {

			e.printStackTrace();

		}
	}

	
	public static final String URL = "http://10.5.0.123:27289/cartao/atualiza/debito/";
	public static final String USUARIO = "catraca";
	public static final String SENHA = "CaTr@CaUniLab2015";
	

}
