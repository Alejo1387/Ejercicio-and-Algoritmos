package Ejercicio_0034;

import javax.swing.JOptionPane;

public class Opposite_number {
    public static void main(String[] args) {
        String num = JOptionPane.showInputDialog("\nEscribe el numero:\n");

        float num2 = Float.parseFloat(num);

        if (num2 == 0) {
            JOptionPane.showMessageDialog(null, "\nEl 0 no tiene contraparte\n");
        } else if (num2 > 0){
            JOptionPane.showMessageDialog(null, "\nNumero: " + num + "\n\nContraparte: -" + num + "\n");
        } else {
            JOptionPane.showMessageDialog(null, "\nNumero: " + num + "\n\nContraparte: " + num.substring(1) + "\n");
        }
    }
}