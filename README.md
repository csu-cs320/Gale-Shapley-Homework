# Gale-Shapley-Homework

You will turn in a tar file named Gale-Shapley-Homework.tar. It should untar to a folder called Gale-Shapley-Homework. In that folder, there should be a gale-shapley.py file.

We should be able to run your gale-shapley.py script with the name of a file containing input in the format shown in the tests. 
```bash
$ python3 gale-shapley.py some_problem_file.txt
```

Input file format:
```
abe: carol dee
bob: dee carol

carol: bob abe
dee: abe bob
```

Output file format:
```
abe dee
bob carol
```

It should output a file describing a matching produced by the Gale-Shapley algorithm in the format shown in the tests. This file should be named like the input file with "_solution" appended. That file should describe one of the possible matchings produced by GS. It doesn't matter which group you choose to be the proposers (we'll check both solutions), and it doesn't matter which way you specify the matching. We will read it in as a dictionary and calculate the reverse associations as well. So "a b" is one way to say "a is matched with b". And "b a" is another.

### Example

We should be able to do this:
```bash
$ ls Gale-*
Gale-Shapley-Homework.tar
$ tar xf Gale-Shapley-Homework.tar
$ cd Gale-Shapley-Homework/
$ ls gale*.py
gale-shapley.py
$ python3 gale-shapley.py path/to/some_problem_file.txt
$ ls path/to/some_problem_file*
path/to/some_problem_file.txt path/to/some_problem_file.txt_solution
```
