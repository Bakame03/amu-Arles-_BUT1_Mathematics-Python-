import json

file_path = '/home/bakame03/Documents/BUT1/Folders_Linked_With_GitHub/amu-Arles-_BUT1_Mathematics-Python-/MathematiqueDiscrete/S2_R2_07_Graphes/TP3/R2.07-TP3-NGANJI-Aldo-Alex.ipynb'

with open(file_path, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

new_code = """def bellman(g):
    # Entrées : un graphe G acyclique dont les sommets sont triés 
    # dans l'ordre topologique.
    N = g.topological_sort()
    
    # Initialisation : d(i) = +oo, et d(1) = 0
    D = {}
    for i in N:
        D[i] = Infinity
        
    # Le sommet de départ est le premier dans l'ordre topologique
    sommet_depart = N[0]
    D[sommet_depart] = 0
    
    # pour i = 2, ··· ,n faire (On saute le premier sommet)
    for i in N[1:]:
        # d(i) = min_{j dans N-(i)} (d(j) + f(j,i))
        # N-(i) représente les prédécesseurs de i
        # Dans SageMath, on peut utiliser incoming_edges(i) 
        # qui donne les arêtes entrantes (j, i, poids)
        candidats = []
        for j, _, f in g.incoming_edges(i):
            if D[j] != Infinity:
                candidats.append(D[j] + f)
                
        # j0= prédécesseur de i fournissant la valeur de d(i) ci-dessous
        if len(candidats) > 0:
            D[i] = min(candidats)
            
    return D
"""

for cell in notebook['cells']:
    if cell['cell_type'] == 'code':
        source = cell.get('source', [])
        if any('def bellman(g):' in line for line in source):
            cell['source'] = [line + '\n' for line in new_code.split('\n')][:-1]
            break

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print("Notebook updated.")
