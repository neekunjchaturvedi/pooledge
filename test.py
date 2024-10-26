import math
from flask import Flask, jsonify, request

app = Flask(__name__)

def euclidean(coord1: tuple[float], coord2: tuple[float]) -> float:
    return math.sqrt(math.pow(coord1[0] - coord2[0], 2) + math.pow(coord1[1] - coord2[1], 2))

@app.route("/check", methods=["POST"])
def checkDistance():
    data = request.json
    lat1, lon1 = data.get("coord1")
    lat2, lon2 = data.get("coord2")

    distance = euclidean((lat1, lon1), (lat2, lon2))
    meters = distance * 111139  # Convert to meters
    answer = meters < 200

    return jsonify(result=answer, distance=meters)

if __name__ == "__main__":
    app.run(port=(5000),debug=True)