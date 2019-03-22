public class LabyrinthRobot {

    private static Level map;

    public static void main(String[] args) {
        map = new Level();
        char[][] matrix = map.getMatrix();

        System.out.println(map.getAgent('r'));

        map.display();
    }
}
