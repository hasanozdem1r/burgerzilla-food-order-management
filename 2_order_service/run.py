"""
This script is created to run Order Microservice
Hasan Özdemir 02-07-2022
"""
# path : root/2_order_service/run.py


from flask import g
from flask_migrate import Migrate
from order_application import models
from flask_login import user_loaded_from_header
from order_application import create_app, db
from flask.sessions import SecureCookieSessionInterface


# initialize app object
app = create_app()
# migrations
migrate = Migrate(app, db)




# disabling Session Cookies for APIs
# further reading -> https://flask-login.readthedocs.io/en/latest/
class CustomSessionInterface(SecureCookieSessionInterface):
    """This prevents setting the Flask Session cookie whenever the user authenticated using your"""

    def save_session(self, *args, **kwargs):
        """
        This method is created to save session
        :param args: pass multiple arguments
        :param kwargs: pass keyword arguments
        :return:
        """
        if g.get('login_via_header'):
            return
        return super(CustomSessionInterface, self).save_session(*args,
                                                                **kwargs)

app.session_interface = CustomSessionInterface()

@user_loaded_from_header.connect
def user_loaded_from_header(self, user=None):
    g.login_via_header = True


if __name__ == '__main__':
    """
    Application Entry Point : Run Flask Application
    """
    app.run(host='0.0.0.0', port=5002)
