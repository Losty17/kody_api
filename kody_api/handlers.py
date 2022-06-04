from sqlalchemy.exc import DatabaseError, IntegrityError
from .app import app


@app.errorhandler(404)
def not_found(e):
    return {"error": "the requested resource was not found"}, 404


@app.errorhandler(500)
def internal_error(e):
    return {"error": "internal error"}, 500


@app.errorhandler(IntegrityError)
def constraint_error(e):
    return {"error": "a constraint failed"}, 409


@app.errorhandler(DatabaseError)
def database_error(e):
    return {"error": "a error ocurred in the database"}, 500


@app.errorhandler(400)
def bad_request(e):
    return {"error": "bad request"}, 400


@app.errorhandler(Exception)
def undocumented_exception(e):
    return {"error": f"unhandled error, contact your administrator"}
