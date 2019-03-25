package core;

import java.util.ArrayList;
import java.util.Map;

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
    private int getCurrX() {
        return currX;
    }

    /**
     * Get current Y position
     * @return Current Y position
     */
    private int getCurrY() {
        return currY;
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
     * Retrieve possible actions for a certain agent
     * @param matrix Map external representation
     * @param curr_agents All agents in a certain map
     * @return List of possible moves
     */
    ArrayList<String> get_actions(char[][] matrix, Map<Character, Data> curr_agents) {
        ArrayList<String> agent_actions = new ArrayList<>();

        // Up
        if((this.currY > 1) && (matrix[this.currY - 1][this.currX] == ' ') && !agent_at(this.currX, this.currY - 1, curr_agents))
            agent_actions.add("UP");

        // Right
        if((this.currX < 17) && (matrix[this.currY][this.currX + 1] == ' ') && !agent_at(this.currX + 1, this.currY, curr_agents))
            agent_actions.add("RIGHT");

        // Down
        if((this.currY < 17) && (matrix[this.currY + 1][this.currX] == ' ') && !agent_at(this.currX, this.currY + 1, curr_agents))
            agent_actions.add("DOWN");

        // Left
        if((this.currX > 1) && (matrix[this.currY][this.currX - 1] == ' ') && !agent_at(this.currX - 1, this.currY, curr_agents))
            agent_actions.add("LEFT");

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
                move_agent(0, -1, matrix, curr_agents);
                break;
            case "RIGHT":
                move_agent(1, 0, matrix, curr_agents);
                break;
            case "DOWN":
                move_agent(0, 1, matrix, curr_agents);
                break;
            case "LEFT":
                move_agent(-1, 0, matrix, curr_agents);
                break;
        }
    }

    /**
     *
     * @param inc_x Increment on X
     * @param inc_y Increment on Y
     * @param matrix Map external representation
     * @param curr_agents All agents in a certain map
     */
    private void move_agent(int inc_x, int inc_y, char[][] matrix, Map<Character, Data> curr_agents) {
        for(int i = 0; i < 16; i++) {
            if(matrix[this.currY + inc_y][this.currX + inc_x] == ' ' && !agent_at(this.currX + inc_x, this.currY + inc_y, curr_agents)) {
                this.currX += inc_x;
                this.currY += inc_y;
            }
            else
                break;
        }
    }

    /**
     *
     * @param x X position
     * @param y Y position
     * @param curr_agents All agents in a certain map
     * @return True if agent is present, false otherwise
     */
    private boolean agent_at(int x, int y, Map<Character, Data> curr_agents) {
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
