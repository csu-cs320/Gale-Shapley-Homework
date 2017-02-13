import itertools
import random

# In this file, a matching looks like {'a': 'c', 'b': 'd', 'c': 'a', 'd': 'b'} for example.
# And a stable matching problem looks like:
# ({'a': {'c': 0, 'd': 1}, 'b': {'c': 0, 'd': 1}},
#  {'c': {'a': 0, 'b': 1}, 'd': {'a': 0, 'b': 1}})
# for example. 

def inverse_dict(d):
    '''Invert the mappings (k,v) => (v,k) of argument d, returning the new dict'''
    return {v: k for k,v in d.items()}

def with_reverse_lookup(d):
    '''Add inverted mappings for each existing mapping, returning the argument d'''
    d.update(inverse_dict(d))
    return d

def matching_from_lists(men, women):
    '''Create a matching, with bidirectional lookup, pairing man[0] with women[0], etc'''
    return with_reverse_lookup({m: w for m,w in zip(men, women)})

def all_matchings(men, women):
    '''Make a sequence of all possible perfect matchings between members of the two groups.
    Assumes len(men) == len(women)'''
    return map(matching_from_lists,
               itertools.repeat(list(men)),
               itertools.permutations(women, len(women)))

def random_matching(men, women):
    '''Generate a perfect matching randomly.
    Assumes len(men) = len(women)'''
    return matching_from_lists(list(men), random.sample(list(women), len(women)))

def pref_list_to_dict(pref_list):
    '''Takes a list like ['a', 'b', 'c'] and returns a dict like {'a': 0, 'b': 1, 'c': 2}'''
    return {item: rank for rank,item in enumerate(pref_list)}

def dict_to_pref_list(prefs):
    '''Takes a dict like {'a': 0, 'b': 1, 'c': 2} and returns a list like ['a', 'b', 'c']'''
    return [tup[1] for tup in sorted(inverse_dict(prefs).items())]

def random_pref(persons):
    '''Generates a random preference among the persons, returning the preference dict'''
    return pref_list_to_dict(random.sample(list(persons), len(persons)))

def random_problem(men, women):
    '''Generates a stable matching problem with random preferences for each person'''
    return ({m: random_pref(women) for m in men},
            {w: random_pref(men) for w in women})

def map_values(f, d):
    '''Produces a new dict from argument d, transforming all values with function f'''
    return {k: f(v) for k,v in d.items()}
    
def compact_problem(prob):
    '''Compact preferences from dicts to lists (to prepare for writing to a file)'''
    return (map_values(dict_to_pref_list, prob[0]),
            map_values(dict_to_pref_list, prob[1]))

def uncompact_problem(prob):
    '''Expand preferences from lists to dicts (for ease of lookups when solving)'''
    return (map_values(pref_list_to_dict, prob[0]),
            map_values(pref_list_to_dict, prob[1]))

def is_instability(matching, man, mprefs, woman, wprefs):
    '''Checks whether the pair (man, woman) are an instability in the matching, given their preferences in dict form'''
    return (mprefs[woman] < mprefs[matching[man]] and
            wprefs[man] < wprefs[matching[woman]])

def instabilities(matching, men_prefs, women_prefs):
    '''Generate a sequence of all instabilities in matching, given the preferences in dict form'''
    def helper(m_w):
        m,w = m_w
        return is_instability(matching, m, men_prefs[m],
                             w, women_prefs[w])
    return filter(helper, itertools.product(men_prefs, women_prefs))

def is_stable(matching, men_prefs, women_prefs):
    '''Determine whether the matching is stable'''
    return not any(instabilities(matching, men_prefs, women_prefs))

def all_stable_matchings(men_prefs, women_prefs):
    '''Generate a sequence of all stable matchings, given the preferences in dict form'''
    return filter(lambda matching: is_stable(matching, men_prefs, women_prefs),
                  all_matchings(men_prefs, women_prefs))
