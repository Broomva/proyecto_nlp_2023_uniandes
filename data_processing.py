#%%
# Create Training, Validation and Test Sets

import pandas as pd
from sklearn.model_selection import train_test_split

#%%
# Load the datasets
spa_guc_df = pd.read_csv('datasets/spa_guc/raw/spa_guc_dataset.csv', sep='|')
spa_pbb_df = pd.read_csv('datasets/spa_pbb/raw/spa_pbb_dataset.csv', sep='|')
# %%

spa_guc_train, spa_guc_test = train_test_split(spa_guc_df, test_size=0.2, random_state=42)
spa_guc_train, spa_guc_val = train_test_split(spa_guc_train, test_size=0.2, random_state=42)

spa_pbb_train, spa_pbb_test = train_test_split(spa_pbb_df, test_size=0.2, random_state=42)
spa_pbb_train, spa_pbb_val = train_test_split(spa_pbb_train, test_size=0.2, random_state=42)

#%%
# Save the datasets
spa_guc_train.to_csv('datasets/spa_guc/raw/spa_guc_train.csv', sep='|', index=False)
spa_guc_val.to_csv('datasets/spa_guc/raw/spa_guc_val.csv', sep='|', index=False)
spa_guc_test.to_csv('datasets/spa_guc/raw/spa_guc_test.csv', sep='|', index=False)

spa_pbb_train.to_csv('datasets/spa_pbb/raw/spa_pbb_train.csv', sep='|', index=False)
spa_pbb_val.to_csv('datasets/spa_pbb/raw/spa_pbb_val.csv', sep='|', index=False)
spa_pbb_test.to_csv('datasets/spa_pbb/raw/spa_pbb_test.csv', sep='|', index=False)

# %%
# Create Instruct Dataset
import random

