# EJERCICIO 2 DEL EXAMEN 2024/2025

# APARTADO A:
# Diseñe e implemente una estrategia de preprocesamiento para las variables numéricas y categóricas. 
# Justifique brevemente sus decisiones.

# Como vemos en el dataset, tenemos variables numéricas y categóricas.
# También vemos que en un par de columnas tenemos algunos valores NaN por lo que habría que imputarlos.

# Primero vamos a separar de nuestro dataset la columna quality porque es a donde queremos llegar y el resto de
# columnas son las que vamos a utilizar para el entrenamiento.

x = wine.drop(columns = ["quality"]) # con esto sacamos la columna quality del dataset de entrenamiento
y = wine["quality"] # con esto guardamos la columna de quality para poder compararlo con el entrenamiento

# Ahora ponemos que tipo de columnas son categoricas y que tipo de columnas son numericas en nuesta x.

categoricas = ["color"]
numericas = ["alcohol", "sulfates", "pH"]

# Ahora imputamos las columnas sulfates y ph porque son las que tienen valores NaN y estandarizamos.

imputar_numericos = Pipeline([
    ("imputer", SimpleImputer(strategy = "median")),
    ("scaler", StandardScaler()) 
])

imputar_categoticos = Pipeline([
    ("imputer", SimpleImputer(strategy = "most_frequent")),
    ("one-hot", OneHotEncoder)
])

transformacion = columnTransformer(
    transformers = [
        ("numericas", imputar_numericos, numericas),
        ("categoricas", imputar_categoticos, categoricas) 
    ]
)


# APARTADO B:
# Seleccione y configure un modelo apropiado para este problema. Justifique su elección.

# Elegimos el modelo de regresión logística porque al tratarse de un problema de clasificación binaria,
# funciona correctamente con variables numéricas y categoricas imputadas y estandarizadas.

modelo = LogisticRegresion(
    max_iter = 1000,
    class_weight = "balanced"
)

modelo_final = Pipeline([
    ("procesamiento", transformacion),
    ("modelo", modelo)
])


# APARTADO C
# Seleccione una métrica de evaluación apropiada y evalúe el modelo usando validación
# cruzada con 5 folds. Justifique la elección de la métrica.

# Como dos posibles opciones de métrica poder elegir entre F1-score y AUC-ROC.
# En este caso elegiremos F1-score porque no nos dicen nada sobre si nos importa mas una clase
# que otra y no nos piden que los FN o los FP sean mas importantes unos que otros y por lo tanto
# como buscamos un equilibrio entre precision y recall, elijo F1-score.

modelo_fold = StratifiedKFold(n_splits = 5, shuffle = True, random_state = 0)

f1_score = cross_val_score(modelo_final, x, y, cv = modelo_fold, scoring = "f1")