"""Dataset class to be extended by dataset-specific classes."""
from abc import ABC, abstractmethod


class BaseDataset(ABC):
    """Simple abstract class for datasets."""

    @abstractmethod
    def load_interactions(self):
        """Load the main interaction data into a dataframe"""
        print("1. LOADING ALL USER INTERACTIONS")

    @abstractmethod
    def load_additional_features(self):
        """Load any additional features needed into a dataframe"""
        print("2. LOADING ADDITIONAL FEATURES")

    @abstractmethod
    def combine_additional_features(self):
        """Merge any additional features needed with the main interaction dataframe"""
        print("3. COMBINING ADDITIONAL FEATURES WITH INTERACTION DATA")

    @abstractmethod
    def transform_dataset(self):
        """Transform main interaction dataframe via a series of transform steps/methods"""
        print("4. PRE-PROCESSING INTERACTION DATA")

    @abstractmethod
    def convert_dataframe_to_tf(self):
        """Convert dataframe to a suitable tensorflow dataset format for feeding to models"""
        print("5. CONVERTING DF TO TF DATASET")

    @abstractmethod
    def split_train_valid_test(self):
        """Split the interaction data into train, validation and test sets"""
        print("6. SPLITTING THE DATA INTO TRAIN, VALID, TEST SETS")

    @abstractmethod
    def build_data_transform_dictionaries(self):
        """Build dictionaries to map/encode feature variables to latent embeddings"""
        print("7. BUILD DATA TRANSFORM DICTIONARIES")

    @abstractmethod
    def create_candidate_list(self):
        """Create a list of canidates (e.g. skus, styles) to be used for collaborative filtering"""
        print("8. CREATE LIST OF CANDIDATES")

    @abstractmethod
    def log_data(self):
        """log training data to wandb"""
        print("9. LOG DATA TO WANDB")


    def load_all_data(self):
        print("0. PREPARING FULL DATASET FOR TRAINING...")
        self.load_interactions()
        self.load_additional_features()
        self.combine_additional_features()
        self.transform_dataset()
        self.create_candidate_list()
        self.convert_dataframe_to_tf()
        self.split_train_valid_test()
        self.build_data_transform_dictionaries()
        self.log_data()