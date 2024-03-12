import pickle
from sklearn.ensemble import RandomForestClassifier

# Carregando previsores
with open('previsores.pkl', 'rb') as file:
    X = pickle.load(file)

# Carregando o alvo
with open('alvo.pkl', 'rb') as file:
    y = pickle.load(file)


model_rf = RandomForestClassifier(n_estimators = 150, criterion = 'gini', max_depth = 12, random_state=123)
model_rf.fit(X,y)