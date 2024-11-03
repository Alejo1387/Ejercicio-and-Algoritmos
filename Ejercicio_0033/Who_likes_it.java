package Ejercicio_0033;

import javax.swing.JOptionPane;

public class Who_likes_it {
    public static void main(String[] args) {
        int num = Integer.parseInt(JOptionPane.showInputDialog("\nDime la cantidad de me gusta:\n"));
        
        String[] array_like = new String[num];
        
        for (int i = 0; i < num; i++) {
            array_like[i] = JOptionPane.showInputDialog("\nDime el " + (i+1) + " me gusta:\n");
        }

        if (num < 0) {
            JOptionPane.showMessageDialog(null, "\nError\n");
        } else if (num == 0) {
            JOptionPane.showMessageDialog(null, "\nNo one likes this\n");
        } else if (num >= 1 && num <= 3) {
            if (num == 1) {
                JOptionPane.showMessageDialog(null, "\n" + array_like[0] + " likes this\n");
            } else if (num == 2) {
                JOptionPane.showMessageDialog(null, "\n" + array_like[0] + " and " + array_like[1] + " likes this\n");
            } else {
                JOptionPane.showMessageDialog(null, "\n" + array_like[0] + ", " + array_like[1] + " and " + array_like[2] + " likes this\n");
            }
        } else {
            JOptionPane.showMessageDialog(null, "\n" + array_like[0] + ", " + array_like[1] + " and " + (num - 2) + " likes this\n");
        }
    }
}