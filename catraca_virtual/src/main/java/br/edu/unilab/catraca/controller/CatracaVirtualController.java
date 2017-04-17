package br.edu.unilab.catraca.controller;


public class CatracaVirtualController {
	public int estado;
	
	public CatracaVirtualController(){
		this.estado = ESTADO_ONLINE;
	}
	
	public void iniciar(){
		
	}
	
	public static final int ESTADO_OFFLINE = 0;
	public static final int ESTADO_ONLINE = 1;
	
	
}
