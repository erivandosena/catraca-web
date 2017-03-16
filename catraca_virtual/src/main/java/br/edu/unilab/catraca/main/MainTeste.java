package br.edu.unilab.catraca.main;


import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.ClientResponse;
import com.sun.jersey.api.client.WebResource;

import sun.misc.BASE64Encoder;

public class MainTeste {

	public static void main(String[] args) {

		try {

			String url = URL;
	        String authString = USUARIO + ":" + SENHA;
			
	        @SuppressWarnings("restriction")
			String authStringEnc = new BASE64Encoder().encode(authString.getBytes());
	        
			Client client = Client.create();
			WebResource webResource = client.resource(url);
			
			String input = "{\"regi_data\":\"2017-01-09 09:41:30\",\"regi_valor_pago\":\"2\", \" regi_valor_custo\":\"3\", \"catr_id\":\"1\", \"cart_id\":\"52\", \"vinc_id\":\"52\"}";
			
			System.out.println(input);
	        System.out.println(url);
	        
			ClientResponse response = webResource.accept("application/json").header("Authorization", "Basic " + authStringEnc).post(ClientResponse.class, input);
	
			
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


	
	public static final String URL = "http://10.5.0.123:27289/api/v1/registro/insere";
	public static final String USUARIO = "catraca";
	public static final String SENHA = "CaTr@CaUniLab2015";
	

}
