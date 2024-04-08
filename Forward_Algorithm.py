# From the Forward Algorithm we have discussed in the paper with the help of HMM and other libraries available in python.
# Now we are implementing the forward algorithm to find the probability of happening of observed sequence.
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 22:08:04 2024

@author: Srini
"""

import numpy as np

class HiddenMarkovModel:
    def __init__(self, states, observations, start_prob, transition_prob, emission_prob):
        self.states = states
        self.observations = observations
        self.start_prob = start_prob
        self.transition_prob = transition_prob
        self.emission_prob = emission_prob

    def forward_algorithm(self, observations):
        T = len(observations)
        N = len(self.states)

        # Initialize alpha
        alpha = np.zeros((T, N))
        for i, state in enumerate(self.states):
            alpha[0][i] = self.start_prob[i] * self.emission_prob[i][self.observations.index(observations[0])]

        # Induction
        for t in range(1, T):
            for j, state_to in enumerate(self.states):
                sum_over_alpha = sum(alpha[t - 1][i] * self.transition_prob[i][j] for i, state_from in enumerate(self.states))
                alpha[t][j] = sum_over_alpha * self.emission_prob[j][self.observations.index(observations[t])]

        # Termination
        prob_observation = sum(alpha[T - 1])
        return prob_observation

# Example usage
states = ['Cloudy','Sunny']
observations = ['Happy','Sad']
start_prob = [0.4, 0.6]
transition_prob = [
    [0.23, 0.77],
    [0.53, 0.46]
]
emission_prob = [
    [0.5, 0.5],
    [0.26, 0.74]
]

hmm = HiddenMarkovModel(states, observations, start_prob, transition_prob, emission_prob)
observation_sequence = ['Happy','Sad','Happy']
probability = hmm.forward_algorithm(observation_sequence)
print("Probability of observing sequence {} is {:.6f}".format(observation_sequence, probability))
