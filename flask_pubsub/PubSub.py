import queue
from collections import defaultdict
class PubSub:

    def __init__(self):
         self.listeners = defaultdict(list)
         self.pendingevent = defaultdict(list)

    def Subscribe(self,event_type: str):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        q = queue.Queue(maxsize=5)
        self.listeners[event_type].append(q)
        return q
    

    def format_msg(self, event, msg) -> str:
        if event:
          return f'event: {event}\ndata: {msg}\n\n'
        return f'data: {msg}\n\n'
    
    def Publish(self, msg,event=None):
        msg = self.format_msg(msg=msg,event=event)
        
        if len(self.listeners[event]) == 0:
            self.pendingevent[event].append(msg)
        
        for i in reversed(range(len(self.listeners[event]))):
            try:
                
               while  self.pendingevent[event] :
                   print(self.pendingevent[event])
                   self.listeners[event][i].put_nowait(self.pendingevent[event].pop())
                   
               self.listeners[event][i].put_nowait(msg)
            except queue.Full:
                 del self.listeners[event][i]
                 
    def Unsubscribe(self,event,queue):
        if event in self.listeners and queue in self.listeners[event]:
            self.listeners[event].remove(queue)

pubsub = PubSub()
