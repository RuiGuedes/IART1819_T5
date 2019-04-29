package core;

import java.util.*;

public class Data {

    /**
     * Current X position
     */
    private int currX;

    /**
     * Current Y position
     */
    private int currY;

    /**
     * Target X position
     */
    private int targetX;

    /**
     * Target Y position
     */
    private int targetY;

    /**
     * Default constructor
     * @param currX Current X position
     * @param currY Current Y position
     * @param targetX Target X position
     * @param targetY Target Y position
     */
    Data(int currX, int currY, int targetX, int targetY) {
        this.currX = currX; this.currY = currY;
        this.targetX = targetX; this.targetY = targetY;
    }

    /**
     * Constructor used to allow the creation of copy of object
     * @param object Object to be copied
     */
    Data(Data object) {
        this.currX = object.currX; this.currY = object.currY;
        this.targetX = object.targetX; this.targetY = object.targetY;
    }

    /**
     * Get current X position
     * @return Current X position
     */
    int getCurrX() {
        return currX;
    }

    /**
     * Get current Y position
     * @return Current Y position
     */
    int getCurrY() {
        return currY;
    }

    /**
     * Get target X position
     * @return Target X position
     */
    int getTargetX() {
        return targetX;
    }

    /**
     * Get target Y position
     * @return Target Y position
     */
    int getTargetY() {
        return targetY;
    }

    /**
     * Set current X position
     * @param currX New current X position
     */
    void setCurrX(int currX) {
        this.currX = currX;
    }

    /**
     * Set current Y position
     * @param currY New current Y position
     */
    void setCurrY(int currY) {
        this.currY = currY;
    }

    /**
     * Set target X position
     * @param targetX New target X position
     */
    void setTargetX(int targetX) {
        this.targetX = targetX;
    }

    /**
     * Set target X position
     * @param targetY New target Y position
     */
    void setTargetY(int targetY) {
        this.targetY = targetY;
    }

    /**
     * Get agent pre-processed matrix
     * @param matrix Matrix without any agent
     */
    char[][] getPreProcessedMatrix(char[][] matrix) {
        char[][] newMatrix = deepCopy(matrix);

        if(targetX != -1 && targetY != -1)
            preProcessMatrix(newMatrix);

        return newMatrix;
    }

    /**
     * Deep copy a bi-dimensional array
     * @param original Original array
     * @return Return the original array copy
     */
    private static char[][] deepCopy(char[][] original) {
        if (original == null) {
            return null;
        }

        final char[][] result = new char[original.length][];
        for (int i = 0; i < original.length; i++) {
            result[i] = Arrays.copyOf(original[i], original[i].length);
        }
        return result;
    }

    /**
     * Pre-process agent matrix so that it can be used by the heuristic function
     * @param matrix Matrix to process
     */
    private void preProcessMatrix(char[][] matrix) {
        char distance = '1';

        for(ArrayList<Integer> array : getDirections(matrix, targetX, targetY)) {
            fillDirection(matrix, targetX, targetY, array.get(0), array.get(1), '1');
        }

        while(isEmpty(matrix)) {
            for(ArrayList<Integer> cells : getCells(matrix, distance++)) {
                for(ArrayList<Integer> directions : getDirections(matrix, cells.get(1), cells.get(0))) {
                    fillDirection(matrix, cells.get(1), cells.get(0), directions.get(0), directions.get(1), distance);
                }
            }
        }
    }

    /**
     * Get cells that have a certain content
     * @param matrix Matrix to process
     * @param number Content on cells
     * @return List of cells where content is verified
     */
    private List<ArrayList<Integer>> getCells(char[][] matrix, char number) {
        List<ArrayList<Integer>> cells = new ArrayList<>();

        for (int row = 0; row < matrix.length; row++) {
            for (int column = 0; column < matrix[row].length; column++) {
                if(matrix[row][column] == number) {
                    ArrayList<Integer> tmpList = new ArrayList<>();
                    tmpList.add(row); tmpList.add(column);
                    cells.add(tmpList);
                }
            }
        }

        return cells;
    }

    /**
     * Get possible expansion directions
     * @param matrix Matrix to process
     * @param x X position to begin the expansion
     * @param y Y position to begin the expansion
     * @return List of directions where expansion can be made
     */
    private List<ArrayList<Integer>> getDirections(char[][] matrix, int x, int y) {
        List<ArrayList<Integer>> directions = new ArrayList<>();

        if((y < 17) && matrix[y + 1][x] == ' ' && !reservedPosition(x, y + 1)) {
            directions.add(new ArrayList<>() {{
                add(0);
                add(1);
            }});
        }

        if((y > 0) && matrix[y - 1][x] == ' ' && !reservedPosition(x, y - 1)) {
            directions.add(new ArrayList<>() {{
                add(0);
                add(-1);
            }});
        }

        if((x < 17) && matrix[y][x + 1] == ' ' && !reservedPosition(x + 1, y)) {
            directions.add(new ArrayList<>() {{
                add(1);
                add(0);
            }});
        }

        if((x > 0) && matrix[y][x - 1] == ' ' && !reservedPosition(x- 1, y)) {
            directions.add(new ArrayList<>() {{
                add(-1);
                add(0);
            }});
        }

        return directions;
    }

