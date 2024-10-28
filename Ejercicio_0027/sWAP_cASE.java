package Ejercicio_0027;

import javax.swing.JOptionPane;

public class sWAP_cASE {
    public static void main(String[] args) {
        String texto = JOptionPane.showInputDialog("\nIntruce la cadena:\n");

        String new_tex = "";

        for (int i = 0; i < texto.length(); i++) {
            char c = texto.charAt(i);

            if (c >= 'A' && c <= 'Z') {
                new_tex += (char) (c + 32);
            } else if (c >= 'a' && c <= 'z') {
                new_tex += (char) (c - 32);
            } else {
                new_tex += c;
            }
        }

        JOptionPane.showMessageDialog(null, "\nTexto normal:\n" + texto + "\n\n texto modificado:\n" + new_tex);
    }
}