from music.mc_recommendations import give_me_recs
from flask import Flask

app = Flask(__name__)

@app.route('/')
def runApp():
    results = give_me_recs()
    df_json = results.to_json()
    df_html = results.to_html()
    return df_html, df_json

if __name__ == 'main':
    app.run()
