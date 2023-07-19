import datetime
import json
import users

# UDP_IP is localhost
UDP_IP = "127.0.0.1"


def handle_messages(sock, stop_event_messages, user):
    while not stop_event_messages.is_set():
        try:
            # Receive data from socket (buffer size: 1024 bytes)
            data, addr = sock.recvfrom(1024)

            # Decode received data
            message_json = data.decode()
            message = json.loads(message_json)

            # Handle the received message based on the recipient
            if message["recipient"] == message["sender"]:
                break
            elif message["recipient"] != "everyone":
                print(
                    f"Private message from {message['sender']} at {message['timestamp']}: {message['content']}"
                )
            elif message["recipient"] == "everyone":
                # Handle broadcast message
                print(
                    f"Broadcast message from {message['sender']}: {message['content']}"
                )
        except Exception as e:
            print("User is offline")


def send_message(sock, user):
    content, recipient = None, None
    while content == None:
        inputText = input("Enter your message : ")
        content = inputText if inputText != "" else None
    while recipient == None:
        inputText = input("To : ")
        recipient = users.get_user(inputText)
    # Example message format
    message = {
        "sender": user["name"],
        "recipient": recipient["name"],
        "content": content,
        "timestamp": datetime.datetime.now().isoformat(sep=" ", timespec="seconds"),
    }

    # Convert message to JSON string
    message_json = json.dumps(message)

    # Send message to a specific node
    sock.sendto(message_json.encode(), (UDP_IP, int(recipient["PORT"])))


def handle_user_input(sock, user, stop_event_input, stop_event_messages):
    while not stop_event_input.is_set():
        user_input = input("Enter 1 to send a message (or 'stop' to exit): ")

        if user_input == "1":
            # Call function 1
            send_message(sock, user)
        elif user_input == "stop":
            print("Stopping...")
            stop_event_input.set()
    stop_event_messages.set()
    self_message = {
        "sender": user["name"],
        "recipient": user["name"],
        "content": "Going offline",
        "timestamp": datetime.datetime.now().isoformat(sep=" ", timespec="seconds"),
    }
    self_message_json = json.dumps(self_message)
    sock.sendto(self_message_json.encode(), (UDP_IP, int(user["PORT"])))
