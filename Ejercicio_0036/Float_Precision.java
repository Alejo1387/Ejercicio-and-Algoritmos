package Ejercicio_0036;

import javax.swing.JOptionPane;

public class Float_Precision {
    public static void main(String[] args) {
        double num = Float.parseFloat(JOptionPane.showInputDialog("\nDame un numero decimal:\n"));

        String result = String.format("%.2f", num);

        JOptionPane.showMessageDialog(null, "Decimal:  " + result);
    }
}