import socket
import threading
import sys
import users
import messages


# UDP_IP is localhost
UDP_IP = "127.0.0.1"


def main():
    user = users.login()
    if not user:
        return
    print("Logged in as " + user["name"] + " on port " + str(user["PORT"]) + ".")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, int(user["PORT"])))

    stop_event_input = threading.Event()
    stop_event_messages = threading.Event()
    input_thread = threading.Thread(
        target=messages.handle_user_input,
        args=(sock, user, stop_event_input, stop_event_messages),
    )
    input_thread.start()

    message_thread = threading.Thread(
        target=messages.handle_messages, args=(sock, stop_event_messages, user)
    )
    message_thread.start()

    message_thread.join()
    input_thread.join()


if __name__ == "__main__":
    main()
