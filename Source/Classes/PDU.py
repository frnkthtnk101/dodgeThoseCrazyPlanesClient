'''
PDU.py
class that every response will
give back
'''

class PDU:
    def __init__(self, message, session_id, version, data):
        self.Message = str(message.value)
        self.SessionId = session_id
        self.Version = version
        self.Data = data