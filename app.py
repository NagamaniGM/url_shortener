from flask import Flask, request, redirect, render_template_string
import sqlite3, string, random

app = Flask(__name__)

# Initialize DB
def init_db():
    conn = sqlite3.connect("urls.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS urls (short TEXT, long TEXT)")
    conn.commit()
    conn.close()

def shorten_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        long_url = request.form["long_url"]
        short = shorten_url()
        conn = sqlite3.connect("urls.db")
        c = conn.cursor()
        c.execute("INSERT INTO urls VALUES (?, ?)", (short, long_url))
        conn.commit()
        conn.close()
        return f"Short URL: <a href='/{short}'>http://localhost:5000/{short}</a>"
    return render_template_string("""
        <h2>🔗 URL Shortener</h2>
        <form method="post">
            <input name="long_url" placeholder="Enter long URL" style="width:300px;" required>
            <button type="submit">Shorten</button>
        </form>
    """)

@app.route("/<short>")
def redirect_url(short):
    conn = sqlite3.connect("urls.db")
    c = conn.cursor()
    c.execute("SELECT long FROM urls WHERE short=?", (short,))
    row = c.fetchone()
    conn.close()
    if row:
        return redirect(row[0])
    return "URL not found!", 404

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
