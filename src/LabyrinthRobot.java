public class LabyrinthRobot {

    private static Level map;

    public static void main(String[] args) {
        map = new Level();
        char[][] matrix = map.getMatrix();

        System.out.println(map.getRobots('r'));

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}
