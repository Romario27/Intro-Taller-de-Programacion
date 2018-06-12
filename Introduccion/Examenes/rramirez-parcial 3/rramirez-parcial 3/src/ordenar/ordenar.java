package ordenar;

import java.util.Scanner;

/**
 *
 * @author Romario
 */
public class ordenar {
    public ordenar(){}
    public static void main(String[] args) {
        ordenar ord=new ordenar();
        Scanner entrada=new Scaner(System.in);
        System.out.println("ingrese el array");
        int [] array=entrada.nextInt();
        int [] ordenada= ord.proceso(array);
        System.out.println("El array ordenado es:" + ordenada);
    }
    
    public int proceso(int array){
    }
}
