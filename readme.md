## flask hot reload
http://flask.pocoo.org/docs/1.0/cli/

<!-- powershell -->
```powershell
# flask03-small_restful_api

$env:FLASK_ENV = "development"
$env:FLASK_APP = "server"
flask run
```
<<<<<<< HEAD
`$env:FLASK_APP = "server" ` (這裡的 server 表示 server.py)
=======
```$env:FLASK_APP = "server" (這裡的 server 表示 server.py)```
>>>>>>> f06e910dab64369a550740b19108119766fddb44
執行後，還需要刷新網頁，才能看結果

