import pickle
import json

class Stadium:
    def __init__(self, capacity, type):
        self.capacity = capacity
        self.type = type

    def pack_pickle(self, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(self, file)
        print('Data saved with pickle.')

    @staticmethod
    def unpack_pickle(file_path):
        with open(file_path, 'rb') as file:
            return pickle.load(file)
        print('Data loaded with pickle.')


o2_arena = Stadium(20000, 'multipurpose')
epet_arena = Stadium(18887, 'football')
fortuna_arena = Stadium(19370, 'football')

o2_arena.pack_pickle('stadiums.pkl')
unpacked_pickle = Stadium.unpack_pickle('stadium.pkl')
print('Unpacked Stadium from Pickle:', unpacked_pickle)
