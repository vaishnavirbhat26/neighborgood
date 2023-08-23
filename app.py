from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Configure MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["interestsdb"]
collection = db["interestsdb"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/get_started')
def get_started():
    return render_template('form.html')

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    address = request.form["address"]
    other_activities = request.form["otherActivities"]
    activities = request.form.getlist("activities")

    user_data = {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address,
        "other_activities": other_activities,
        "activities": activities
    }

    collection.insert_one(user_data)

    return "Data submitted successfully!"

if __name__ == "__main__":
    app.run(debug=True)



# Connect to MongoDB Atlas
"""client = MongoClient('mongodb+srv://whyshnavi:DGuHyXevqLs53uum@cluster0.ucafotx.mongodb.net/?retryWrites=true&w=majority')
db = client['interests_db']
interests_collection = db['interests']

app.config['MONGO_URI'] = 'mongodb://localhost:27017/interestsdb'

mongo = PyMongo(app)






if __name__ == '__main__':
    app.run(debug=True)

# Serve the HTML form
@app.route('/formData')
def form():
    return app.send_static_file('form.html')"""































"""
# Handle form submission
@app.route('/submit', methods=['POST'])
def submit_interest():
    try:
        data = request.get_json()
        name = data['name']
        email = data['email']
        phone = data['phone']
        address = data['address']
        activities = data['activities']
        other_activities = data['otherActivities']

        interestsdb.insert_one({
            'name': name,
            'email': email,
            'phone': phone,
            'address': address,
            'activities': activities,
            'other_activities': other_activities
        })

        return jsonify({'message': 'Interest saved successfully'}), 201
    except Exception as e:
        return jsonify({'error': 'Error saving interest'}), 500
"""

if __name__ == '__main__':
    app.run(debug=True)
