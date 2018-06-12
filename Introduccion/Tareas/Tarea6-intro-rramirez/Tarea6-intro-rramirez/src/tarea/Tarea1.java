
package tarea1;

import java.util.Scanner;

public class Tarea1 {

    public static void main(String[] args) {
        operacionesfig oper = new operacionesfig();
        
        System.out.println("***Menú***");
        System.out.println("Calculo de Area");
        System.out.println("1- Circulo");
        System.out.println("2- Rectangulo");
        System.out.println("Ingrese la opcion que desea ejecutar");
        Scanner entrada= new Scanner(System.in);
        int opcion= entrada.nextInt();
        
        double resultado =0;
        
        switch (opcion){
            case 1:
                System.out.println("Ingrese el radio del circulo:");
                int radio= entrada.nextInt();
                resultado = oper.circulo(radio);
                System.out.println("El area del circulo es:"+resultado);
                break;
            case 2:
                System.out.println("Ingrese el largo del rectangulo:");
                int largo= entrada.nextInt();
                System.out.println("Ingrese el ancho del rectangulo:");
                int ancho= entrada.nextInt();
                resultado = oper.rectangulo(largo, ancho);
                System.out.println("El area del rectangulo es:"+resultado);
                break;
            default:
                System.out.println("Opcion no valida");
        }
    }
    
}
