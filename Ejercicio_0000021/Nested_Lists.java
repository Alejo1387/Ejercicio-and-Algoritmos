package Ejercicio_000021;

import javax.swing.JOptionPane;

public class Nested_Lists{
    public static void main(String[] args) {
        int n = Integer.parseInt(JOptionPane.showInputDialog("\nDime la cantidad de estudiantes:\n"));

        String[] arrayName = new String[n];
        int[] arrayNumber = new int[n];

        for (int i = 0; i < n; i++) {
            String name = JOptionPane.showInputDialog("\nDime el nombre del" + (i+1) + " estudiante:\n");
        }
    }
}