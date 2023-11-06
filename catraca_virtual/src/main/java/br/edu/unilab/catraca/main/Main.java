package br.edu.unilab.catraca.main;



import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.nio.channels.FileLock;
import java.util.ArrayList;

import br.edu.unilab.catraca.controller.CatracaVirtualController;
import br.edu.unilab.catraca.dao.CartaoDAO;
import br.edu.unilab.catraca.recurso.CartaoRecurso;
import br.edu.unilab.catraca.recurso.CatracaRecurso;
import br.edu.unilab.catraca.recurso.CatracaUnidadeRecurso;
import br.edu.unilab.catraca.recurso.TipoRecurso;
import br.edu.unilab.catraca.recurso.UnidadeRecurso;
import br.edu.unilab.catraca.recurso.UsuarioRecurso;
import br.edu.unilab.catraca.recurso.VinculoRecurso;
import br.edu.unilab.catraca.verificador_de_conexao.Cliente;
import br.edu.unilab.unicafe.model.Cartao;
import br.edu.unilab.unicafe.model.Tipo;
import br.edu.unilab.unicafe.model.Usuario;



/**
 * 
 * @author Jefferson
 *
 */

public class Main {

	@SuppressWarnings("resource")
	public static void main(String[] args) {
		
		File f = new File(".lock");
		FileLock lock = null;
		try {
			f.createNewFile();
			lock = new RandomAccessFile(f, "rw").getChannel().tryLock();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		if (lock != null) {
			Cliente c = new Cliente();
			c.iniciar();
		} else {
			System.out.println("Ja ha uma instancia rodando");
		}
	}

}
