package core;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Level {

    /**
     * Bi-dimensional representation of map
     */
    private char[][] matrix = new char[18][18];

    /**
     * core.Data structure containing agents information
     */
    private Map<Character, Data> agents = new HashMap<>();

    /**
     * Initializes level class
     */
    Level() {
        try {
            read_file(read_input());
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    /**
     * Initializes level class
     * @param filename Directory of the map to be read
     */
    Level(String filename) {
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
     * @throws FileNotFoundException Possible exception
     */
    private void read_file(String filename) throws FileNotFoundException {

        int index = 0;
        File fileLevel = new File(filename);
        Scanner sc =  new Scanner(fileLevel);
        Pattern pattern = Pattern.compile("[^X\\s]");

        while (sc.hasNextLine()) {
            String line = sc.nextLine();
            System.arraycopy(line.toCharArray(), 0, matrix[index], 0, line.toCharArray().length);

            Matcher matcher = pattern.matcher(line);

            if(matcher.find()) {
                parse_row(line, index);
            }

            index++;
        }
    }

    /**
     * Checks possible target or agents presents in line
     * @param line Matrix row
     * @param index Index of the row
     */
    private void parse_row(String line, int index) {
        for(int i = 65; i < 123; i++) {
            if(!((i > 90 && i < 97) || (i == 88) || (i == 120))) {
                if(line.indexOf((char)i) != -1) {
                    store_data((char)i, line.indexOf((char)i), index);
                }
            }
        }
    }

    /**
     * Stores agent data
     * @param color Identifier of agent or its target
     * @param x Row
     * @param y Column
     */
    private void store_data(char color, int x, int y) {
        matrix[y][x] = ' ';
        char key = (int)color < 96 ? color : (char)(color - 32);

        if(agents.containsKey(key)) {
            Data agent = agents.get(key);
            if((int)color > 96) {
                agent.setTargetY(y); agent.setTargetX(x);
            }
            else {
                agent.setCurrY(y); agent.setCurrX(x);
            }
            agents.put(key, agent);
        } else {
            Data agent = (int)color > 96 ?  new Data(-1,-1, x, y) : new Data(x, y, -1, -1);
            agents.put(key, agent);
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
     * @return core.Data structure containing all agents
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

    /**
     * Checks whether level is completed or not
     * @return True if level is complete. False otherwise
     */
    boolean complete() {
        for (Map.Entry<Character, Data> agent : agents.entrySet()) {
            if(!agent.getValue().cmp())
                return false;
        }
        return true;
    }

    void possible_moves() {

        for (Map.Entry<Character, Data> agent : agents.entrySet()) {

        }
    }
}
