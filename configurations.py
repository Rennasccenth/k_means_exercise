import os


class Configurations:
    def __init__(self):
        self.TRAINING_DATA_PATH: str = os.getenv("TRAINING_DATA_PATH")
        self.TESTING_DATA_PATH: str = os.getenv("TESTING_DATA_PATH")
        self.RANDOM_STATE: int = int(os.getenv("RANDOM_STATE"))
        self.N_SAMPLES: int = int(os.getenv("N_SAMPLES"))
        self.N_CLUSTERS: int = int(os.getenv("N_CLUSTERS"))
