import time


class Sender:
    def __init__(self, window_size, receiver):
        self.window_size = window_size
        self.receiver = receiver
        self.base = 0
        self.next_seq_num = 0

    def send_data(self):
        while self.next_seq_num < self.base + self.window_size:
            if self.next_seq_num < self.receiver.buffer_size:
                print(f"Sending packet with sequence number {self.next_seq_num}")
                self.receiver.receive_data(self.next_seq_num)
                self.next_seq_num += 1
            else:
                print("Receiver buffer is full. Waiting...")
                time.sleep(1)

    def receive_ack(self, ack):
        if ack >= self.base:
            self.base = ack + 1
            print(f"Received ACK for packet with sequence number {ack}")


class Receiver:
    def __init__(self, buffer_size):
        self.buffer_size = buffer_size

    def receive_data(self, seq_num):
        print(f"Received packet with sequence number {seq_num}")
        # Simulate processing time
        time.sleep(1)
        self.send_ack(seq_num)

    def send_ack(self, ack):
        print(f"Sending ACK for packet with sequence number {ack}")
        # Provide the Sender instance as the first argument
        sender.receive_ack(ack)


sender = Sender(window_size=3, receiver=None)
receiver = Receiver(buffer_size=2)
sender.receiver = receiver

while True:
    sender.send_data()
    time.sleep(2)
