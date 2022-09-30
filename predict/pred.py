import joblib

def f_prediction(a,b,c,d,e,f,g,h):
    # load the model 
    print(a,b,c,d,e,f,g,h)
    model = joblib.load('predict/diabetic_80.pkl')

    # Prediction
    data = model.predict([[a,b,c,d,e,f,g,h]])

    if data[0] == 0:
        data = 'person is not diabetic'
    else:
        data = 'person is diabetic'

    return data
