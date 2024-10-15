package Ejercicio_0016;

import javax.swing.JOptionPane;

public class Potenciation {
    public static void main(String[] args) {
        int num1 = Integer.parseInt(JOptionPane.showInputDialog("\nDame el numero de la base de la potencia:\n\n"));

        while (num1 < 0) {
            num1 = Integer.parseInt(JOptionPane.showInputDialog("\nSolo numero natural para base de la potencia:\n\n"));
        }

        int num2 = Integer.parseInt(JOptionPane.showInputDialog("\nDame el numero de la potencia:\n\n"));

        while (num2 < 0) {
            num2 = Integer.parseInt(JOptionPane.showInputDialog("\nSolo numero natural para de la potencia:  \n\n"));
        }

        int result = num1;

        if (num1 == 0) {
            if (num2 == 0) {
                result = 1;
            } else {
                result = 0;
            }
        } else if (num2 == 0) {
            result = 1;
        } else {
            int i = 1;
            while (i < num2) {
                result *= num1;
                i +=1;
            }
        }

        String mensaje = String.format("""
          %d    
        %d      es igual a %d

        """, num2, num1, result);

        JOptionPane.showMessageDialog(null, mensaje);
    }
}