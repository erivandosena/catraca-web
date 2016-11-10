package br.edu.unilab.catraca.controller.recurso;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.ClientResponse;
import com.sun.jersey.api.client.WebResource;
import sun.misc.BASE64Encoder;

public class JerseyClientGet {

	public static void main(String a[]){
        
        String url = "http://10.5.0.123:27289/api/cartao/jcartao";
        String name = "catraca";
        String password = "CaTr@CaUniLab2015";
        String authString = name + ":" + password;
        String authStringEnc = new BASE64Encoder().encode(authString.getBytes());
        System.out.println("Base64 encoded auth string: " + authStringEnc);
        Client restClient = Client.create();
        WebResource webResource = restClient.resource(url);
        ClientResponse resp = webResource.accept("application/json")
                                         .header("Authorization", "Basic " + authStringEnc)
                                         .get(ClientResponse.class);
        if(resp.getStatus() != 200){
            System.err.println("Unable to connect to the server");
        }
        System.out.println("Teste");
        String output = resp.getEntity(String.class);
        System.out.println("response: "+output);
        
        
        JSONArray projectArray;
		try {
			projectArray = new JSONArray(output.substring(11));
			
			for (int i = 0; i < projectArray.length(); i++) {
	            JSONObject proj = projectArray.getJSONObject(i);
	            System.out.println("ID:"+proj.getString("cart_id")+", Numero:"+proj.getString("cart_numero"));
	        }
			System.out.println();
		} catch (JSONException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
        
        
    }
}