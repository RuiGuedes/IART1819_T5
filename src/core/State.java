package core;

import java.util.HashMap;
import java.util.Map;

public class State {

    /**
     * Data structure containing agents information
     */
    private Map<Character, Data> agents = new HashMap<>();

    private int pathCost = 0;

    State() {

    }

    State(State state) {
        for (Map.Entry<Character, Data> agent : state.getAgents().entrySet()) {
            agents.put(agent.getKey(), new Data(agent.getValue()));
        }
        this.pathCost = state.getPathCost() + 1;
        System.out.println(state.getPathCost() + " --- " + pathCost);
    }

    int getPathCost() {
        return pathCost;
    }

    Map<Character, Data> getAgents() {
        return agents;
    }

    @Override
    public String toString() {
        StringBuilder info = new StringBuilder();

        for (Map.Entry<Character, Data> agent : agents.entrySet()) {
            info.append("|").append(agent.getValue().getCurrX()).append("-").append(agent.getValue().getCurrY());
        }

        return info + "|";
    }
}
