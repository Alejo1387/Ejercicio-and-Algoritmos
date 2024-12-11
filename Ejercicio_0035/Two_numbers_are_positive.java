package Ejercicio_0035;

import javax.swing.JOptionPane;

public class Two_numbers_are_positive {
    public static void main(String[] args) {
        String numbers = "(";
        byte n = 0;

        int num = Integer.parseInt(JOptionPane.showInputDialog("\nDame el 1 numero:\n"));
        if(num > 0) {
            n += 1;
        }
        numbers += Integer.toString(num) + ", ";

        num = Integer.parseInt(JOptionPane.showInputDialog("\nDame el 2 numero:\n"));
        if(num > 0) {
            n += 1;
        }
        numbers += Integer.toString(num) + ", ";

        num = Integer.parseInt(JOptionPane.showInputDialog("\nDame el 1 numero:\n"));
        if(num > 0) {
            n += 1;
        }
        numbers += Integer.toString(num) + ")";

        if (n == 2) {
            JOptionPane.showMessageDialog(null, numbers + "  ->  True");
        } else {
            JOptionPane.showMessageDialog(null, numbers + "  ->  False");
        }
    }
}