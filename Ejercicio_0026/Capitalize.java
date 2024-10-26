package Ejercicio_0026;

import javax.swing.JOptionPane;

public class Capitalize {
    public static void main(String[] args) {
        String s = JOptionPane.showInputDialog("\nEscribe la cadena:\n");

        s += " ";
        String mesage = "";
        String texto = "";

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ') {
                mesage += texto.substring(0, 1).toUpperCase() + texto.substring(1).toLowerCase() + " ";
                texto = "";
            } else {
                texto += s.charAt(i);
            }
        }

        JOptionPane.showMessageDialog(null, "\nResultado:  " + mesage + "\n");
    }
}