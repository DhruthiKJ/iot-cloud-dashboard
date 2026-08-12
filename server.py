from flask import Flask, request, jsonify
from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route("/sensor-data", methods=["POST"])
def receive_data():
    data = request.get_json()
    result = supabase.table("sensor_readings").insert(data).execute()
    print("Saved to Supabase:", data)
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)