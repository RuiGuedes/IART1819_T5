import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Level {

    /**
     * Bi-dimensional representation of map
     */
    private char[][] matrix = new char[18][18];

    /**
     * Data structure containing agents information
     */
    private Map<Character, Data> agents = new HashMap<>();

    /**
     * Initializes level class
     */
    Level() {
        try {
            read_file("maps/level.txt");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    /**
     * Initializes level class
     * @param filename Directory of the map to be read
     */
    public Level(String filename) {
        try {
            read_file(filename);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    /**
     * Read filename
     * @return Name of the file to be read
     */
    private String read_input() {
        Scanner reader = new Scanner(System.in);
        System.out.print("Enter level file name: ");
        String filename = reader.nextLine();
        reader.close();

        return filename;
    }


    /**
     * Reads map from a file and initializes matrix
     * @param filename Name of the file to be read
     * @throws FileNotFoundException
     */
    private void read_file(String filename) throws FileNotFoundException {

        File fileLevel = new File(filename);
        Scanner sc =  new Scanner(fileLevel);
        int index = 0;

        while (sc.hasNextLine()) {
            String line = sc.nextLine();
            char[] lineArray = line.toCharArray();

            for (int i=0; i< lineArray.length;i++)
                matrix[index][i] = lineArray[i];

            if(line.matches(".*[rgbyRGBY].*"))
                check_robot(line, index);

            index++;
        }
    }

    private void check_robot(String line, int index) {
        int pos;

        if((pos = line.indexOf('r')) != -1) {
            save_target('r', pos, index);
        }
        if((pos = line.indexOf('g')) != -1) {
            save_target('g',pos,index);
        }
        if((pos = line.indexOf('b')) != -1) {
            save_target('b',pos,index);
        }
        if((pos = line.indexOf('y')) != -1) {
            save_target('y',pos,index);
        }
        if((pos = line.indexOf('R')) != -1) {
            save_robot('r', pos, index);
        }
        if((pos = line.indexOf('G')) != -1) {
            save_robot('g',pos,index);
        }
        if((pos = line.indexOf('B')) != -1) {
            save_robot('b',pos,index);
        }
        if((pos = line.indexOf('Y')) != -1) {
            save_robot('y',pos,index);
        }
    }

    private void save_robot(char color, int x, int y) {
        Data robot;
        matrix[y][x] = ' ';
        System.out.println(matrix[y][x]);

        if(agents.containsKey(color)) {
            robot = agents.get(color);
            robot.setCurrY(y);
            robot.setCurrX(x);
            agents.put(color,robot);
        } else {
            robot = new Data(x,y, -1, -1);
            agents.put(color,robot);
        }
    }

    private void save_target(char color, int x, int y) {
        Data robot;
        matrix[y][x] = ' ';

        if(agents.containsKey(color)) {
            robot = agents.get(color);
            robot.setTargetY(y);
            robot.setTargetX(x);
            agents.put(color,robot);
        } else {
            robot = new Data(-1,-1, x, y);
            agents.put(color,robot);
        }
    }

    /**
     * Get matrix
     * @return matrix
     */
    char[][] getMatrix() {
        return matrix;
    }

    /**
     * Get agent
     * @param r Agent identifier
     * @return Agent
     */
    Data getAgent(char r) {
        return agents.get(r);
    }

    /**
     * Get all agents
     * @return Data structure containing all agents
     */
    public Map<Character, Data> getAgents() {
        return agents;
    }

    /**
     * Display matrix in a friendly way
     */
    void display() {
        for (char[] row : matrix) {
            for (char cell : row) {
                System.out.print(cell + " ");
            }
            System.out.println();
        }
    }
}
