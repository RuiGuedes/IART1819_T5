package core;

import agent.Action;
import search.agent.SearchAgent;
import search.framework.Metrics;
import search.framework.SearchForActions;
import search.framework.problem.GeneralProblem;
import search.framework.problem.Problem;
import search.framework.qsearch.TreeSearch;
import search.informed.AStarSearch;
import search.informed.GreedyBestFirstSearch;
import search.uninformed.BreadthFirstSearch;
import search.uninformed.DepthFirstSearch;
import search.uninformed.IterativeDeepeningSearch;

import java.io.File;
import java.io.IOException;
import java.util.*;

public class LabyrinthRobot {

    /**
     * Scanner to read user input
     */
    private static final Scanner reader = new Scanner(System.in);

    /**
     * Min depth for Depth-Limited Search
     */
    private static int MIN_DEPTH = 1;

    /**
     * Max depth for Depth-Limited Search
     */
    private static int MAX_DEPTH = 1000;

    public static void main(String[] args) throws Exception {

        // Read filename and initialize map
        String filename = read_file_name();

        // Display interface
        mainMenu(filename);
    }

    /**
     * Read filename
     */
    private static String read_file_name() throws IOException, InterruptedException {
        String filename;

        displayTitle();
        System.out.println("#################");
        System.out.println("# Reading Level #");
        System.out.println("#################\n");

        while (true) {
            System.out.print("Enter level name: ");
            filename = reader.nextLine();

            File f = new File("maps/" + filename + ".txt");
            if(f.exists() && !f.isDirectory())
                break;
            else
                System.out.println("Invalid level name. Try again !\n");
        }

        new Level("maps/" + filename + ".txt").display();

        System.out.println("File has been read successfully.\n");
        blockUntil();

        return "maps/" + filename + ".txt";
    }

    /**
     * Displays main menu
     * @param filename Level filename
     */
    private static void mainMenu(String filename) throws Exception {

        ArrayList<String> displayOptions = new ArrayList<>() {
            {
                add("1 - Depth-First Search");
                add("2 - Breadth-First Search");
                add("3 - Iterative Deepening Search");
                add("4 - Greedy-Best-First Search");
                add("5 - A-StarSearch");
                add("6 - Exit\n");
            }
        };

        ArrayList<String> possibleHeuristics = new ArrayList<>() {
            {
                add("\nHeuristic Functions\n");
                add("1 - Agent Alignment Heuristic");
                add("2 - Free Movement Heuristic\n");
            }
        };

        while(true) {
            displayTitle();
            String option = read_input(displayOptions, "Select an algorithm: ", "Invalid option. Try again !", 1, displayOptions.size());

            switch (option) {
                case "1":
                    uninformedSearch(new Level(filename), "Depth-First Search");
                    break;
                case "2":
                    uninformedSearch(new Level(filename), "Breadth-First Search");
                    break;
                case "3":
                    uninformedSearch(new Level(filename), "Iterative Deepening Search");
                    break;
                case "4":
                    String greedyHeuristic = read_input(possibleHeuristics, "Select an heuristic: ", "Invalid option. Try again !", 1, possibleHeuristics.size() - 1);
                    informedSearch(new Level(filename), "Greedy-Best-First Search", Integer.parseInt(greedyHeuristic));
                    break;
                case "5":
                    String aStarHeuristic = read_input(possibleHeuristics, "Select an heuristic: ", "Invalid option. Try again !", 1, possibleHeuristics.size() - 1);
                    informedSearch(new Level(filename), "A-StarSearch", Integer.parseInt(aStarHeuristic));
                    break;
                case "6":
                    return;
            }
        }
    }

    /**
     * Read options
     * @return Selected option
     */
    private static String read_input(ArrayList<String> displayOptions, String displayQuestion, String displayInvalid, int lowerLimit, int upperLimit) {
        String option;

        for(String displayOption : displayOptions)
            System.out.println(displayOption);

        while (true) {
            System.out.print(displayQuestion);
            option = reader.nextLine();

            try {
                if(Integer.parseInt(option) >= lowerLimit && Integer.parseInt(option) <= upperLimit)
                    break;
                else
                    throw new Exception();
            }
            catch (Exception e) {
                System.out.println(displayInvalid + "\n");
            }
        }

        return option;
    }

    /**
     * Performs uninformed search
     * @param map Level chosen
     * @param algorithm Algorithm to be used
     */
    private static void uninformedSearch(Level map, String algorithm) throws IOException, InterruptedException {
        Problem<State, Action> problem = new GeneralProblem<>(map.getCurrState(), Level::getActions, Level::getResult,  Level::testGoal);
        SearchForActions<State, Action> search = null;

        switch (algorithm) {
            case "Depth-First Search":
                search = new DepthFirstSearch<>(new TreeSearch<>());
                break;
            case "Breadth-First Search":
                search = new BreadthFirstSearch<>(new TreeSearch<>());
                break;
            case "Iterative Deepening Search":
                search = new IterativeDeepeningSearch<>();
                break;
        }

        long memory = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();
        long start = System.currentTimeMillis();

        Optional<List<Action>> actions = search.findActions(problem);

        long elapsedTime = System.currentTimeMillis() - start;
        long memoryUsage = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();

        if(actions.isPresent())
            displayAlgorithmInformation(map, actions.get(), search.getMetrics(), null, elapsedTime, memoryUsage);
        else
            displayAlgorithmInformation(map, new ArrayList<>(), search.getMetrics(), null, elapsedTime, memoryUsage);
    }

