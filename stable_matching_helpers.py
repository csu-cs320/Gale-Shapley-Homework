import itertools
import random


def inverse_dict(d):
    return {v: k for k,v in d.items()}

def with_reverse_lookup(d):
    d.update(inverse_dict(d))
    return d

def matching_from_lists(men, women):
    return with_reverse_lookup({m: w for m,w in zip(men, women)})

def all_matchings(men, women):
    return map(matching_from_lists,
               itertools.repeat(list(men)),
               itertools.permutations(women, len(women)))

def random_matching(men, women):
    return matching_from_lists(list(men), random.sample(list(women), len(women)))

def pref_list_to_dict(pref_list):
    return {item: rank for rank,item in enumerate(pref_list)}

def dict_to_pref_list(prefs):
    return [tup[1] for tup in sorted(inverse_dict(prefs).items())]

def random_pref(persons):
    return pref_list_to_dict(random.sample(list(persons), len(persons)))

def random_problem(men, women):
    return ({m: random_pref(women) for m in men},
            {w: random_pref(men) for w in women})

def map_values(f, d):
    return {k: f(v) for k,v in d.items()}
    
def compact_problem(prob):
    return (map_values(dict_to_pref_list, prob[0]),
            map_values(dict_to_pref_list, prob[1]))

def uncompact_problem(prob):
    return (map_values(pref_list_to_dict, prob[0]),
            map_values(pref_list_to_dict, prob[1]))

def is_instability(matching, man, mprefs, woman, wprefs):
    return (mprefs[woman] < mprefs[matching[man]] and
            wprefs[man] < wprefs[matching[woman]])

def instabilities(matching, men_prefs, women_prefs):
    def helper(m_w):
        m,w = m_w
        return is_instability(matching, m, men_prefs[m],
                             w, women_prefs[w])
    return filter(helper, itertools.product(men_prefs, women_prefs))

def is_stable(matching, men_prefs, women_prefs):
    return not any(instabilities(matching, men_prefs, women_prefs))

def all_stable_matchings(men_prefs, women_prefs):
    return filter(lambda matching: is_stable(matching, men_prefs, women_prefs),
                  all_matchings(men_prefs, women_prefs))
