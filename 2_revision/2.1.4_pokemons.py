import sys

pokemons = [i.rstrip() for i in sys.stdin]
print(len(pokemons) - len(set(pokemons)))

# Sample Input 1:
#
# Pichu
# Pichu
# Tyrogue
# Pichu
# Combee
# Marill
# Tyrogue
# Sample Output 1:
#
# 3
