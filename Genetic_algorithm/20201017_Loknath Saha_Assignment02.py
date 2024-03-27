import random

def fitness(selected_batsmen, target_run, batsmen):
    total_runs = sum([batsman[1] for i, batsman in enumerate(batsmen) if selected_batsmen[i] == 1])
    return total_runs - target_run

def crossover(parent1, parent2):
    point1 = random.randint(0, len(parent1) - 1)
    point2 = random.randint(point1, len(parent1) - 1)
    child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
    return child1, child2


def mutate(selected_batsmen, mutation_rate):
    mutated_batsmen = []
    for bit in selected_batsmen:
        if random.random() < mutation_rate:
            mutated_batsmen.append(1 - bit)  
        else:
            mutated_batsmen.append(bit)
    return mutated_batsmen

with open("Input1.txt", "r") as file:
    lines = file.readlines()
    n, target_run = map(int, lines[0].split())
    batsmen = [line.strip().split() for line in lines[1:]]
    batsmen = [(batsman[0], int(batsman[1])) for batsman in batsmen]


population_size = 30
mutation_rate = 0.01
max_generations = 100


population = [[random.choice([0, 1]) for _ in range(n)] for _ in range(population_size)]

solution_found = False

for generation in range(max_generations):
    fitness_scores = [fitness(selected_batsmen, target_run, batsmen) for selected_batsmen in population]


    if 0 in fitness_scores:
        solution_found = True
        break
    min_fitness = min(fitness_scores)
    fitness_scores = [score - min_fitness + 1 for score in fitness_scores]

    selected_parents = []
    for _ in range(population_size // 2):
        parent1, parent2 = random.choices(population, weights=fitness_scores, k=2)
        selected_parents.append((parent1, parent2))


    new_population = []
    for parent1, parent2 in selected_parents:
        child1, child2 = crossover(parent1, parent2)
        new_population.extend([child1, child2])

    new_population = [mutate(selected_batsmen, mutation_rate) for selected_batsmen in new_population]
    population = new_population

if solution_found:
    best_index = fitness_scores.index(0)
    final_solution = population[best_index]
    players = [batsmen[i][0] for i, bit in enumerate(final_solution)]
    binary_string = "".join(map(str, final_solution))
    print(players)
    print(binary_string)
else:
    print("-1")
