package core;

import agent.Action;
import agent.impl.DynamicAction;
import search.framework.Node;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.function.ToDoubleFunction;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Level {

    /**
     * Bi-dimensional representation of map
     */
    private static char[][] matrix = new char[18][18];

    /**
     * Current game state
     */
    private static State initialState;

    /**
     * Current game state
     */
    private static State currState;

    /**
     * Holds all information about the visited nodes at a certain moment
     */
    private static Map<String, Integer> searchInfo;

    /**
     * Agents pre-processed matrix
     */
    private static Map<Character, char[][]> preProcessedMatrix;

    /**
     * Initializes level class
     * @param filename Directory of the map to be read
     */
    Level(String filename) {
        try {
            // Reads file that contains the selected level
            readFile(filename);

            // Stores initial state
            storeInitialState();

            // Initializes agents pre-processing
            initPreProcess();

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    /**
     * Reads map from a file and initializes matrix
     * @param filename Name of the file to be read
     * @throws FileNotFoundException Possible exception
     */
    private void readFile(String filename) throws FileNotFoundException {

        int index = 0;
        currState = new State(); searchInfo = new HashMap<>();
        File fileLevel = new File(filename);
        Scanner sc =  new Scanner(fileLevel);
        Pattern pattern = Pattern.compile("[^X\\s]");

        while (sc.hasNextLine()) {
            String line = sc.nextLine();
            System.arraycopy(line.toCharArray(), 0, matrix[index], 0, line.toCharArray().length);

            Matcher matcher = pattern.matcher(line);

            if(matcher.find()) {
                parseRow(line, index);
            }

            index++;
        }
    }

    /**
     * Checks possible target or agents presents in line
     * @param line Matrix row
     * @param index Index of the row
     */
    private void parseRow(String line, int index) {
        for(int i = 65; i < 123; i++) {
            if(!((i > 90 && i < 97) || (i == 88) || (i == 120))) {
                if(line.indexOf((char)i) != -1) {
                    storeData((char)i, line.indexOf((char)i), index);
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
    private void storeData(char color, int x, int y) {
        matrix[y][x] = ' ';
        char key = (int)color < 96 ? color : (char)(color - 32);

        if(currState.getAgents().containsKey(key)) {
            Data agent = currState.getAgents().get(key);
            if((int)color > 96) {
                agent.setTargetY(y); agent.setTargetX(x);
            }
            else {
                agent.setCurrY(y); agent.setCurrX(x);
            }
            currState.getAgents().put(key, agent);
        } else {
            Data agent = (int)color > 96 ?  new Data(-1,-1, x, y) : new Data(x, y, -1, -1);
            currState.getAgents().put(key, agent);
        }
    }

    /**
     * For each agent pre-process its own matrix to be used by the heuristic function
     */
    private void initPreProcess() {
        preProcessedMatrix = new HashMap<>();

        for (Map.Entry<Character, Data> agent : currState.getAgents().entrySet()) {
            preProcessedMatrix.put(agent.getKey(), agent.getValue().getPreProcessedMatrix(matrix));
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
     * Return the game current state
     * @return Current state
     */
    State getCurrState() {
        return currState;
    }

    /**
     * Returns data structure that contains information about the search made
     * @return Search structure
     */
    public static Map<String, Integer> getSearchInfo() {
        return searchInfo;
    }

    /**
     * Stores initial state
     */
    private void storeInitialState() {
        initialState = new State(currState);
    }

    /**
     * Resets current state 
     */
    public static void reset() {
        currState = new State(initialState);
        searchInfo = new HashMap<>();
    }

    /**
     * Display matrix in a friendly way
     */
    void display() {
        System.out.println();
        for(int row = 0; row < matrix.length; row++) {
            for(int column = 0; column < matrix[row].length; column++) {
                if(matrix[row][column] == '0')
                    System.out.print("  ");
                else {
                    char agent = agentAt(column, row);
                    if (agent != ' ')
                        System.out.print(agent + " ");
                    else
                        System.out.print(matrix[row][column] + " ");
                }
            }
            System.out.println();
        }
        System.out.println();
        System.out.println("##########");
        System.out.println("# Legend #");
        System.out.println("##########");
        System.out.println("\nX -> Map Boundary");
        System.out.println("Uppercase -> Robot Position");
        System.out.println("Lowercase -> Target Position\n");
    }

    /**
     * Checks if there exists an agent at a certain position
     * @param x X position
     * @param y Y position
     * @return Cell identifier
     */
    private char agentAt(int x, int y) {
        for(Map.Entry<Character, Data> agent : initialState.getAgents().entrySet()) {
            if(agent.getValue().getCurrX() == x && agent.getValue().getCurrY() == y)
                return agent.getKey();
            else if(agent.getValue().getTargetX() == x && agent.getValue().getTargetY() == y) {
                return (char) (agent.getKey() + 32);
            }
        }
        return ' ';
    }

    /**
     * Get possible actions for a certain agent
     * @param currState All agents in a certain map
     * @return List of possible actions
     */
    static List<Action> getActions(State currState) {
        List<Action> actions = new ArrayList<>();

        for (Map.Entry<Character, Data> agent : currState.getAgents().entrySet()) {
            ArrayList<String> agent_actions = agent.getValue().getActions(matrix, currState.getAgents());

            for (String action : agent_actions) {
                String name = agent.getKey() + "-" + action;

                State nextState = getResult(currState, new DynamicAction(name));

                if(searchInfo.containsKey(nextState.toString())) {
                    if(searchInfo.get(nextState.toString()) > nextState.getPathCost()) {
                        searchInfo.put(nextState.toString(), nextState.getPathCost());
                        actions.add(new DynamicAction(name));
                    }
                }
                else {
                    searchInfo.put(nextState.toString(), nextState.getPathCost());
                    actions.add(new DynamicAction(name));
                }
            }
        }
        return actions;
    }

    /**
     * Get the result for a certain action
     * @param currState All agents in a certain map
     * @param action Action to be performed
     * @return The new state reached
     */
    static State getResult(State currState, Action action) {
        State nextState = new State(currState);
        //System.out.println("asdasdsdasdasd + " + currState);
        String[] action_info = ((DynamicAction) action).getName().split("-");
        nextState.getAgents().get(action_info[0].charAt(0)).action(action_info[1], matrix, currState.getAgents());

        return nextState;
    }

    /**
     * Checks whether level is completed or not
     * @return True if level is complete. False otherwise
     */
    static boolean testGoal(State currState) {
        for (Map.Entry<Character, Data> agent : currState.getAgents().entrySet()) {
            if(!agent.getValue().cmp())
                return false;
        }
        return true;
    }

    /**
     * Creates heuristic function
     * @return New heuristic function
     */
    static ToDoubleFunction<Node<State, Action>> createHeuristicFunction(int heuristicFunction) {
        if(heuristicFunction == 1)
            return new AgentAlignmentHeuristic();
        else
            return new FreeMovementHeuristic();
    }

    
    private static class FreeMovementHeuristic implements ToDoubleFunction<Node<State, Action>> {

        double getNeededMoves(char key, Data agent) {
            if(agent.getTargetX() != -1 && agent.getTargetY() != -1)
                return Character.digit(preProcessedMatrix.get(key)[agent.getCurrY()][agent.getCurrX()], 10);
            else
                return 0;
        }

        @Override
        public double applyAsDouble(Node<State, Action> node) {
            double result = 0;

            for (Map.Entry<Character, Data> agent : node.getState().getAgents().entrySet()) {
                result += getNeededMoves(agent.getKey(), agent.getValue());
            }

            return result;
        }
    }

    private static class AgentAlignmentHeuristic implements ToDoubleFunction<Node<State, Action>> {

        @Override
        public double applyAsDouble(Node<State, Action> node) {
            double result = 0;

            for (Map.Entry<Character, Data> agent : node.getState().getAgents().entrySet()) {
                result += agent.getValue().getAlignmentValue();
            }

            return result;
        }
    }

}
