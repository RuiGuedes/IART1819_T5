package core;

import search.framework.SearchForActions;
import search.framework.problem.GeneralProblem;
import search.framework.problem.Problem;
import search.framework.qsearch.GraphSearch;
import search.framework.qsearch.TreeSearch;
import search.uninformed.BreadthFirstSearch;
import search.uninformed.DepthFirstSearch;
import search.uninformed.DepthLimitedSearch;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Optional;

public class LabyrinthRobot {

    private static Level map;

    public static void main(String[] args) {
        map = new Level("maps/level.txt");

        Problem<Map<Character, Data>, ArrayList<String>> problem = new GeneralProblem<>(map.getAgents(), Level::get_actions, Level::get_result, Level::test_goal);
        SearchForActions<Map<Character, Data>, ArrayList<String>> search = new DepthFirstSearch<>(new GraphSearch<>());
        //SearchForActions<Map<Character, Data>, ArrayList<String>> search = new DepthLimitedSearch<>(8);
        //SearchForActions<Map<Character, Data>, ArrayList<String>> search = new BreadthFirstSearch<>(new TreeSearch<>());
        Optional<List<ArrayList<String>>> actions = search.findActions(problem);

        System.out.println(actions.get());

        /*System.out.println(problem.getInitialState());
        System.out.println(problem.getActions(problem.getInitialState()));
        System.out.println(problem.getResult(problem.getInitialState(), problem.getActions(problem.getInitialState()).get(0)));
        System.out.println(problem.testGoal(problem.getResult(problem.getInitialState(), problem.getActions(problem.getInitialState()).get(0))));*/


    }
}
