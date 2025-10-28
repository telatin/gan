#!/usr/bin/env python3
import itertools

# each term is a list of lists, as some terms can be declined in more
# than one way but still being the same (e.g ornis/ornithos)
pref = [
    ["pullus"],
    ["ornis", "ornithos"],
    ["avis"],
    ["kottos"],
    ["gallus", "gallu"],
    ["alektryon"],
    ["pteron"],
    ["gallina"],
]
mid = [
    ["stercus"],
    ["excrementum"],
    ["kopros"],
    ["faex", "faecis"],
    ["merda"],
    ["kakke"],
    ["enteron"],
    ["intestinum"],
    [""],
]
terms = [
    ["cola"],
    ["microbium"],
    ["monas"],
    ["spira"],
    ["bios"],
    ["bacterium"],
    ["plasma"],
    ["soma"],
    [""],
]


# the 'iterables' list contains the parts of the word to be generated in the order they should appear
iterables = [pref, mid, terms]

counter = 0

# itertools.product generates all the combinations of the lists in "iterables"
for t in itertools.product(*iterables):
    spellingVariants = []
    for subList in t:
        spellingVariants.append(subList)
    counter += 1
    print(counter, end="\t")
    for j in itertools.product(*spellingVariants):
        print("".join(j), end=", ")

    print("")
