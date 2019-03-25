package core;

import agent.Action;
import search.agent.SearchAgent;
import search.framework.Node;
import search.framework.SearchForActions;
import search.framework.problem.GeneralProblem;
import search.framework.problem.Problem;
import search.framework.qsearch.GraphSearch;
import search.framework.qsearch.TreeSearch;
import search.informed.GreedyBestFirstSearch;
import search.uninformed.BreadthFirstSearch;
import search.uninformed.DepthFirstSearch;
import search.uninformed.DepthLimitedSearch;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.function.ToDoubleFunction;

public class LabyrinthRobot {

    private static Level map;

    public static void main(String[] args) {


        map = new Level("maps/level.txt");

        uninformed();
        //informed();
    }



    private static void informed() throws Exception {

        Problem<Map<Character, Data>, Action> problem = new GeneralProblem<>(map.getAgents(),
                Level::get_actions,
                Level::get_result,
                Level::test_goal);

        //SearchForActions<Map<Character, Data>, Action> search = new GreedyBestFirstSearch<Map<Character, Data>, Object>
          //      (new GraphSearch<>(), createManhattanHeuristicFunction());
       // SearchAgent<Map<Character, Data>, Action> agent = new SearchAgent<>(problem, search);

    }

    public static ToDoubleFunction<Node<Map<Character, Data>, ArrayList<String>>> createManhattanHeuristicFunction() {
        return null;
    }

    public static void uninformed() {
        Problem<Map<Character, Data>, Action> problem = new GeneralProblem<>(map.getAgents(),
                Level::get_actions,
                Level::get_result,
                Level::test_goal);
        //SearchForActions<Map<Character, Data>, ArrayList<String>> search = new DepthFirstSearch<>(new GraphSearch<>());
        SearchForActions<Map<Character, Data>, Action> search = new DepthLimitedSearch<>(10);
        //SearchForActions<Map<Character, Data>, Action> search = new BreadthFirstSearch<>(new TreeSearch<>());
        Optional<List<Action>> actions = search.findActions(problem);

        System.out.println(actions.get());
        System.out.println(search.getMetrics());
    }

}
