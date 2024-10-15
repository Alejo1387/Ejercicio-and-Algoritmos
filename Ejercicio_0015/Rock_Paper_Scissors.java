package Ejercicio_0015;

import javax.swing.JOptionPane;
import java.util.Random;

public class Rock_Paper_Scissors {
    public static void main(String[] args) {
        Random random = new Random();
        int opcion_machina = random.nextInt(3) + 1;
        String opcion_machina2 = "";
        switch (opcion_machina) {
            case 1 -> opcion_machina2 = "Tijera";
            case 2 -> opcion_machina2 = "Papel";
            case 3 -> opcion_machina2 = "Piedra";
        }

        String Mensaje1 = """
                Vamos a jugar Piedra, Papel y Tijera, estas son las opciones:

                    1. Piedra
                    2. Papel
                    3. Tijera

                Elije la opcion numerica:

                """;
        
        int opcion_person = Integer.parseInt(JOptionPane.showInputDialog(Mensaje1));

        String opcion_person2 = "";

        switch (opcion_person) {
            case 1 -> opcion_person2 = "Piedra";
            case 2 -> opcion_person2 = "Papel";
            case 3 -> opcion_person2 = "Tijera";
        }

        if (opcion_machina2 == opcion_person2){
            String mensaje2 = "\nMaquina:    "+opcion_machina2+"\nTú:    "+opcion_person2+"\nResultado:    Empate!!";
            JOptionPane.showMessageDialog(null, mensaje2);
        } else if (opcion_machina2 == "Papel") {
            if (opcion_person2 == "Tijera") {
                String mensaje2 = "\nMaquina:    "+opcion_machina2+"\nTú:    "+opcion_person2+"\nResultado:    Ganaste!!";
                JOptionPane.showMessageDialog(null, mensaje2);
            } else if (opcion_person2 == "Piedra") {
                String mensaje2 = "\nMaquina:    "+opcion_machina2+"\nTú:    "+opcion_person2+"\nResultado:    Perdiste!!";
                JOptionPane.showMessageDialog(null, mensaje2);
            }
        } else if (opcion_machina2 == "Piedra") {
            if (opcion_person2 == "Papel") {
                String mensaje2 = "\nMaquina:    "+opcion_machina2+"\nTú:    "+opcion_person2+"\nResultado:    Ganaste!!";
                JOptionPane.showMessageDialog(null, mensaje2);
            } else if (opcion_person2 == "Tijera") {
                String mensaje2 = "\nMaquina:    "+opcion_machina2+"\nTú:    "+opcion_person2+"\nResultado:    Perdiste!!";
                JOptionPane.showMessageDialog(null, mensaje2);
            }
        } else if (opcion_machina2 == "Tijera") {
            if (opcion_person2 == "Piedra") {
                String mensaje2 = "\nMaquina:    "+opcion_machina2+"\nTú:    "+opcion_person2+"\nResultado:    Ganaste!!";
                JOptionPane.showMessageDialog(null, mensaje2);
            } else if (opcion_person2 == "Papel") {
                String mensaje2 = "\nMaquina:    "+opcion_machina2+"\nTú:    "+opcion_person2+"\nResultado:    Perdiste!!";
                JOptionPane.showMessageDialog(null, mensaje2);
            }
        }

        
    }
}