from application import app


#if something goes wrong debug allows to see what goes wrong, host on 0.0.0.0 makes it avliable for the wider internet
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')