import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

def load_data():
    iris = load_iris()
    X, y = iris.data, iris.target
    return X, y 

def train_model(X, y):
    clf = RandomForestClassifier()
    clf.fit(X, y)
    return clf


def save_model(clf):
    joblib.dump(clf, 'model.joblib')
    print('Model saved')
    

def main():
    X, y = load_data()
    clf = train_model(X, y)
    save_model(clf)


if __name__ == '__main__':
    main()