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

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.function.ToDoubleFunction;

public class LabyrinthRobot {

    private static Level map;

    public static void main(String[] args) throws Exception {


        map = new Level("maps/level22.txt");

        //map.display();
        //map.getAgents().get('R').display();
        //uninformed();
        informed();
    }


    private static void informed() throws Exception {

        Problem<Map<Character, Data>, Action> problem = new GeneralProblem<>(map.getAgents(),
                Level::get_actions,
                Level::get_result,
                Level::test_goal);

        //SearchForActions<Map<Character, Data>, Action> search = new GreedyBestFirstSearch<>(new GraphSearch<>(), Level.createHeuristicFunction());
        SearchForActions<Map<Character, Data>, Action> search = new AStarSearch<>(new GraphSearch<>(), Level.createHeuristicFunction());
        SearchAgent<Map<Character, Data>, Action> agent = new SearchAgent<>(problem, search);

        System.out.println(agent.getActions().size());
        System.out.println(agent.getActions());

    }

    public static void uninformed() {
        Problem<Map<Character, Data>, Action> problem = new GeneralProblem<>(map.getAgents(),
                Level::get_actions,
                Level::get_result,
                Level::test_goal);
        //SearchForActions<Map<Character, Data>, ArrayList<String>> search = new DepthFirstSearch<>(new GraphSearch<>());
        SearchForActions<Map<Character, Data>, Action> search = new DepthLimitedSearch<>(60);
        //SearchForActions<Map<Character, Data>, Action> search = new BreadthFirstSearch<>(new TreeSearch<>());
        Optional<List<Action>> actions = search.findActions(problem);

        System.out.println(actions.get());
        System.out.println(search.getMetrics());
    }

}
