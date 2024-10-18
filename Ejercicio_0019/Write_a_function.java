package Ejercicio_0019;

import javax.swing.JOptionPane;

public class Write_a_function {
    public static void main(String[] args) {
        int year = Integer.parseInt(JOptionPane.showInputDialog("\nEscribe el año:\n"));

        boolean texto = false;
        
        if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
            texto = true;
        }

        JOptionPane.showMessageDialog(null, texto);
    }
}