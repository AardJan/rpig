from flask import Flask, render_template, request
import get_info_data as gid

app = Flask(__name__)

@app.route("/")
def home():
    sm = gid.get_soil_moisture()
    temperature, humidity = gid.get_temp_and_humidity()
    return render_template('index.html',
                            sm = sm,
                            temperature = temperature,
                            humidity = humidity )

@app.route("/temp")
def temp():
    return render_template()

@app.route("/api/iot", methods=['GET', 'POST'])
def api_iot():
    content_json = request.json
    print(content_json)
    return "ok"
    
if __name__ == "__main__":
    app.run(host='192.168.0.101', port=5001)