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

		Date hora = new Date();
		
		System.out.println(hora.toString());
//		

		
		TurnoDAO dao = new TurnoDAO();
		ArrayList<Turno> lista = dao.retornaLista();
		String dataTexto = lista.get(0).getHoraInicial();
		
		
		Date data = null;
		
		
		SimpleDateFormat format = new SimpleDateFormat("HH:mm:ss");
		format.setLenient(false);
		try {
			data = format.parse(dataTexto);
		} catch (ParseException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	
		
		if(data.before(hora)){
			System.out.println("Antes");
		}
////		
////		
////	
////		
////		 Calendar calendar = new GregorianCalendar();
////		 SimpleDateFormat out = new SimpleDateFormat("HH:mm:ss");
////		 calendar.setTime(data);
////		
//		  
//		 System.out.println(out.format(calendar.getTime()));
//		 
	}

}
