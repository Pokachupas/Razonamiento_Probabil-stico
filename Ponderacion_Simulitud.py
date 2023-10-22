import random

# Distribución de probabilidad objetivo (ejemplo)
target_distribution = {
    'A': 0.3,
    'B': 0.4,
    'C': 0.2,
    'D': 0.1
}

# Función para calcular la similitud entre dos distribuciones (puede ajustarse según las necesidades)
def calculate_similarity(distribution1, distribution2):
    similarity = sum((distribution1[key] - distribution2[key]) ** 2 for key in distribution1)
    return similarity

# Función para realizar muestreo basado en ponderación de similitud
def similarity_weighted_sampling(target_distribution, num_samples):
    samples = []
    distribution_keys = list(target_distribution.keys())

    for _ in range(num_samples):
        sampled_value = random.choice(distribution_keys)
        samples.append(sampled_value)

    return samples

# Realizar muestreo basado en ponderación de similitud
num_samples = 1000
samples = similarity_weighted_sampling(target_distribution, num_samples)

# Contar la frecuencia de cada valor muestreado
sample_counts = {value: samples.count(value) / num_samples for value in set(samples)}

# Imprimir los resultados
print("Resultados del muestreo:")
for value, frequency in sample_counts.items():
    print(f"{value}: Frecuencia estimada: {frequency:.4f}, Probabilidad objetivo: {target_distribution[value]}")