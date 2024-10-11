package Ejercicio_0012;

import javax.swing.JOptionPane;

public class Polish_alphabet {
    public static void main(String[] args) {
        String cadena = JOptionPane.showInputDialog("Escribe la cadena:");

        String[] polish = {"ą", "ć", "ę", "ł", "ń", "ó", "ś", "ź"};
        String[] replacements = {"a", "c", "e", "l", "n", "o", "s", "z"};

        String new_cadena = cadena;

        for (int i = 0; i < polish.length; i++) {
            new_cadena = new_cadena.replace(polish[i], replacements[i]);
        }

        JOptionPane.showMessageDialog(null, "Resultado: \n\n" + new_cadena);
    }
}
