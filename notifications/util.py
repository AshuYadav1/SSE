import queue

# Global event queue to hold SSE events
sse_event_queue = queue.Queue()

def send_sse_event(message):

    sse_event_queue.put(message)
