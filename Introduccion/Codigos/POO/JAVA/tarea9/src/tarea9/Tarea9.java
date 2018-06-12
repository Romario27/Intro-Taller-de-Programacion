
package tarea9;

import java.util.Scanner;

/**
 *
 * @author Romario
 */
public class Tarea9 {
    public Tarea9(){}
    public static void main(String[] args) {
        int suma=0;
        Scanner entrada = new Scanner(System.in);
        while(true){
            System.out.println("Ingrese el numero");
            int numero =entrada.nextInt();
            suma += numero;
            if (numero==0){break;} 
        }
        System.out.println("La suma es:" + suma);
    }
    
}
