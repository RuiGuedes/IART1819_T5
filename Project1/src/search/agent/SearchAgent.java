package search.agent;

import java.util.*;

import agent.Action;
import agent.Percept;
import agent.impl.AbstractAgent;
import agent.impl.NoOpAction;
import search.framework.Metrics;
import search.framework.SearchForActions;
import search.framework.problem.Problem;

/**
 *
 * @param <S> The type used to represent states
 * @param <A> The type of the actions to be used to navigate through the state space
 *
 * @author Ravi Mohan
 * @author Ruediger Lunde
 */
public class SearchAgent<S, A extends Action> extends AbstractAgent {
	private List<Action> actionList;

	private Iterator<Action> actionIterator;

	private Metrics searchMetrics;

	public SearchAgent(Problem<S, A> p, SearchForActions<S, A> search) throws Exception {
		Optional<List<A>> actions = search.findActions(p);
		actionList = new ArrayList<>();
		if (actions.isPresent())
			actionList.addAll(actions.get());

		actionIterator = actionList.iterator();
		searchMetrics = search.getMetrics();
	}

	@Override
	public Action execute(Percept p) {
		if (actionIterator.hasNext())
			return actionIterator.next();
		return NoOpAction.NO_OP; // no success or at goal
	}

	public boolean isDone() {
		return !actionIterator.hasNext();
	}

	public List<Action> getActions() {
		return actionList;
	}

	public Properties getInstrumentation() {
		Properties result = new Properties();
		for (String key : searchMetrics.keySet()) {
			String value = searchMetrics.get(key);
			result.setProperty(key, value);
		}
		return result;
	}
}