import music.mc_recommendations as mc_recommendations
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/form')
def show_form():
    
    return render_template('form.html')
    



    


@app.route('/process', methods=['POST'])
def process_input():
    input_value = request.form['input']
    parts = input_value.split('/')
    playlist_id = parts[-1]
    parts = playlist_id.split('?')
    playlist_id = parts[0]

    

    results = mc_recommendations.give_me_recs(input_value)
    df_json = results.to_json()
    #print(len(df_json))
    return df_json




if __name__ == 'main':
    app.run()