from flask import g

def session_manager(transaction):
    def wrapper():
        try:
            return transaction()
        except:
            g.session.rollback()
            raise

    return wrapper

def return_500_if_errors(f):
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            response = {
                'status_code': 500,
                'status': 'Internal Server Error'
            }
            return flask.jsonify(response), 500
    return wrapper