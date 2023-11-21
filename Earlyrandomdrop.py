#Implement the Early Random Drop Buffer Management Policies. 

import random

class EarlyRandomDropQueue:
    def __init__(self, max_queue_size, drop_threshold, drop_probability):
        self.max_queue_size = max_queue_size
        self.drop_threshold = drop_threshold
        self.drop_probability = drop_probability
        self.queue = []

    def enqueue_packet(self, packet):
        if len(self.queue) < self.max_queue_size:
            self.queue.append(packet)
        else:
            if len(self.queue) >= self.drop_threshold and random.random() < self.drop_probability:
                print(f"Early dropping packet: {packet.data}")
            else:
                print(f"Replacing packet at index 0 with packet: {packet.data}")
                self.queue.pop(0)
                self.queue.append(packet)

    def dequeue_packet(self):
        if self.queue:
            return self.queue.pop(0)
        return None

class Packet:
    def __init__(self, data):
        self.data = data

def main():
    max_queue_size = 10
    drop_threshold = 8
    drop_probability = 0.2
    queue = EarlyRandomDropQueue(max_queue_size, drop_threshold, drop_probability)

    for packet_data in range(15):
        packet = Packet(packet_data)
        queue.enqueue_packet(packet)

    for _ in range(15):
        packet = queue.dequeue_packet()
        if packet:
            print(f"Received packet: {packet.data}")
        else:
            print("Queue is empty.")

if __name__ == "__main__":
    main()