from flask import Falsk

app = Flask(__name__)

#route: http://www.bth.se/"den här delen av en länk"/

@app.route("/") #appens route
def main():
    print("hello python")
    return("hej")


@app.rout("/test")
def do_test():
    f = 3 + "fel"
    return "test från do_test():{f} är det här."



@app.errorhandler(500)
def internal_server_error(_):
    """
    Handler for internal server error 500
    """
    return "<pre>" + traceback.format_exc()


if __name__ == "__main__":
    app.run()
