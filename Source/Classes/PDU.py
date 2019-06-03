'''
PDU.py
class that every response will
give back
'''

class PDU:
    def __init__(self, message, session_id, version, data):
        self.message = message.value
        self.session_id = session_id
        self.version = version
        self.data = data