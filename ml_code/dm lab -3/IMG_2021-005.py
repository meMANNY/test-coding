import numpy as np

# question 1
def sphere_function(individual):
    return np.sum(np.square(individual))

# question 2
def gaussian_mutation(individual, mutation_prob=0.5, mutation_scale=0.1):
    if np.random.rand() < mutation_prob:
        mutation_vector = np.random.normal(0, mutation_scale, size=len(individual))
        individual += mutation_vector
        return True  
    return False 


def swap_mutation(individual, mutation_prob=0.5):
    if np.random.rand() < mutation_prob:
        idx1, idx2 = np.random.choice(len(individual), 2, replace=False)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
        return True  
    return False 

# question 3
def blended_crossover(parent1, parent2, alpha=0.5):
    child = np.zeros_like(parent1)
    for i in range(len(parent1)):
        if np.random.rand() < 0.5:
            child[i] = parent1[i]  
        else:
            gamma = (1 + 2 * alpha) * np.random.rand() - alpha
            child[i] = (1 - gamma) * parent1[i] + gamma * parent2[i]  
    return child

# question 4,5,6,7
def evolutionary_algorithm(n_genes, pop_size=250, mutation_scale=0.1, alpha=0.5, elite_count=3):
    
    generations = int(50000 / n_genes)
    
    population = np.random.uniform(-5.12, 5.12, (pop_size, n_genes))
    best_fitness_overall = float('inf')
    
    mutation_successes = 0
    mutation_attempts = 0
    crossover_successes = 0
    crossover_attempts = 0

    for generation in range(generations):
        
        fitness_values = np.array([sphere_function(ind) for ind in population])
        sorted_indices = np.argsort(fitness_values)
        
        best_fitness = fitness_values[sorted_indices[0]]
        worst_fitness = fitness_values[sorted_indices[-1]]
        average_fitness = np.mean(fitness_values)
        
        if best_fitness < best_fitness_overall:
            best_fitness_overall = best_fitness
        
        
        elites = population[sorted_indices[:elite_count]]
        
        
        new_population = []
        
        
        new_population.extend(elites)
        
        
        for _ in range((pop_size - elite_count) * 9 // 10):
            parent_indices = np.random.choice(elite_count, 2, replace=False) 
            parent1, parent2 = elites[parent_indices[0]], elites[parent_indices[1]]
            
        
            child = blended_crossover(parent1, parent2, alpha)
            crossover_attempts += 1
            crossover_successes += 1
            
            
            mutation_attempts += 1
            if gaussian_mutation(child, mutation_scale=mutation_scale):
                mutation_successes += 1
            else:
                if swap_mutation(child):
                    mutation_successes += 1
            
            new_population.append(child)
        
        
        random_individuals = np.random.uniform(-5.12, 5.12, (pop_size // 10, n_genes))
        new_population.extend(random_individuals)
        
        
        population = np.array(new_population)

        
        print(f"Generation {generation+1}/{generations}:")
        print(f"  Best fitness: {best_fitness}")
        print(f"  Average fitness: {average_fitness}")
        print(f"  Worst fitness: {worst_fitness}")
    
    
    print("\nFinal Stats:")
    print(f"Best fitness overall: {best_fitness_overall}")
    print(f"Mutation success rate: {mutation_successes/mutation_attempts:.2f}")
    print(f"Crossover success rate: {crossover_successes/crossover_attempts:.2f}")

# repeated for 
for n_genes in range(25, 501, 25):
    print(f"\nRunning evolutionary algorithm for {n_genes} genes and population size 250:")
    evolutionary_algorithm(n_genes=n_genes)

#CREATING AN OUTPUT FILE
