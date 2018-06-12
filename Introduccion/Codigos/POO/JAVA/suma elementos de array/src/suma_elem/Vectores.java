/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package suma_elem;

import java.util.Scanner;

public class Vectores {
   
    public Vectores(){}
    public int[] llenarArray(){
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese la longitud del vector");
        int longitud =entrada.nextInt();
        int[] vector = new int[longitud];
        for(int contador = 0; contador < vector.length; contador++){
            System.out.println("Ingrese el valor del array para la posición " 
                                + contador);
            vector[contador] = entrada.nextInt();
        }
        return vector;
    }
    public int sumarElementos(int[] vector1){
        int suma = 0;
        for(int contador = 0; contador < vector1.length; contador++){
           suma += vector1[contador];
        }
        return suma;
    }    
    public static void main(String[] args){
        Vectores vect = new Vectores();
        System.out.println("Llenar valores del array 1");
        int[] vector1 = vect.llenarArray();   
        int resultado = vect.sumarElementos(vector1);  
        System.out.println("La suma es:" + resultado);
    }
}
