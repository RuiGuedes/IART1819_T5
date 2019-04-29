package core;

import java.util.HashMap;
import java.util.Map;

public class State {

    /**
     * Data structure containing all agents information
     */
    private Map<Character, Data> agents = new HashMap<>();

    /**
     * Path cost so far
     */
    private int pathCost = 0;

    /**
     * Default constructor
     */
    State() {}

    /**
     * Creates a new state by copying a state. Increments path cost since the new state is a new node
     * @param state State to be copied
     */
    State(State state) {
        for (Map.Entry<Character, Data> agent : state.getAgents().entrySet()) {
            agents.put(agent.getKey(), new Data(agent.getValue()));
        }
        this.pathCost = state.getPathCost() + 1;
    }

    /**
     * Get path cost so far
     * @return Path cost
     */
    int getPathCost() {
        return pathCost;
    }

    /**
     * Get data structure containing all agents
     * @return Agents data structure
     */
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
