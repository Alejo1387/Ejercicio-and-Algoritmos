package Ejercicio_0020;

import java.util.Arrays;
import javax.swing.JOptionPane;

public class Find_the_Runner_Up_Score {
    public static void main(String[] args) {
        int cantidadNum = Integer.parseInt(JOptionPane.showInputDialog("\nDime la cantidad de numeros en el array:\n"));

        int[] array = new int[cantidadNum];

        for (int i = 0; i < cantidadNum; i++) {
            int num = Integer.parseInt(JOptionPane.showInputDialog("\nDime el "+(i+1)+" numero del array:\n"));
            array[i] = num;
        }

        int min = array[0];

        for (int j = 0; j < cantidadNum; j++) {
            if (array[j] < min) {
                min = array[j];
            }
        }

        int max2 = min;

        int max = array[0];
        for (int k = 0; k < cantidadNum; k++) {
            if (array[k] > max) {
                max2 = max;
                max = array[k];
            } else if (array[k] >= max2 && array[k] < max) {
                max2 = array[k];
            }
        }

        String mensaje = String.format("""
        Array:
        %s

        Segundo lugar:
        %d
        """, Arrays.toString(array), max2);

        JOptionPane.showMessageDialog(null, mensaje);
    }
}