    /**
     * Performs informed search
     * @param map Level chosen
     * @param algorithm Algorithm to be used
     */
    private static void informedSearch(Level map, String algorithm, int heuristic) throws Exception {
        Problem<State, Action> problem = new GeneralProblem<>(map.getCurrState(), Level::getActions, Level::getResult,  Level::testGoal);
        SearchForActions<State, Action> search = null;

        switch (algorithm) {
            case "Greedy-Best-First Search":
                search = new GreedyBestFirstSearch<>(new TreeSearch<>(), Level.createHeuristicFunction(heuristic));
                break;
            case "A-StarSearch":
                search = new AStarSearch<>(new TreeSearch<>(), Level.createHeuristicFunction(heuristic));
                break;
        }

        long memory = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();
        long start = System.currentTimeMillis();

        SearchAgent<State, Action> agent = new SearchAgent<>(problem, search);

        long elapsedTime = System.currentTimeMillis() - start;
        long memoryUsage = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();

        displayAlgorithmInformation(map, agent.getActions(), null, agent.getInstrumentation(), elapsedTime, memoryUsage);
    }

    /**
     * Clears screen
     */
    private static void clearScreen() throws IOException, InterruptedException {
        new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
    }

    /**
     * Displays game title
     */
    private static void displayTitle() throws IOException, InterruptedException {
        clearScreen();
        System.out.println("######################");
        System.out.println("## Labyrinth Robots ##");
        System.out.println("######################\n");
    }

    /**
     * Displays algorithm detailed information
     * @param actions Actions made
     * @param metrics Algorithm metrics
     * @param properties Algorithm metrics
     * @param elapsedTime Time elapsed
     */
    private static void displayAlgorithmInformation(Level map, List<Action> actions, Metrics metrics, Properties properties, long elapsedTime, long memoryUsage) throws IOException, InterruptedException {
        displayTitle();
        map.display();
        displaySolution(actions);
        displayStatistics(metrics, properties, elapsedTime, memoryUsage);
        blockUntil();
    }

    /**
     * Displays level solution
     * @param actions Actions made
     */
    private static void displaySolution(List<Action> actions) {
        System.out.println("##################");
        System.out.println("# Level solution #");
        System.out.println("##################\n");

        if(actions.isEmpty())
            System.out.println("No solution available to be displayed.");

        for(int i = 1; (i - 1) < actions.size(); i++) {
            System.out.println(i + " - " + actions.get(i - 1).toString());
        }
    }

    /**
     * Displays algorithm metrics
     * @param metrics Algorithm metrics
     * @param properties Algorithm metrics
     * @param elapsedTime Time elapsed
     */
    private static void displayStatistics(Metrics metrics, Properties properties, long elapsedTime, long memoryUsage) {

        ArrayList<String> stats = new ArrayList<>();
        ArrayList<String> info = new ArrayList<>() {
            {
                add("maxQueueSize");
                add("nodesExpanded");
                add("pathCost");
                add("queueSize");
            }
        };

        for (String name : info) {
            if (metrics != null)
                stats.add(metrics.get(name));
            else
                stats.add(properties.get(name).toString());
        }

        System.out.println("\n##############");
        System.out.println("# Statistics #");
        System.out.println("##############\n");
        System.out.println("Maximum Queue Size = " + stats.get(0));
        System.out.println("Nodes Expanded = " + stats.get(1));
        System.out.println("Path Cost = " + stats.get(2));
        System.out.println("Queue Size = " + stats.get(3));
        System.out.println("Time Spent = " + elapsedTime + " ms");
        System.out.println("Memory Usage = " + humanReadableByteCount(memoryUsage, true));
        System.out.println();
    }

    /**
     * Blocks until user press any key to continue
     */
    private static void blockUntil() {
        System.out.print("Press any key to continue ... ");
        while (true) {
            if(reader.hasNextLine()) {
                reader.nextLine();
                break;
            }

        }
    }

    /**
     * Displays memory usage in a friendly way.
     * @param bytes Amount of bytes
     * @param si Display mode
     * @return Bytes formatted
     * @author aioobe
     */
    private static String humanReadableByteCount(long bytes, boolean si) {
        int unit = si ? 1000 : 1024;
        if (bytes < unit) return bytes + " B";
        int exp = (int) (Math.log(bytes) / Math.log(unit));
        String pre = (si ? "kMGTPE" : "KMGTPE").charAt(exp-1) + (si ? "" : "i");
        return String.format("%.1f %sB", bytes / Math.pow(unit, exp), pre);
    }

}
