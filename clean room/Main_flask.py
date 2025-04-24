from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/Homepage')
def Homepage():
    return render_template('Homepage.html')

@app.route('/About Me')
def About_Me():
    return render_template('About Me.html', title="Halaman About Me")

@app.route('/Lagu Favorit')
def Lagu():
    return render_template('lagu.html', title="Halaman Lagu")

@app.route('/Projects')
def Projects():
    return render_template('Projects.html', title="Halamat Projects")

@app.route('/Contact')
def Contact():
    return render_template('Contact.html', title="Halamat Contact")

@app.route('/kasih', methods=['POST'])
def kasih():
    nama = request.form['nama']
    rate = request.form['rate']
    return f'Terima kasih {nama}, kamu mengasih rating {rate}'

if __name__ == "__main__":
    app.run(debug=True) #file hanya akan berjalan jika di run dari sini