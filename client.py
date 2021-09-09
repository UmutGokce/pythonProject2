import socketio

sio = socketio.Client()


def sensorReads():  #sonsuz döngüde temsili sıcaklıkı 75 yazar
    while True:
        sio.emit('my_message', {'temp':75})
        sio.sleep(5)
@sio.event
def connect(): #bağlantı kurulduğu gibi sensorReads fonksiyonunu çalıştırır.
    print('connection established')
    sio.start_background_task(sensorReads())


@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:5000/') #5000.porttan bağlantı yapılıyor çünkü server 5000.portu dinliyor.
sio.wait()
