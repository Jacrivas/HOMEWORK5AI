import random


def genetic_algorithm(population, fitness, max_generations=1000):
    def weighted_random_choice(population, weights):
        return random.choices(population, weights, k=2)

    def reproduce(parent1, parent2):
        n = len(parent1)
        c = random.randint(0, n - 1)
        return parent1[:c] + parent2[c:]

    def mutate(child, mutation_rate=0.01):

        child_list = list(child)
        for i in range(len(child_list)):
            if random.random() < mutation_rate:
                child_list[i] = '1' if child_list[i] == '0' else '0'
        return ''.join(child_list)

    def get_fitness_scores(population):
        return [fitness(individual) for individual in population]


    for generation in range(max_generations):

        fitness_scores = get_fitness_scores(population)

        if max(fitness_scores) >= 1.0:
            break


        population2 = []
        weights = [score / sum(fitness_scores) for score in fitness_scores]
        for _ in range(len(population)):
            parent1, parent2 = weighted_random_choice(population, weights)
            child = reproduce(parent1, parent2)


            if random.random() < 0.1:
                child = mutate(child)

            population2.append(child)


        population = population2


    return max(population, key=fitness)

def fitness_function(individual):

    return sum(int(bit) for bit in individual) / len(individual)


initial_population = ['10101', '00011', '11100', '11011', '01010']
best_individual = genetic_algorithm(initial_population, fitness_function)

print("Best individual:", best_individual)