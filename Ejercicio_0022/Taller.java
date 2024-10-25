import javax.swing.JOptionPane;

public class Taller {
    public static void main(String[] args) {

        int numeroIterador = Integer.parseInt(JOptionPane.showInputDialog(null,"\nDime la cantidad de estudiantes:\n", "Nota final - Politecnico Mayor", JOptionPane.INFORMATION_MESSAGE));
        
        String mensaje = "";
        String materia2 = "";
        double notaFinal1 = 0;
        double notaFinal2 = 0;
        double notaFinal3 = 0;
        double notaFinal = 0;

        for (int i = 0; i < numeroIterador; i++) {

            String nombre = JOptionPane.showInputDialog(null,"\nDime el nombre del " + (i+1) + " estudiantes:\n", "Nota final - Politecnico Mayor", JOptionPane.INFORMATION_MESSAGE);
            String apellido = JOptionPane.showInputDialog(null,"\nDime el apellido de " + (nombre) + "\n", "Nota final - Politecnico Mayor", JOptionPane.INFORMATION_MESSAGE);
            mensaje += "Estudiante "+(i+1)+":  "+nombre+" "+apellido+"\n\n";

            for (int j = 1; j < 5; j++) {
                if (j == 1) {
                    materia2 = "Programación 1:";
                    mensaje += materia2+"\n";
                } else if (j== 2) {
                    materia2 = "Programación 2:";
                    mensaje += materia2+"\n";
                } else if (j == 3) {
                    materia2 = "Estructura de datos:";
                    mensaje += materia2+"\n";
                }

                int k = 0;
                if (j <= 3) {
                    double nota1 = Double.parseDouble(JOptionPane.showInputDialog(null,"\nDime la nota " + (k+1) + " de " + (nombre) + " de la materia: " + materia2 + "\n", "Nota final - Politecnico Mayor", JOptionPane.INFORMATION_MESSAGE));
                    mensaje += "Nota corte 1: " + String.format("%.0f", nota1) + "\n";

                    double nota2 = Double.parseDouble(JOptionPane.showInputDialog(null,"\nDime la nota " + (k+2) + " de " + (nombre) + " de la materia: " + materia2 + "\n", "Nota final - Politecnico Mayor", JOptionPane.INFORMATION_MESSAGE));
                    mensaje += "Nota corte 2: " + String.format("%.0f", nota2) + "\n";

                    double nota3 = Double.parseDouble(JOptionPane.showInputDialog(null,"\nDime la nota " + (k+3) + " de " + (nombre) + " de la materia: " + materia2 + "\n", "Nota final - Politecnico Mayor", JOptionPane.INFORMATION_MESSAGE));
                    mensaje += "Nota corte 3: " + String.format("%.0f", nota3) + "\n";

                    if (j == 1) {
                        notaFinal1 = (((nota1*1.2)+(nota2*1.05)+(nota3*1.2)) / (1.2+1.05+1.2));
                        mensaje += "Nota final: "+String.format("%.0f", notaFinal1) + "\n\n";
                    } else if (j == 2) {
                        notaFinal2 = (((nota1*1.2)+(nota2*1.05)+(nota3*1.2)) / (1.2+1.05+1.2));
                        mensaje += "Nota final: "+String.format("%.0f", notaFinal2) + "\n\n";
                    } else if (j == 3) {
                        notaFinal3 = (((nota1*1.2)+(nota2*1.05)+(nota3*1.2)) / (1.2+1.05+1.2));
                        mensaje += "Nota final: "+String.format("%.0f", notaFinal3) + "\n\n";
                    }
                } else {
                    notaFinal = (notaFinal1 + notaFinal2 + notaFinal3) / 3;
                    mensaje += "promedio: "+String.format("%.0f", notaFinal) + "\n\n";
                    if (notaFinal > 80 || notaFinal > 4.0) {
                        mensaje += "Nota mayor a 4.0 o 80%.  Obtiene un beneficio de descuento de matricula el siguiente semestre.      \n\n\n";
                    }
                }
            }

        }

        JOptionPane.showMessageDialog(null, mensaje, "Nota final - Politecnico Mayor", JOptionPane.INFORMATION_MESSAGE);
    }
}
