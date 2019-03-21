import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Level {
    
    private char[][] matrix = new char[18][18];
    private Map<Character, Data> robots = new HashMap<>();
    
    public Level() {
        //String filename = read_input();
        //System.out.println(filename);
        String filename = "maps/level.txt";

        try {
            read_file(filename);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }


    }

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

        if(robots.containsKey(color)) {
            robot = robots.get(color);
            robot.setCurrY(y);
            robot.setCurrX(x);
            robots.put(color,robot);
        } else {
            robot = new Data(x,y, -1, -1);
            robots.put(color,robot);
        }
    }

    private void save_target(char color, int x, int y) {
        Data robot;
        matrix[y][x] = ' ';

        if(robots.containsKey(color)) {
            robot = robots.get(color);
            robot.setTargetY(y);
            robot.setTargetX(x);
            robots.put(color,robot);
        } else {
            robot = new Data(-1,-1, x, y);
            robots.put(color,robot);
        }
    }

    private String read_input() {
        Scanner reader = new Scanner(System.in);
        System.out.print("Enter level file name: ");
        String filename = reader.nextLine();
        reader.close();

        return filename;
    }

    public char[][] getMatrix() {
        return matrix;
    }

    public Data getRobots(char r) {
        return robots.get(r);
    }
}
