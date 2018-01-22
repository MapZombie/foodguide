from flask import Flask
from app.views import application
application.secret_key = 'gfdsgdgr483hihero13h9e8fioea'
if __name__=="__main__":
    application.run(host='0.0.0.0', debug=True)

