package Ejercicio_0017;

import javax.swing.JOptionPane;
import java.util.Arrays;

public class Find_Maximum_and_Minimum_Values_of_a_List {
    public static void main(String[] args) {
        int cantidad_array = Integer.parseInt(JOptionPane.showInputDialog("\nDime la cantidad de numeros en el array:\n"));
        
        int[] array = new int[cantidad_array];
        
        for (int i = 0; i < cantidad_array; i++) {
            int num = Integer.parseInt(JOptionPane.showInputDialog("\nDime el "+(i+1)+" elemento del array:\n"));
            array[i] = num;
        }

        int min = array[0];
        int max = array[0];

        for(int i = 0; i < cantidad_array; i++) {
            if (array[i] < min){
                min = array[i];
            }
            if (array[i] > max) {
                max = array[i];
            }
        }

        String mensaje = String.format("""
        Array:
        %s

        Numero minimo:
        %d

        Numero maximo:
        %d
        """, Arrays.toString(array), min, max);

        JOptionPane.showMessageDialog(null, mensaje);
    }
}
