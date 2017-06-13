package br.edu.unilab.catraca.verificador_de_conexao;

public class TestClient {
	
	public static void main(String[] args) {
		
		Cliente c = new Cliente();
		if(c.testar()){
			
			System.out.println("Valeu");
		}
		else{
			System.out.println("Nao valeu");
		}
	}

}
