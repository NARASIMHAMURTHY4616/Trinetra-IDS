from flask import Flask, render_template
from threading import Thread

from capture.net_sniffer import packet_detect, ui_packets, total_packets

app = Flask(__name__)


@app.route("/")
def dashboard():
    return render_template(
        "dashboard.html",
        total_packets=total_packets,
        packets=ui_packets[-50:]      # Show last 50 packets
    )


def start_sniffer():
    packet_detect()


if __name__ == "__main__":

    # Start packet sniffer in background
    sniffer_thread = Thread(target=start_sniffer)
    sniffer_thread.daemon = True
    sniffer_thread.start()

    # Start Flask
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
