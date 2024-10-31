package Ejercicio_0028;

import javax.swing.JOptionPane;

public class String_Split_and_Join {
    public static void main(String[] args) {
        String entrada = JOptionPane.showInputDialog("\nIntroduce la cadena de texto:\n");

        String[] espace = entrada.split(" ");

        String ouput = String.join("-", espace);

        String mensaje = String.format("""
                texto:
                %s

                Resultado:
                %s
                """, entrada, ouput);

        JOptionPane.showMessageDialog(null, mensaje);
    }
}