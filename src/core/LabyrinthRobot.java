package core;

import agent.Action;
import search.agent.SearchAgent;
import search.framework.Node;
import search.framework.SearchForActions;
import search.framework.problem.GeneralProblem;
import search.framework.problem.Problem;
import search.framework.qsearch.GraphSearch;
import search.framework.qsearch.TreeSearch;
import search.informed.AStarSearch;
import search.informed.GreedyBestFirstSearch;
import search.uninformed.BreadthFirstSearch;
import search.uninformed.DepthFirstSearch;
import search.uninformed.DepthLimitedSearch;

import java.io.File;
import java.util.*;
import java.util.function.ToDoubleFunction;

public class LabyrinthRobot {

    private static Level map;

    private static int MIN_DEPTH = 10;
    private static int MAX_DEPTH = 1000;

    public static void main(String[] args) throws Exception {

        // Read filename and initialize map
        read_file_name();

        // Display interface
        mainMenu();
    }

    private static void clearScreen(int limit) {
        for(int i = 0; i < limit; i++)
            System.out.println();
    }

    private static void displayTitle() {
        System.out.println("######################");
        System.out.println("## Labyrinth Robots ##");
        System.out.println("######################\n");
    }

    private static void mainMenu() throws Exception {

        ArrayList<String> displayOptions = new ArrayList<>() {
            {
                add("1 - Depth-First Search");
                add("2 - Breadth-First Search");
                add("3 - Depth-Limited Search");
                add("4 - Greedy-Best-First Search");
                add("5 - A-StarSearch");
                add("6 - Exit\n");
            }
        };

        while(true) {
            displayTitle();
            String option = read_input(displayOptions, "Select an algorithm: ", "Invalid option. Try again !", 1, displayOptions.size());

            switch (option) {
                case "1":
                    uninformedSearch("Depth-First Search", 0);
                    break;
                case "2":
                    uninformedSearch("Breadth-First Search", 0);
                    break;
                case "3":
                    String limit = read_input(null, "Select the limit depth [" + MIN_DEPTH + " , " + MAX_DEPTH + "]: ", "Invalid limit. Try again !", MIN_DEPTH, MAX_DEPTH);
                    uninformedSearch("Depth-First Search", Integer.parseInt(limit));
                    break;
                case "4":
                    informedSearch("Greedy-Best-First Search");
                    break;
                case "5":
                    informedSearch("A-StarSearch");
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
        Scanner reader = new Scanner(System.in);

        while (true) {
            for(String displayOption : displayOptions) System.out.println(displayOption);

            System.out.print(displayQuestion);
            option = reader.nextLine();

            try {
                if(Integer.parseInt(option) >= lowerLimit && Integer.parseInt(option) <= upperLimit)
                    break;
                else
                    throw new Exception();
            }
            catch (Exception e) {
                System.out.println(displayInvalid);
                clearScreen(1);
            }
        }

        return option;
    }

    /**
     * Read filename
     */
    private static void read_file_name() {
        String filename;
        Scanner reader = new Scanner(System.in);

        while (true) {
            System.out.print("Enter filename: ");
            filename = reader.nextLine();

            File f = new File("maps/" + filename + ".txt");
            if(f.exists() && !f.isDirectory())
                break;
            else
                System.out.println("Invalid file. Try again !");
        }

        map = new Level("maps/" + filename + ".txt");
    }

    private static void uninformedSearch(String algorithm, int limit) {
        Problem<State, Action> problem = new GeneralProblem<>(map.getCurrState(), Level::get_actions, Level::get_result,  Level::test_goal);
        SearchForActions<State, Action> search = null;

        switch (algorithm) {
            case "Depth-First Search":
                search = new DepthFirstSearch<>(new GraphSearch<>());
                break;
            case "Breadth-First Search":
                search = new BreadthFirstSearch<>(new TreeSearch<>());
                break;
            case "Depth-Limited Search":
                search = new DepthLimitedSearch<>(limit);
                break;
        }

        Optional<List<Action>> actions = search.findActions(problem);

        System.out.println(actions.get());
        System.out.println(search.getMetrics());
    }

    private static void informedSearch(String algorithm) throws Exception {
        Problem<State, Action> problem = new GeneralProblem<>(map.getCurrState(), Level::get_actions, Level::get_result,  Level::test_goal);
        SearchForActions<State, Action> search = null;

        switch (algorithm) {
            case "Greedy-Best-First Search":
                search = new GreedyBestFirstSearch<>(new GraphSearch<>(), Level.createHeuristicFunction());
                break;
            case "A-StarSearch":
                search = new AStarSearch<>(new GraphSearch<>(), Level.createHeuristicFunction());
                break;
        }

        SearchAgent<State, Action> agent = new SearchAgent<>(problem, search);

        System.out.println(agent.getActions().size());
        System.out.println(agent.getActions());
    }

}
