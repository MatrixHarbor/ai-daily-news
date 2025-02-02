'''
ComputingBit defines an API containing 3 methods that must be implemented by the
Qubit subclass:
1. probability_amplitudes
2. validate_amplitudes
3. experiment
'''
from abc import ABC, abstractmethod

class ComputingBit(ABC):
    @abstractmethod
    def probability_amplitudes(self):
        """
        Abstract method to calculate probability amplitudes.
        Must be implemented by the Qubit subclass.
        """
        raise NotImplementedError("Did you implement the 'probability_amplitudes' method?")

    @abstractmethod
    def validate_amplitudes(self):
        """
        Abstract method to validate the provided amplitudes.
        Must be implemented by the Qubit subclass.
        """
        raise NotImplementedError("Did you implement the 'validate_amplitudes' method?")

    @abstractmethod
    def experiment(self):
        """
        Abstract method to perform a quantum experiment.
        Must be implemented by the Qubit subclass.
        """
        raise NotImplementedError("Did you implement the 'experiment' method?")
