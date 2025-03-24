import queue
from collections import defaultdict
class PubSub:

    def __init__(self):
         self.listeners = defaultdict(list)

    def Subscribe(self,event_type: str):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        q = queue.Queue(maxsize=5)
        self.listeners[event_type].append(q)
        return q
    

    def format_msg(self, event, msg) -> str:
        #if event:
        #   return f'event:{event}\n{msg}'
        return f'data: {msg}\n\n'
    
    def Publish(self, msg,event=None):
        # print(f"Event is {event}")
        msg = self.format_msg(msg=msg,event=event)
        for i in reversed(range(len(self.listeners[event]))):
            try:
                self.listeners[event][i].put_nowait(msg)
            except queue.Full:
                 del self.listeners[event][i]
                 
    def Unsubscribe(self,event,queue):
        if event in self.listeners and queue in self.listeners[event]:
            self.listeners[event].remove(queue)

pubsub = PubSub()
