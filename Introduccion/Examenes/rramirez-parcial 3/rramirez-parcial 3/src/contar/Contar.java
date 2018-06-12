package contar;

import java.util.Scanner;

/**
 *
 * @author Romario
 */
public class Contar {
    public Contar(){}
    public static void main(String[] args) {
        Contar cont=new Contar();
        int digitos=cont.ope();
        System.out.println("Tiene"+digitos+"digitos");
    }
    public int ope(){
        Scanner entrada=new Scanner(System.in);
        System.out.println("Ingrese el numero");
        int num=entrada.nextInt();
        int cont=0;
        while (num!=0){
            cont+=1;
            num=num/10;
        }
        return cont;
    }
}
