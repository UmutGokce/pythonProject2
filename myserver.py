# using eventlet, visit the docs for more info
import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def my_message(sid, data):
    print('message ', data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    #burada 5000.portu dinliyoruz fakat raspberry'de boş olduğunu emin olduğumuz herhangi bir port dinlenebilir.
    # leave the 'localhost' empty string to run on your IP
    eventlet.wsgi.server(eventlet.listen(('localhost', 5000)), app)