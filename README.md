# Proyecto Curso NLP 2023-2 UniAndes

## Integrantes

Laura Rodriguez

Alma Trigos

Miguel Ruiz

Carlos Escobar

## Descripción

El proposito del proyecto fue entrenar modelos de lenguage para traducción de español a lenguas indigenas (Wayuu y Nasa Yuwe). Se utilizo la libreria de Hugging Face para entrenar los modelos de lenguage y cargarlos al hub de modelos.

El repositorio incluye tres carpetas:

- **datasets**: Contiene los datasets utilizados para entrenar los modelos de lenguage. Incluye los scripts para procesar el texto para los modelos de traducción e instrucción.
- **training**: Contiene los scripts para entrenar los modelos de lenguage, usando transformers y fine tuning de llama 2.
- **inference**: Contiene los scripts para cargar los modelos de lenguage y realizar inferencia.

## Instrucciones

### Datos

Los datos 'raw' se encuentran en la carpeta datasets. Alli, para cada lenguage, hay un script para convertir el dataset paralelo a un conjunto valido para entrenar los modelos de lenguaje, ya sea para traduccion en transformers o con instruccion para fine tuning en llama 2. Estos scripts generan el dataset y lo cargan en el hub de datasets de Hugging Face.

### Entrenamiento

Hay dos opciones de entrenamiento:

- Con transformers como T5, BART, MT5, entrenados desde el archivo 'transformer_translation_training.ipynb'. Este notebook recibe tres parametros base, que son el lenguage de origen, el lenguage de destino y el nombre del modelo. El script usa el dataset del hub de datasets de Hugging Face y entrena el modelo de lenguage. Al finalizar, guarda el modelo en el hub de modelos de Hugging Face.

- Con fine tuning de llama 2 mediante el dataset de instruccion. Al igual que el anterior, recibe tres parametros base, que son el lenguage de origen, el lenguage de destino y el nombre del modelo, entrena el modelo y lo carga al hub de modelos de Hugging Face.

### Inferencia

Tambien hay dos opciones, para inferir con los modelos de lenguage:

- Con transformers como T5, BART, MT5, entrenados desde el archivo 'transformer_translation_inference.ipynb'. Este notebook recibe tres parametros base, que son el lenguage de origen, el lenguage de destino y el nombre del modelo. El script carga el modelo del hub de modelos de Hugging Face y realiza inferencia con el modelo.

- Con fine tuning de llama 2 mediante el dataset de instruccion. Al igual que el anterior, recibe tres parametros base, que son el lenguage de origen, el lenguage de destino y el nombre del modelo, carga el modelo del hub de modelos de Hugging Face y realiza inferencia con el modelo.

### Resultados

Todos los procesos de entrenamiento se registraron en Weight & Biases. Los resultados se pueden consultar en el reporte de entrenamiento en el siguiente [SPA-GUC/PBB Fine Tuning](https://api.wandb.ai/links/broomva/88p32d6r).

Adicionalme, se incluye un reporte/paper donde se discute a detalle el proceso de entrenamiento y los resultados obtenidos. El reporte se encuentra en la carpeta 'paper'.

