import logging
from flask import request, redirect, render_template
from flask_appbuilder.security.views import AuthRemoteUserView
from flask_appbuilder.security.forms import LoginForm_db
from flask_login import login_user, logout_user
from flask_appbuilder.hooks import before_request

logger = logging.getLogger()
class CustomRemoteAuthView(AuthRemoteUserView):
    @expose('/login/', methods=['GET', 'POST'])
    def login(self):
      username = request.environ['REMOTE_USER']
      logger.info("CustomRemoteAuthView[login]: username in request env {0}".format(username))
      if username == None:
        form = LoginForm_db()
        logger.info("CustomRemoteAuthView[login]:  did not find user login")
        login_template = 'appbuilder/login_db.html'
        return render_template(login_template, title='Superset-Remote-Auth', form=form, appbuilder=self.appbuilder)
      else:
        user = self.appbuilder.sm.auth_user_remote_user(username=username)
        logger.info("CustomRemoteAuthView[login]: Found user in remote {0}".format(user))
        login_user(user, remember=False)
        return redirect(self.appbuilder.get_url_for_index)


    @expose('/logout/', methods=['GET', 'POST'])
    def logout(self):
      logger.info("CustomRemoteAuthView[logout]: Logout request got cookies {0}".format(request.cookies))
      logout_user()
    
    @before_request
    def validate_request(self):
      logger.info("CustomRemoteAuthView[validate_request]: do pre request validation")

class CustomRemoteSecurityManager(SupersetSecurityManager):
         authremoteuserview = CustomRemoteAuthView
         def __init__(self, appbuilder):
                 super(CustomRemoteSecurityManager, self).__init__(appbuilder)