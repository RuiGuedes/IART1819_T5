package core;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class Data {
    private int currX;
    private int currY;
    private int targetX;
    private int targetY;

    Data(int currX, int currY, int targetX, int targetY) {
        this.currX = currX; this.currY = currY;
        this.targetX = targetX; this.targetY = targetY;
    }

    public int getCurrX() {
        return currX;
    }

    public void setCurrX(int currX) {
        this.currX = currX;
    }

    public int getCurrY() {
        return currY;
    }

    public void setCurrY(int currY) {
        this.currY = currY;
    }

    public int getTargetX() {
        return targetX;
    }

    public void setTargetX(int targetX) {
        this.targetX = targetX;
    }

    public int getTargetY() {
        return targetY;
    }

    public void setTargetY(int targetY) {
        this.targetY = targetY;
    }

    public ArrayList<String> get_actions(Character key, char[][] matrix, Map<Character, Data> curr_agents) {
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

    private boolean agent_at(int x, int y, Map<Character, Data> curr_agents) {
        for(Map.Entry<Character, Data> agent : curr_agents.entrySet()) {
            if(agent.getValue().getCurrX() == x && agent.getValue().getCurrY() == y)
                return true;
        }
        return false;
    }

    boolean cmp() {
        return ((this.targetX == -1) || ((this.currX == this.targetX) && (this.currY == this.targetY)));
    }

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

    private void move_agent(int inc_x, int inc_y, char[][] matrix, Map<Character, Data> curr_agents) {
        while(true) {
            if(matrix[this.currY + inc_y][this.currX + inc_x] == ' ' && !agent_at(this.currX + inc_x, this.currY + inc_y, curr_agents)) {
                this.currX += inc_x;
                this.currY += inc_y;
            }
            else
                return;
        }
    }


    @Override
    public String toString() {
        return "X: " + this.currX + " Y: " + this.currY + "\nTx: " + this.targetX + " Ty: " + this.targetY;
    }
}
