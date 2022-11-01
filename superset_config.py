import os
import pkg_resources

SUPERSET_LOG_VIEW = True

BASE_DIR = pkg_resources.resource_filename("superset", "")
if "SUPERSET_HOME" in os.environ:
    DATA_DIR = os.environ["SUPERSET_HOME"]
else:
    DATA_DIR = os.path.expanduser("~/.superset")



ENABLE_TIME_ROTATE = True
TIME_ROTATE_LOG_LEVEL = "DEBUG"
FILENAME = os.path.join(DATA_DIR, "superset.log")
ROLLOVER = "midnight"
INTERVAL = 1
BACKUP_COUNT = 30


from custom_remote_security_manager import CustomRemoteSecurityManager
from flask_appbuilder.security.manager import AUTH_REMOTE_USER

AUTH_TYPE = AUTH_REMOTE_USER
CUSTOM_SECURITY_MANAGER = CustomRemoteSecurityManager


FEATURE_FLAGS = {
  'THUMBNAILS': True,
  'THUMBNAILS_SQLA_LISTENERS' : True,
  'DASHBOARD_CACHE' : True,
  'UX_BETA' : True,
  'LISTVIEWS_DEFAULT_CARD_VIEW' : True,
  'ENABLE_REACT_CRUD_VIEWS' : True,
  'DASHBOARD_NATIVE_FILTERS' : True,
  'DASHBOARD_CROSS_FILTERS' : True,
  'VERSIONED_EXPORT' : True,
  'DASHBOARD_RBAC': True,
  'ENABLE_TEMPLATE_PROCESSING': True
  }