templates = [
    "Translate from Spanish to Guc",
    "How would you express this in Guc?",
    "Render the following text from Spanish into Guc",
    "Convert this Spanish sentence to Guc",
    "Provide the Guc version of this Spanish text",
    "Interpret this Spanish phrase in Guc",
    "Change this from Spanish into Guc",
    "What is the Guc translation for the Spanish sentence",
    "Rewrite the below in Guc",
    "Translate this text into Guc from Spanish",
    "Give the Guc equivalent of this Spanish phrase",
    "Turn this Spanish sentence into Guc",
    "How to say this in Guc?",
    "Translate the following Spanish into Guc",
    "Provide a translation in Guc for this Spanish text",
    
    "Traduce del español al Guc",
    "¿Cómo dirías esto en Guc?",
    "Convierte este texto del español al Guc",
    "Transforma la siguiente frase de español a Guc",
    "Proporciona la versión en Guc de este texto en español",
    "Interpreta esta frase en español al Guc",
    "Cambia esto del español al Guc",
    "¿Cuál es la traducción en Guc de la frase en español?",
    "Reescribe lo siguiente en Guc",
    "Traduce este texto a Guc del español",
    "Da el equivalente en Guc de esta frase en español",
    "Convierte esta frase en español a Guc",
    "¿Cómo se dice esto en Guc?",
    "Traduce lo siguiente del español al Guc",
    "Proporciona una traducción en Guc para este texto en español",
    
    "Translate from Spanish to Wayuu",
    "Provide a Wayuu translation for this Spanish text",
    "Convert this from Spanish into Wayuu",
    "How is this said in Wayuu?",
    "What's the Wayuu version of this Spanish sentence",
    "Express this in Wayuu",
    "Transform the following Spanish into Wayuu",
    "Rewrite this Spanish phrase in Wayuu",
    "How would you interpret this in Wayuu?",
    "Turn the below Spanish text into Wayuu",
    "Convert the given Spanish sentence to Wayuu",
    "Translate the following into Wayuu from Spanish",
    "Provide the Wayuu equivalent of this Spanish phrase",
    "Change this Spanish text into Wayuu",
    "Render this Spanish sentence in Wayuu",
    
    "Traduce del español al Wayuu",
    "Proporciona una traducción en Wayuu para este texto en español",
    "Convierte esto de español a Wayuu",
    "¿Cómo se dice esto en Wayuu?",
    "¿Cuál es la versión en Wayuu de esta oración en español?",
    "Expresa esto en Wayuu",
    "Transforma el siguiente español a Wayuu",
    "Reescribe esta frase en español en Wayuu",
    "¿Cómo interpretarías esto en Wayuu?",
    "Convierte el siguiente texto en español a Wayuu",
    "Traduce la oración en español dada a Wayuu",
    "Traduce lo siguiente a Wayuu del español",
    "Proporciona el equivalente en Wayuu de esta frase en español",
    "Cambia este texto en español a Wayuu",
    "Representa esta oración en español en Wayuu",
    
    "Translate the following from Spanish to Wayuu Naiki",
    "Express this Spanish phrase in Wayuu Naiki",
    "Transform this Spanish text into Wayuu Naiki",
    "Convert this sentence from Spanish to Wayuu Naiki",
    "What is the Wayuu Naiki version of this Spanish text",
    "Provide a translation in Wayuu Naiki for the Spanish phrase",
    "How would you say this in Wayuu Naiki?",
    "Translate this from Spanish into Wayuu Naiki",
    "Render the Spanish sentence in Wayuu Naiki",
    "Interpret this in Wayuu Naiki",
    "Change this Spanish into Wayuu Naiki",
    "Rephrase this Spanish sentence in Wayuu Naiki",
    "Give the Wayuu Naiki translation for this Spanish text",
    "Turn this from Spanish into Wayuu Naiki",
    "How to express this in Wayuu Naiki?",
    
    "Traduce lo siguiente del español al Wayuu Naiki",
    "Expresa esta frase en español en Wayuu Naiki",
    "Transforma este texto en español a Wayuu Naiki",
    "Convierte esta oración del español al Wayuu Naiki",
    "¿Cuál es la versión en Wayuu Naiki de este texto en español?",
    "Proporciona una traducción en Wayuu Naiki para la frase en español",
    "¿Cómo dirías esto en Wayuu Naiki?",
    "Traduce esto del español al Wayuu Naiki",
    "Representa la oración en español en Wayuu Naiki",
    "Interpreta esto en Wayuu Naiki",
    "Cambia este español a Wayuu Naiki",
    "Reformula esta oración en español a Wayuu Naiki",
    "Da la traducción en Wayuu Naiki para este texto en español",
    "Convierte esto de español a Wayuu Naiki",
    "¿Cómo expresar esto en Wayuu Naiki?"
]


# Function to randomly select an instruction template
def random_instruction():
    return random.choice(templates)

# Add instruction column
spa_guc_df['instruction'] = spa_guc_df.apply(lambda row: random_instruction(), axis=1)

# Reorder columns to have 'instruction' first
spa_guc_df = spa_guc_df[['instruction', 'spa', 'guc']]

# Save to a new file or overwrite
spa_guc_df.to_csv("datasets/spa_guc/instruct/spa_guc_instruct.csv", sep='|', index=False)
# %%

instruct_spa_guc_train, instruct_spa_guc_test = train_test_split(spa_guc_df, test_size=0.2, random_state=42)
instruct_spa_guc_train, instruct_spa_guc_val = train_test_split(instruct_spa_guc_train, test_size=0.2, random_state=42)

# Save the datasets
instruct_spa_guc_train.to_csv('datasets/spa_guc/instruct/spa_guc_instruct_train.csv', sep='|', index=False)
instruct_spa_guc_val.to_csv('datasets/spa_guc/instruct/spa_guc_instruct_val.csv', sep='|', index=False)
instruct_spa_guc_test.to_csv('datasets/spa_guc/instruct/spa_guc_instruct_test.csv', sep='|', index=False)
# %%
