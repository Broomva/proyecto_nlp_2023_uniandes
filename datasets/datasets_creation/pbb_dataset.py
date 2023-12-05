#%% 
import pandas as pd

#%%
dataset_1 = pd.read_csv('files/constitucion_nasa_yuwe_spanish.csv', sep = '|')
# %%

dataset_2  = pd.read_csv('files/diccionario_nasa_yuwe.csv', sep = '|')

# %%

dataset_3 = pd.read_csv('files/palabras_importantes_nasa_yuwe_spanish.csv', sep = '|')
dataset_3 = dataset_3.reindex(columns=['pbb', 'spa'])

# %%

spa_pbb_dataset = pd.concat([dataset_1, dataset_2, dataset_3], ignore_index=True)
# %%
spa_pbb_dataset.to_csv('files/spa_pbb_dataset.csv', index=False, sep="|")
# %%

word_counts = spa_pbb_dataset['spa'].apply(lambda x: len(x.split()))

total_words = word_counts.sum()

print(f'Total number of words in the "spa" column: {total_words}')
# %%
num_records = spa_pbb_dataset.shape[0]

print(f'Number of records in the DataFrame: {num_records}')
# %%
unique_words = set()

for text in spa_pbb_dataset['spa']:
    unique_words.update(text.split())

num_unique_words = len(unique_words)

print(f'Number of unique words in the "spa" column: {num_unique_words}')

# %%
