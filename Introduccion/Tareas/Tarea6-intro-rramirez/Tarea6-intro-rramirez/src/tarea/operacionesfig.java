package tarea1;

public class operacionesfig {
    public operacionesfig(){}
    public int circulo(int radio){
        return (int) (Math.PI * Math.pow(radio,2));
    }
    public int rectangulo(int largo, int ancho){
        return largo * ancho;
    }
}