import os
from flask import Flask, render_template, request
from google.cloud import bigquery

app = Flask(__name__)

# Set the environment variable to the path of your service account key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key1.json"

# Initialize BigQuery client
client = bigquery.Client()

# Define your BigQuery dataset and table
dataset_id = "demodata"  # Replace with your dataset ID
table_id = "Demotable"      # Replace with your table ID

@app.route("/", methods=["GET", "POST"])
def user_details():
    if request.method == "POST":
        Name = request.form["name"]
        Age = request.form["age"]

        # Insert data into BigQuery
        insert_data_into_bigquery(Name, Age)

        return render_template("new.html", name=Name, age=Age)

    return render_template("new.html")

def insert_data_into_bigquery(name, age):
    # Construct a BigQuery SQL statement
    sql = f"INSERT INTO `{dataset_id}.{table_id}` (name, age) VALUES ('{name}', {age})"

    # Run the SQL statement
    query_job = client.query(sql)

    # Wait for the query to complete
    query_job.result()

if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")