    /**
     * Fills a certain direction with a certain content
     * @param matrix Matrix to process
     * @param x X position of start position
     * @param y Y position of start position
     * @param incX Increment on X
     * @param incY Increment on Y
     * @param number Content to fill cells
     */
    private void fillDirection(char[][] matrix, int x, int y, int incX, int incY, char number) {
        while(matrix[y + incY][x + incX] == ' ' && !reservedPosition(x + incX, y + incY)) {
            matrix[y + incY][x + incX] = number;
            y += incY;
            x += incX;
        }
    }

    /**
     * Checks if there are still missing cells to be filled
     * @param matrix Matrix to process
     * @return True if there are, false otherwise
     */
    private boolean isEmpty(char[][] matrix) {
        for(int row = 0; row < matrix.length; row++) {
            for(int column = 0; column < matrix[row].length; column++) {
                if(!reservedPosition(column, row) && matrix[row][column] == ' ')
                    return true;
            }
        }
        return  false;
    }

    /**
     * Verifies if a certain position is reserved or not
     * @param x X position
     * @param y Y position
     * @return True if it is, false otherwise
     */
    private boolean reservedPosition(int x, int y) {
        return (targetX == x && targetY == y);
    }

    /**
     * Get alignment value according to robot position
     * @return Alignment value
     */
    double getAlignmentValue() {
        if(currX == targetX && currY == targetY)
            return 0;
        else if(currX == targetX || currY == targetY)
            return 1.0;
        else
            return 2.0;
    }

    /**
     * Retrieve possible actions for a certain agent
     * @param matrix Map external representation
     * @param curr_agents All agents in a certain map
     * @return List of possible moves
     */
    ArrayList<String> getActions(char[][] matrix, Map<Character, Data> curr_agents) {
        ArrayList<String> agent_actions = new ArrayList<>();

        // Up
        if((this.currY > 1) && (matrix[this.currY - 1][this.currX] == ' ') && !agentAt(this.currX, this.currY - 1, curr_agents))
            agent_actions.add("UP");

        // Right
        if((this.currX < 17) && (matrix[this.currY][this.currX + 1] == ' ') && !agentAt(this.currX + 1, this.currY, curr_agents))
            agent_actions.add("RIGHT");

        // Down
        if((this.currY < 17) && (matrix[this.currY + 1][this.currX] == ' ') && !agentAt(this.currX, this.currY + 1, curr_agents))
            agent_actions.add("DOWN");

        // Left
        if((this.currX > 1) && (matrix[this.currY][this.currX - 1] == ' ') && !agentAt(this.currX - 1, this.currY, curr_agents))
            agent_actions.add("LEFT");

        // Comment this line to ensure actions order for all algorithms is the same
        // Collections.shuffle(agent_actions);

        return agent_actions;
    }

    /**
     * Perform a certain action
     * @param action Action to be performed
     * @param matrix Map external representation
     * @param curr_agents All agents in a certain map
     */
    public void action(String action, char[][] matrix, Map<Character, Data> curr_agents) {
        switch (action) {
            case "UP":
                moveAgent(0, -1, matrix, curr_agents);
                break;
            case "RIGHT":
                moveAgent(1, 0, matrix, curr_agents);
                break;
            case "DOWN":
                moveAgent(0, 1, matrix, curr_agents);
                break;
            case "LEFT":
                moveAgent(-1, 0, matrix, curr_agents);
                break;
        }
    }

    /**
     * Moves an agent to a certain position
     * @param inc_x Increment on X
     * @param inc_y Increment on Y
     * @param matrix Map external representation
     * @param curr_agents All agents in a certain map
     */
    private void moveAgent(int inc_x, int inc_y, char[][] matrix, Map<Character, Data> curr_agents) {
        for(int i = 0; i < 16; i++) {
            if(matrix[this.currY + inc_y][this.currX + inc_x] == ' ' && !agentAt(this.currX + inc_x, this.currY + inc_y, curr_agents)) {
                this.currX += inc_x;
                this.currY += inc_y;
            }
            else
                break;
        }
    }

    /**
     * Checks if there is an agent at a certain position
     * @param x X position
     * @param y Y position
     * @param curr_agents All agents in a certain map
     * @return True if agent is present, false otherwise
     */
    private boolean agentAt(int x, int y, Map<Character, Data> curr_agents) {
        for(Map.Entry<Character, Data> agent : curr_agents.entrySet()) {
            if(agent.getValue().getCurrX() == x && agent.getValue().getCurrY() == y)
                return true;
        }
        return false;
    }

    /**
     * Checks if agent is at its target position
     * @return True if current and target position matches.
     */
    boolean cmp() {
        return ((this.targetX == -1) || ((this.currX == this.targetX) && (this.currY == this.targetY)));
    }

    @Override
    public String toString() {
        return "X: " + this.currX + " Y: " + this.currY + " -- Tx: " + this.targetX + " Ty: " + this.targetY;
    }
}
