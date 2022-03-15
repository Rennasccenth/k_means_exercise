from dotenv import load_dotenv
from pandas import DataFrame
from sklearn.cluster import KMeans

from configurations import Configurations
from src.repository.happiness_csv_repository import HappinessCSVRepository

load_dotenv()


# def generate_traning_data(rnd_state: int, n_samples: int | list) -> Tuple[np.ndarray, np.ndarray]:
#     """Generates data for training purposes.
#
#     :param n_samples: If int, it is the total number of points equally divided among clusters.
#     :param rnd_state: Determines random number generation for dataset creation."""
#     return make_blobs(n_samples=n_samples, random_state=rnd_state)

def custom_print(inp: str, out: str) -> None:
    print(f"Group {out} -> {inp} ")


if __name__ == '__main__':
    # Fetch configurations
    configurations = Configurations()

    # Creating and configurating kmeans
    kmeans = KMeans(
        n_clusters=configurations.N_CLUSTERS,
        # verbose=True
    )

    # Get repositories
    training_repository = HappinessCSVRepository(configurations.TRAINING_DATA_PATH)
    test_repository = HappinessCSVRepository(configurations.TESTING_DATA_PATH)

    # Fetch TRAINING data.
    training_dataframe: DataFrame = training_repository.get_data()
    # Fetch TEST data.
    test_dataframe: DataFrame = test_repository.get_data()

    new_training_df = training_dataframe.drop(columns=["Country or region"])
    new_test_df = test_dataframe.drop(columns=["Country or region"])

    # Training model with TRAINING data
    kmeans.fit(new_training_df)

    # Predict
    test_predictions = kmeans.predict(new_test_df)

    # Print
    [custom_print(inp, out) for inp, out in
     zip(test_dataframe["Country or region"], test_predictions)]
