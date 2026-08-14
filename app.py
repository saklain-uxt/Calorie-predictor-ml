from flask import Flask, request, render_template

from src.pipline.predict_pipline import PredictPipeline, CustomData


application = Flask(__name__)

app = application


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():

    if request.method == 'GET':
        return render_template('home.html',results=None)

    else:
        print("FORM DATA:", request.form)

        data = CustomData(
            gender=request.form.get('gender'),
            age=float(request.form.get('age')),
            height=float(request.form.get('height')),
            weight=float(request.form.get('weight')),
            duration=float(request.form.get('duration')),
            heart_rate=float(request.form.get('heart_rate')),
            body_temp=float(request.form.get('body_temp'))
        )

        pred_df = data.get_data_as_data_frame()

        print("Input DataFrame:")
        print(pred_df)

        print("Before Prediction")

        predict_pipeline = PredictPipeline()

        print("Pipeline Created")

        results = predict_pipeline.predict(pred_df)

        print("After Prediction")
        print("Prediction:", results)

        return render_template(
            'home.html',
            results=results[0]
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)