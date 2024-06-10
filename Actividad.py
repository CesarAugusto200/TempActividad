import pandas as pd
import matplotlib.pyplot as plt


file_path ='Actividad.xlsx'
data = pd.read_excel(file_path, header=None)

temperatures = data.values.flatten()

temperatures = temperatures[~pd.isnull(temperatures)]

temperatures_df = pd.DataFrame(temperatures, columns=['Temperature'])

possibilities = temperatures_df['Temperature'].value_counts().reset_index()
possibilities.columns = ['Temperature', 'Count']
print("Posibilidades del conjunto de datos:")
print(possibilities)


prob_greater_than_24 = (temperatures_df['Temperature'] > 24).mean()
print(f"\nProbabilidad de temperaturas mayores a 24 ºC: {prob_greater_than_24:.2%}")

prob_between_27_29 = temperatures_df['Temperature'].between(27, 29).mean()
print(f"Probabilidad de temperaturas entre 27 y 29 ºC: {prob_between_27_29:.2%}")


prob_even = (temperatures_df['Temperature'] % 2 == 0).mean()
prob_odd = 1 - prob_even
print(f"Probabilidad de temperaturas pares: {prob_even:.2%}")
print(f"Probabilidad de temperaturas impares: {prob_odd:.2%}")



frequency_table = temperatures_df['Temperature'].value_counts().sort_index().reset_index()
frequency_table.columns = ['Temperature', 'Frequency']

mean_temperature = temperatures_df['Temperature'].mean()
median_temperature = temperatures_df['Temperature'].median()
std_dev_temperature = temperatures_df['Temperature'].std()

print("\nTabla de Frecuencia:")
print(frequency_table)
print(f"\nMedidas de tendencia central y dispersión:")
print(f"Media: {mean_temperature:.2f}")
print(f"Mediana: {median_temperature:.2f}")
print(f"Desviación Estándar: {std_dev_temperature:.2f}")


plt.figure(figsize=(10, 6))
plt.hist(temperatures_df['Temperature'], bins=20, edgecolor='k', alpha=0.7)
plt.title('Histograma de Temperaturas')
plt.xlabel('Temperatura (ºC)')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()
