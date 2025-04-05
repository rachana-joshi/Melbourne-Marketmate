from flask import Flask, jsonify, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

# ✅ Load live dataset from Google Sheets as CSV
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSiSUl6UU5tT1Wgjq2ns5XzZ5JmH3j1xZPs9DGI8dtfVZ7RhVPb9-kixWDV3GoCoZXgTwz4cMfCFYSg/pub?output=csv"

@app.route("/")
def client_dashboard():
    return render_template("client.html")

@app.route("/agent")
def agent_dashboard():
    return render_template("agent.html")

@app.route("/api/data")
def get_data():
    try:
        df = pd.read_csv(sheet_url)
        df = df.replace({np.nan: None})  # Replace NaNs for JSON compatibility
        return jsonify(df.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
