import mc_recommendations as mc_recommendations
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
#revert
@app.route('/form')
def show_form():
    
    return render_template('form.html')
"""    
@app.route('/login')
def login():
    client_id = "c1f4309625494c848f3d90c0b3f96813"
    redirect_uri = "https://flask-milk-crate.vercel.app/form"
    scope = 'user-read-private user-read-email'
    authorization_url = f'https://accounts.spotify.com/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&scope={scope}'
    return redirect(authorization_url)
"""

    
@app.route('/process', methods=['POST'])
def process_input():
    input_value = request.form['input']

    # Split the URL by '/' and get the last part
    parts = input_value.split('/')
    playlist_id = parts[-1]

# Split the playlist ID by '?' and get the first part
    parts = playlist_id.split('?')
    playlist_id = parts[0]

    

    results = mc_recommendations.give_me_recs(input_value)
    df_json = results.to_json()
    #print(len(df_json))
    return df_json




if __name__ == 'main':
    app.run()
