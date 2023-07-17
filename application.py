from myresume import create_app



application = create_app('testing')
if __name__ == "__main__":
    application.run(debug=True)