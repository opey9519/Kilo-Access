import azure.functions as func
from azure.functions import WsgiMiddleware
from wsgi import app as flask_app

app = func.FunctionApp()


@app.function_name(name="api")
@app.route(route="{*route}", auth_level=func.AuthLevel.ANONYMOUS)
def main(req: func.HttpRequest, context: func.Context):
    return WsgiMiddleware(flask_app).handle(req, context)
