# import pickle
# import tensorflow as tf
# from keras.models import load_model
# import sklearn
# from flask import Flask, request

# # global variable
# global model, scaler

# def load():
#     global model, scaler
#     model = tf.keras.models.load_model(open('model/model.h5', 'rb'))
#     scaler = pickle.load(open('model/scaler_final.pkl', 'rb'))

# def prediksi(data):
#     # data = scaler.transform(data)
#     # prediksi = int(model.predict(data))
#     # nilai_kepercayaan = model.predict_proba(data).flatten()
#     # nilai_kepercayaan = max(nilai_kepercayaan) * 100
#     # nilai_kepercayaan = round(nilai_kepercayaan)
#     onehour = request.args.get('onehour', default = 1, type = int)
#     twohour = request.args.get('twohour', default = 1, type = int)
#     threehour = request.args.get('threehour', default = 1, type = int)

#     data = [[onehour],[twohour],[threehour]]
#     data = scaler.transform(data)
#     data = data.reshape(1,3,1)
#     pred = model.predict(data)
#     pred= scaler.inverse_transform(pred)
#     return str(pred.flat[0])

#     if prediksi == 0:
#         hasil_prediksi = "Tidak Resign"
#     else:
#         hasil_prediksi = "Akan Resign"
#     return hasil_prediksi, nilai_kepercayaan