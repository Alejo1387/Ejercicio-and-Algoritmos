package Ejercicio_0018;

import javax.swing.JOptionPane;
import java.util.Arrays;

public class Count_of_positives_sum_of_negatives {
    public static void main(String[] args) {
        int cantidad_array = Integer.parseInt(JOptionPane.showInputDialog("\nCantidad de numeros:\n"));

        int[] array = new int[cantidad_array];

        for (int i = 0; i < cantidad_array; i++) {
            int num = Integer.parseInt(JOptionPane.showInputDialog("\nDime el "+(i+1)+" elemento del array:\n"));
            array[i] = num;
        }

        int can_pos = 0;
        int neg = 0;

        for (int i = 0; i < cantidad_array; i++) {
            if (array[i] > 0) {
                can_pos+=1;
            }
            if (array[i] < 0) {
                neg += array[i];
            }
        }

        String mensaje = String.format("""
        Array:
        %s

        Cantidad de positivos:
        %d

        Suma de negativos:
        %d
        """, Arrays.toString(array), can_pos, neg);

        JOptionPane.showMessageDialog(null, mensaje);
    }
}
