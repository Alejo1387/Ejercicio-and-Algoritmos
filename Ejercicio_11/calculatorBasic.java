package Ejercicio_11;

import javax.swing.JOptionPane;

public class calculatorBasic {
    public static void main(String[] args) {
        int num1 = Integer.parseInt(JOptionPane.showInputDialog("Dame el primer numero:"));
        int num2 = Integer.parseInt(JOptionPane.showInputDialog("Dame el segundo numero:"));
        String signo_texto = JOptionPane.showInputDialog("Dime el signo:");
        char signo = signo_texto.charAt(0);
        if (signo == '+') {
            JOptionPane.showMessageDialog(null, num1+num2);
        } else if (signo == '-') {
            JOptionPane.showMessageDialog(null, num1-num2);
        } else if (signo == '*') {
            JOptionPane.showMessageDialog(null, num1*num2);
        } else if (signo == '/') {
            JOptionPane.showMessageDialog(null, num1/num2);
        } else {
            JOptionPane.showMessageDialog(null, "    ERROR    ");
        }
    }
}
