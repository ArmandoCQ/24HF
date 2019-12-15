from flaskblog import create_app

app = create_app()

if __name__ == '__main__':
#    app.run(debug=True)
    #To run in local network
    app.run(host=os.environ.get('IP_ADDRESS'),port=os.environ.get('port'))
    
