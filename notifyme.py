from flask import Flask, request
from win10toast import ToastNotifier
import threading

app = Flask(__name__)
toaster = ToastNotifier()

def show_notification(message):
    toaster.show_toast("Notification", message, duration=5)

@app.route('/notify', methods=['GET'])
def notify():
    message = request.args.get('message', 'No message provided')
    threading.Thread(target=show_notification, args=(message,)).start()
    return {"status": "success", "message": "Notification sent"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
