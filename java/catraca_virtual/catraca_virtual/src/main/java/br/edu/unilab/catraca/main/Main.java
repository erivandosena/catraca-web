package br.edu.unilab.catraca.main;



import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.nio.channels.FileLock;

import br.edu.unilab.catraca.dao.CartaoDAO;



/**
 * 
 * @author Jefferson
 *
 */

public class Main {

	public static void main(String[] args) {
		
		File f = new File(".lock");
		FileLock lock = null;
		try {
			f.createNewFile();
			lock = new RandomAccessFile(f, "rw").getChannel().tryLock();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		if (lock != null) {
			CartaoDAO dao = new CartaoDAO();
			dao.mostrar();
			
		} else {
			System.out.println("Ja ha uma instancia rodando");
		}
	}

}
