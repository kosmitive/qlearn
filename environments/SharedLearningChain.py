import numpy as np

from environments.DeterministicMDP import DeterministicMDP
from spaces.DiscreteSpace import DiscreteSpace


class SharedLearningChain(DeterministicMDP):

    def __init__(self, name, num_states, N):

        # create the state and action space
        self.inner_size = N
        state_space = DiscreteSpace(N)
        action_space = DiscreteSpace(3)

        # one maps to 2
        starting_state = 1

        # specify the transition function
        transition_func = np.zeros((N, 3), dtype=np.int32)

        # iterate over and fill with the transitions
        for i in range(N):
            transition_func[i, 0] = i - 1
            transition_func[i, 1] = i + 1
            transition_func[i, 2] = 0

        transition_func[0, 0] = 0

        transition_func[N - 1, 1] = N - 1
        transition_func[N - 1, 2] = N - 1

        # now we define the reward function
        reward_function = np.zeros((N, 3), dtype=np.float64)
        for i in range(N - 1):
            reward_function[i, 2] = -0.1

        reward_function[0, 0] = -0.1
        reward_function[0, 2] = -0.1
        reward_function[1, 0] = -0.1
        reward_function[N-2, 1] = 1

        super().__init__(name, num_states, action_space, state_space, transition_func, reward_function, starting_state)

    def get_name(self):
        return "shared_chain"
