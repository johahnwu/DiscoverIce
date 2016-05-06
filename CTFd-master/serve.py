import os
from CTFd import create_app
os.system('mysql<db_create.sql')
app = create_app()
app.debug = True
app.run(host="0.0.0.0", port=4000)
