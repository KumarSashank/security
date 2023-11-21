#Implement RED algorithm DEC Bit scheme in TCP
import random

class Router:
    def __init__(self, max_queue_size, marking_threshold, marking_probability):
        self.queue = []
        self.max_queue_size = max_queue_size
        self.marking_threshold = marking_threshold
        self.marking_probability = marking_probability

    def enqueue_packet(self, packet):
        if len(self.queue) < self.max_queue_size:
            self.queue.append(packet)
        else:
            # Queue is full, decide whether to mark the packet
            if len(self.queue) >= self.marking_threshold:
                if random.random() < self.marking_probability:
                    packet.marked = True
                else:
                    packet.marked = False
            else:
                packet.marked = False

    def dequeue_packet(self):
        if self.queue:
            return self.queue.pop(0)
        return None

class Packet:
    def __init__(self, data):
        self.data = data
        self.marked = False

def main():
    router = Router(max_queue_size=10, marking_threshold=8, marking_probability=0.2)

    for packet_data in range(20):
        packet = Packet(packet_data)
        router.enqueue_packet(packet)

    for _ in range(20):
        packet = router.dequeue_packet()
        if packet:
            if packet.marked:
                print(f"Received marked packet: {packet.data}")
            else:
                print(f"Received unmarked packet: {packet.data}")
        else:
            print("Queue is empty.")

if __name__== "__main__":
    main()