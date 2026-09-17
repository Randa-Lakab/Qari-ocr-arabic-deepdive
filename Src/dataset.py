import random
from datasets import load_dataset


def load_muharaf_dataset():
    muharaf = load_dataset("aamijar/muharaf-public")
    return muharaf


def build_historical_test_set(muharaf, n_historical=8):
    historical_indices = random.sample(
        range(len(muharaf["train"])),
        n_historical
    )

    historical_test_set = []

    for i, idx in enumerate(historical_indices):
        row = muharaf["train"][idx]

        img = row["image"]
        gt = row["text"]

        path = f"test_images/historical_{i:02d}.png"
        img.save(path)

        historical_test_set.append({
            "id": f"historical_{i:02d}",
            "image_path": path,
            "ground_truth": gt
        })

    return historical_test_set