package br.edu.unilab.catraca.main;

import java.util.ArrayList;

import br.edu.unilab.catraca.controller.CatracaVirtualController;
import br.edu.unilab.catraca.recurso.CartaoRecurso;
import br.edu.unilab.catraca.recurso.CatracaRecurso;
import br.edu.unilab.catraca.view.CatracaVirtualView;
import br.edu.unilab.unicafe.model.Cartao;
import br.edu.unilab.unicafe.model.Catraca;

public class Teste {

	public static void main(String[] args) {
		CatracaVirtualController controller = new CatracaVirtualController();
		controller.iniciar();
		
//		CatracaRecurso r = new CatracaRecurso();
//		for(Catraca c : r.obterLista()){
//			System.out.println(c.getNome());
//		}

	}

}
