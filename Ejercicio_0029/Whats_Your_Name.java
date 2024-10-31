package Ejercicio_0029;

import javax.swing.JOptionPane;

public class Whats_Your_Name {
    public static void main(String[] args) {
        String first = JOptionPane.showInputDialog("\nFirst name:\n");
        String last = JOptionPane.showInputDialog("\nLast name:\n");

        JOptionPane.showMessageDialog(null, "Hello "+first+" "+last+"! You just delved into Java.");
    }
}