# -*- coding: utf-8 -*-
"""
@author: Gayam Srinivasa Reddy
"""

states = ('cloudy', 'sunny')
 
observations = ('happy', 'sad', 'happy')
 
start_probability = {'cloudy': 0.4, 'sunny': 0.6}
 
transition_probability = {
   'cloudy' : {'cloudy': 0.23, 'sunny': 0.77},
   'sunny' : {'cloudy': 0.54, 'sunny': 0.46}
   }
 
emission_probability = {
   'cloudy' : {'happy': 0.5, 'sad': 0.5},
   'sunny' : {'happy': 0.26, 'sad': 0.74}
   }

def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}
    for y in states:
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]

    for t in range(1, len(obs)):
        V.append({})
        newpath = {}
 
        for y in states:
            (prob, state) = max((V[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states)
            V[t][y] = prob
            newpath[y] = path[state] + [y]
        path = newpath
    n = 0          
    if len(obs) != 1:
        n = t
    (prob, state) = max((V[n][y], y) for y in states)
    return (prob, path[state])

def print_dptable(V):
    s = "    " + " ".join(("%7d" % i) for i in range(len(V))) + "\n"
    for y in V[0]:
        s += "%.5s: " % y
        s += " ".join("%.7s" % ("%f" % v[y]) for v in V)
        s += "\n"
    print(s)
print(viterbi(observations, states, start_probability, transition_probability, emission_probability))
