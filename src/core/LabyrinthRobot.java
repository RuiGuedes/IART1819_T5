package core;



public class LabyrinthRobot {

    private static Level map;

    public static void main(String[] args) {
        map = new Level("maps/level.txt");

        boolean var = map.complete();


    }
}
