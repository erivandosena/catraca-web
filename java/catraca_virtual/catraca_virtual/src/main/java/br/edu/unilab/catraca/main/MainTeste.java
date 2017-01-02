package br.edu.unilab.catraca.main;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;

import br.edu.unilab.catraca.controller.recurso.CartaoRecurso;
import br.edu.unilab.catraca.controller.recurso.CatracaUnidadeRecurso;
import br.edu.unilab.catraca.dao.TurnoDAO;
import br.edu.unilab.unicafe.model.Turno;

public class MainTeste {

	public static void main(String[] args) {
		
		CatracaUnidadeRecurso recurso = new CatracaUnidadeRecurso();
		recurso.sincronizar();
	}

}
