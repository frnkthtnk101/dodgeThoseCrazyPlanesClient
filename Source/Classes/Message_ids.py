from enum import Enum

class Message_ids(Enum):
    INTIALIZE_GAME = (0).to_bytes(1, byteorder='big')
    CANNOT_INITIALIZE_GAME = (1).to_bytes(1, byteorder='big')
    RECEIVE_SESSION_ID = (2).to_bytes(1, byteorder='big')
    END_GAME = (3).to_bytes(1, byteorder='big')
    QUIT_GAME = (4).to_bytes(1, byteorder='big')
    OK = (5).to_bytes(1, byteorder='big')
    SEND_SESSION_ID = (6).to_bytes(1, byteorder='big')
    BAD_SESSION_ID = (7).to_bytes(1, byteorder='big')
    GET_LEVEL = (8).to_bytes(1, byteorder='big')
    RECEIVE_LEVEL = (9).to_bytes(1, byteorder='big')
    BAD_LEVEL = (10).to_bytes(1, byteorder='big')
    ERROR = (11).to_bytes(1, byteorder='big')

