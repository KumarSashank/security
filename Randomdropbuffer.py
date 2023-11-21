#Implement the Random Drop Buffer Management Policies:                                    

import random

class RandomDropQueue:
    def __init__(self, max_queue_size):
        self.max_queue_size = max_queue_size
        self.queue = []

    def enqueue_packet(self, packet):
        if len(self.queue) < self.max_queue_size:
            self.queue.append(packet)
        else:
            if random.random() < 0.5:
                print(f"Dropping packet: {packet.data}")
            else:
                # Replace a random packet in the queue
                random_index = random.randint(0, self.max_queue_size - 1)
                print(f"Replacing packet at index {random_index} with packet: {packet.data}")
                self.queue[random_index] = packet

    def dequeue_packet(self):
        if self.queue:
            return self.queue.pop(0)
        return None

class Packet:
    def __init__(self, data):
        self.data = data

def main():
    max_queue_size = 10
    queue = RandomDropQueue(max_queue_size)

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