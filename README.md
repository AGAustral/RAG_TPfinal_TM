El proyecto implementa RAG utilizando TinyLlama 1.1B y el indexador FAISS/MiniLM-L6-v2. Durante el diseño, enfrenté las siguientes dificultades principales:

1. Fallos Críticos de Fidelidad
Experimenté alucinación constante y fallos de fidelidad. Mi LLM (TinyLlama) demostró una alta propensión a inventar datos (ej., Ministerios incorrectos o acrónimos falsos), ignorando la instrucción de usar solo el contexto. Esto se debió en gran medida a la limitación intrínseca de los modelos de pequeña escala pero también a la mala estructura del formato del texto proporcionado, que además provoco la mezcla de conceptos, forzando a mi modelo a mezclar ideas (ej., la definición de CMO con motivos de inasistencia).

2. Desafíos de Recuperación (Retrieval)
La calidad de mi contexto fue un desafío central:

La división inicialmente asignada del texto generó "chunks" semánticamente rotos.

Para compensar la imprecisión del retrieval, tuve que aplicar una ingeniería de contexto extrema: utilicé un alto overlap de 100 a 150 palabras y aumenté la recuperación a k=6 documentos para saturar el prompt.

Finalmente, la latencia de TinyLlama en CPU utilizando el cacheo (@st.cache_resource) en Streamlit.

Conclusión (Importancia del Texto Fuente)
La implementación exitosa requirió una ingeniería de contexto agresiva para forzar la fidelidad del LLM. Esto demostró que el diseño y calidad de la Base de Datos Documental (BDD) es factor crítico para evitar que un modelo de lenguaje ligero alucine.
