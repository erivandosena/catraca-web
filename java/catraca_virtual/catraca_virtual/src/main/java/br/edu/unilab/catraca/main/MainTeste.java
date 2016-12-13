package br.edu.unilab.catraca.main;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;

import br.edu.unilab.catraca.dao.TurnoDAO;
import br.edu.unilab.unicafe.model.Turno;

public class MainTeste {

	public static void main(String[] args) {

		Date horaAtual = new Date();
		SimpleDateFormat dataNoFrame = new SimpleDateFormat("dd/mm/yyyy HH:mm:ss");
		System.out.println(dataNoFrame.format(horaAtual));
//		 
	}

}
