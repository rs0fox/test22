from flask import Flask, render_template
import psycopg2  # For PostgreSQL, use `mysql-connector-python` for MySQL

app = Flask(__name__)

def get_scores():
    scores = []
    try:
        conn = psycopg2.connect("dbname=game_db user=your_user password=your_password host=db_host")
        cur = conn.cursor()
        cur.execute("SELECT username, score FROM scores ORDER BY score DESC")
        scores = cur.fetchall()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error retrieving scores: {e}")
    return scores

@app.route('/')
def index():
    scores = get_scores()
    return render_template('index.html', scores=scores)

if __name__ == "__main__":
    app.run(debug=True)
