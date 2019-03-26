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

class Level {

    /**
     * Bi-dimensional representation of map
     */
    private static char[][] matrix = new char[18][18];

    /**
     * Current game state
     */
    private State currState;

    /**
     * Holds all information about the visited nodes so far
     */
    private static Map<String, Integer> searchInfo = new HashMap<>();

    /**
     * Initializes level class
     */
    Level() {
        try {
            read_file(read_input());
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    /**
     * Initializes level class
     * @param filename Directory of the map to be read
     */
    Level(String filename) {
        try {
            read_file(filename);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    /**
     * Read filename
     * @return Name of the file to be read
     */
    private String read_input() {
        Scanner reader = new Scanner(System.in);
        System.out.print("Enter level file name: ");
        String filename = reader.nextLine();
        reader.close();

        return filename;
    }


    /**
     * Reads map from a file and initializes matrix
     * @param filename Name of the file to be read
     * @throws FileNotFoundException Possible exception
     */
    private void read_file(String filename) throws FileNotFoundException {

        int index = 0;
        this.currState = new State();
        File fileLevel = new File(filename);
        Scanner sc =  new Scanner(fileLevel);
        Pattern pattern = Pattern.compile("[^X\\s]");

        while (sc.hasNextLine()) {
            String line = sc.nextLine();
            System.arraycopy(line.toCharArray(), 0, matrix[index], 0, line.toCharArray().length);

            Matcher matcher = pattern.matcher(line);

            if(matcher.find()) {
                parse_row(line, index);
            }

            index++;
        }

        initPreProcess();
    }

    /**
     * Checks possible target or agents presents in line
     * @param line Matrix row
     * @param index Index of the row
     */
    private void parse_row(String line, int index) {
        for(int i = 65; i < 123; i++) {
            if(!((i > 90 && i < 97) || (i == 88) || (i == 120))) {
                if(line.indexOf((char)i) != -1) {
                    store_data((char)i, line.indexOf((char)i), index);
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
    private void store_data(char color, int x, int y) {
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
        for (Map.Entry<Character, Data> agent : currState.getAgents().entrySet()) {
            agent.getValue().setMatrix(matrix);
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
     * Display matrix in a friendly way
     */
    void display() {
        for (char[] row : matrix) {
            for (char cell : row) {
                System.out.print(cell + " ");
            }
            System.out.println();
        }
    }

    /**
     * Get possible actions for a certain agent
     * @param currState All agents in a certain map
     * @return List of possible actions
     */
    static List<Action> get_actions(State currState) {
        List<Action> actions = new ArrayList<>();

        for (Map.Entry<Character, Data> agent : currState.getAgents().entrySet()) {
            ArrayList<String> agent_actions = agent.getValue().get_actions(matrix, currState.getAgents());

            for (String action : agent_actions) {
                String name = agent.getKey() + "-" + action;

                State nextState = get_result(currState, new DynamicAction(name));

                if(searchInfo.containsKey(nextState.toString())) {
                    System.out.println(currState.getPathCost() + " ||| " + nextState.getPathCost());
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

    public static Map<String, Integer> getSearchInfo() {
        return searchInfo;
    }

    /**
     * Get the result for a certain action
     * @param currState All agents in a certain map
     * @param action Action to be performed
     * @return The new state reached
     */
    static State get_result(State currState, Action action) {
        State nextState = new State(currState);

        String[] action_info = ((DynamicAction) action).getName().split("-");
        nextState.getAgents().get(action_info[0].charAt(0)).action(action_info[1], matrix, currState.getAgents());

        return nextState;
    }

    /**
     * Checks whether level is completed or not
     * @return True if level is complete. False otherwise
     */
    static boolean test_goal(State currState) {
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
    static ToDoubleFunction<Node<State, Action>> createHeuristicFunction() {
        return new HeuristicFunction();
    }

    /**
     * @author Ravi Mohan
     * @author Ruediger Lunde
     *
     */
    private static class HeuristicFunction implements ToDoubleFunction<Node<State, Action>> {

        @Override
        public double applyAsDouble(Node<State, Action> node) {
            double result = 0;

            for (Map.Entry<Character, Data> agent : node.getState().getAgents().entrySet()) {
                result += agent.getValue().getNeededMoves();
            }

            return result;
        }
    }

}
