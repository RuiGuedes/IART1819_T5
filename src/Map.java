import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Map {
    
    private char[][] matrix;
    
    public Map() {
        String filename = read_input();
        System.out.println(filename);
        //String filename = "level.txt";
        
        read_file(filename);
    }

    private void read_file(String filename) {

            File fileLevel = new File(filename);

    }

    private String read_input() {
        Scanner reader = new Scanner(System.in);
        System.out.print("Enter level file name: ");
        String filename = reader.nextLine();
        reader.close();

        return filename;
    }
    
    
}
