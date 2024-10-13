package Ejercicio_0013;

import javax.swing.JOptionPane;

public class Quadrants {
    public static void main(String[] args) {
        double X = Float.parseFloat(JOptionPane.showInputDialog("Dime el numero de X:\n"));
        while (X==0) {
            X = Float.parseFloat(JOptionPane.showInputDialog("Dime el numero distinto a 0:\n"));
        }

        double Y = Float.parseFloat(JOptionPane.showInputDialog("Dime el numero de Y:\n"));
        while (Y==0) {
            Y = Float.parseFloat(JOptionPane.showInputDialog("Dime el numero distinto a 0:\n"));
        }

        if (X>0 && Y>0) {
            JOptionPane.showMessageDialog(null, "\nLos datos ("+X+", "+Y+") estan en el cuadrante 1");
        } else if (X<0 && Y>0) {
            JOptionPane.showMessageDialog(null, "\nLos datos ("+X+", "+Y+") estan en el cuadrante 2");
        } else if (X<0 && Y<0) {
            JOptionPane.showMessageDialog(null, "\nLos datos ("+X+", "+Y+") estan en el cuadrante 3");
        } else {
            JOptionPane.showMessageDialog(null, "\nLos datos ("+X+", "+Y+") estan en el cuadrante 3");
        }
    }
}