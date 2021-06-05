from abc import ABC, abstractmethod

class BaseTrainer(ABC):
    """Simple abstract class for trainers."""

    @abstractmethod
    def compile_model(self):
        print("8. COMPILING MODEL")

    @abstractmethod
    def fit(self):
        print("9. TRAINING MODEL")

    @abstractmethod
    def evaluate(self):
        print("10. EVALUATING MODEL")

    @abstractmethod
    def predict(self):
        print("11. TEST PREDICTIONS")

    @abstractmethod
    def publish(self):
        print("12. PUBLISH MODELS")