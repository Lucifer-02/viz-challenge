import pandas as pd
import numpy as np
import pyperclip


def to_vega_dataset(df: pd.DataFrame) -> list[dict]:
    return df.to_dict(orient="records")


def save_to_clipboard(text: str) -> None:
    pyperclip.copy(text)


def chart1():
    species = ["Adelie", "Chinstrap", "Gentoo"]
    sex_counts = {
        "Male": np.array([73, 34, 61]),
        "Female": np.array([73, 34, 58]),
    }

    data = pd.DataFrame(
        {
            "Species": species * 2,
            "Sex": ["Male"] * 3 + ["Female"] * 3,
            "Count": list(sex_counts["Male"]) + list(sex_counts["Female"]),
        }
    )
    print(data.to_dict(orient="records"))


def chart2():
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    # Example data
    n_samples = 2
    people = ("Tom", "Dick", "Harry", "Slim", "Jim")
    peoples = []
    for person in people:
        peoples += [person] * n_samples
    performance = (np.random.rand(len(people), n_samples) * 3 + 10).flatten()
    assert len(peoples) == len(performance)

    data = pd.DataFrame({"people": peoples, "performance": performance})

    print(data.to_dict(orient="records"))


def chart4():
    fruit_names = ["Coffee", "Salted Caramel", "Pistachio"]
    fruit_counts = [4000, 2000, 7000]

    data = pd.DataFrame({"fruit_names": fruit_names, "fruit_counts": fruit_counts})

    dataset = to_vega_dataset(data)
    print(dataset)
    save_to_clipboard(str(dataset))


def chart5():
    animal_names = ["Lion", "Gazelle", "Cheetah"]
    mph_speed = [50, 60, 75]

    data = pd.DataFrame({"animal_names": animal_names, "mph_speed": mph_speed})

    dataset = to_vega_dataset(data)
    print(dataset)
    save_to_clipboard(str(dataset))


if __name__ == "__main__":
    # chart1()
    # chart2()
    # chart 3 is chart 2
    # chart4()
    chart5()
