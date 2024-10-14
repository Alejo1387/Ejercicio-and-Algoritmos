package Ejercicio_0014;

import javax.swing.JOptionPane;
import java.util.ArrayList;

public class Convert_a_string_to_an_array {
    public static void main(String[] args) {
        String texto = JOptionPane.showInputDialog("\nIntroduce el String:\n");
        String textoNuevo = texto + " ";
        
        String textoArray = "";
        ArrayList<String> array = new ArrayList<>();

        for (int i = 0; i<textoNuevo.length(); i++) {
            if (textoNuevo.charAt(i) != ' ') {
                textoArray = textoArray + textoNuevo.charAt(i);
            } else if (textoNuevo.charAt(i) == ' ') {
                if (!textoArray.isEmpty()) {
                    array.add(textoArray);
                }
                textoArray = "";
            }
        }

        JOptionPane.showMessageDialog(null, "\nTexto: "+texto+"\n\nArray: "+array);
    }
}