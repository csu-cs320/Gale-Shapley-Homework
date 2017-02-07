by_number_of_stable_matchings = [
    # by the GS proof there is no problem with 0 stable matchings
    None,
    # 1 stable matching
    ({'a': ['f', 'g', 'e', 'h'],
      'b': ['g', 'h', 'f', 'e'],
      'c': ['e', 'h', 'f', 'g'],
      'd': ['h', 'e', 'g', 'f']},
     {'e': ['c', 'a', 'd', 'b'],
      'f': ['a', 'c', 'd', 'b'],
      'h': ['b', 'c', 'a', 'd'],
      'g': ['b', 'd', 'a', 'c']}),
    # 2 stable matchings
    ({'a': ['h', 'f', 'g', 'e'],
      'b': ['f', 'e', 'h', 'g'],
      'c': ['e', 'f', 'g', 'h'],
      'd': ['h', 'e', 'f', 'g']},
     {'e': ['d', 'b', 'a', 'c'],
      'f': ['a', 'c', 'b', 'd'],
      'h': ['c', 'a', 'b', 'd'],
      'g': ['d', 'c', 'a', 'b']}),
    # 3 stable matchings
    ({'a': ['f', 'g', 'h', 'e'],
      'b': ['e', 'h', 'f', 'g'],
      'c': ['g', 'h', 'e', 'f'],
      'd': ['e', 'f', 'g', 'h']},
     {'e': ['a', 'c', 'd', 'b'],
      'f': ['c', 'b', 'd', 'a'],
      'h': ['d', 'a', 'b', 'c'],
      'g': ['d', 'c', 'b', 'a']}),
    # 4 stable matchings
    ({'a': ['g', 'f', 'h', 'e'],
      'b': ['e', 'h', 'f', 'g'],
      'c': ['g', 'h', 'f', 'e'],
      'd': ['h', 'g', 'f', 'e']},
     {'e': ['a', 'c', 'b', 'd'],
      'f': ['d', 'b', 'c', 'a'],
      'h': ['a', 'b', 'c', 'd'],
      'g': ['d', 'c', 'a', 'b']}),
    # 5 stable matchings
    ({'a': ['e', 'h', 'g', 'f'],
      'b': ['h', 'g', 'e', 'f'],
      'c': ['e', 'g', 'h', 'f'],
      'd': ['g', 'f', 'e', 'h']},
     {'e': ['b', 'a', 'd', 'c'],
      'f': ['c', 'a', 'd', 'b'],
      'h': ['d', 'c', 'b', 'a'],
      'g': ['a', 'b', 'c', 'd']}),
    # 6 stable matchings
    ({'a': ['f', 'e', 'h', 'g'],
      'b': ['h', 'g', 'e', 'f'],
      'c': ['e', 'g', 'h', 'f'],
      'd': ['g', 'e', 'f', 'h']},
     {'e': ['a', 'd', 'b', 'c'],
      'f': ['c', 'd', 'b', 'a'],
      'h': ['d', 'a', 'c', 'b'],
      'g': ['a', 'b', 'c', 'd']}),
    # 7 stable matchings
    ({'a': ['e', 'f', 'h', 'g'],
      'b': ['h', 'g', 'f', 'e'],
      'c': ['g', 'h', 'e', 'f'],
      'd': ['f', 'e', 'h', 'g']},
     {'e': ['b', 'd', 'a', 'c'],
      'f': ['c', 'a', 'd', 'b'],
      'h': ['a', 'c', 'd', 'b'],
      'g': ['d', 'b', 'a', 'c']}),
    # 8 stable matchings
    ({'a': ['h', 'g', 'e', 'f'],
      'b': ['g', 'h', 'f', 'e'],
      'c': ['f', 'h', 'g', 'e'],
      'd': ['e', 'g', 'h', 'f']},
     {'e': ['b', 'a', 'c', 'd'],
      'f': ['a', 'b', 'c', 'd'],
      'h': ['d', 'c', 'b', 'a'],
      'g': ['c', 'd', 'a', 'b']})]

# a problem with 3 stable matchings
({'a': ['f', 'g', 'h', 'e'],
  'b': ['e', 'h', 'f', 'g'],
  'c': ['g', 'h', 'e', 'f'],
  'd': ['e', 'f', 'g', 'h']},
 {'e': ['a', 'c', 'd', 'b'],
  'f': ['c', 'b', 'd', 'a'],
  'h': ['d', 'a', 'b', 'c'],
  'g': ['d', 'c', 'b', 'a']})

# the stable matchings
[
    # women get their best valid partner, men get their worst valid partner
    [('a', 'h'), ('b', 'f'), ('c', 'e'), ('d', 'g')],
    # two men and two women got their best (c, d) (h, f)
    # two men and two women got their worst (a, b) (g, e)
    [('a', 'h'), ('b', 'f'), ('c', 'g'), ('d', 'e')],
    # men get their best valid partner, women get their worst valid partner
    [('a', 'f'), ('b', 'h'), ('c', 'g'), ('d', 'e')]
]
