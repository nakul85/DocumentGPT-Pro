from typing import List, Tuple


def calculate_retrieval_confidence(results: List[Tuple]):
    """
    Convert ChromaDB distances into a user-friendly confidence score.
    """

    if not results:
        return 0, "Low"

    distances = [score for _, score in results]

    avg_distance = sum(distances) / len(distances)

    # Calibrated mapping for ChromaDB distances
    confidence = max(
        0,
        min(
            100,
            round((1.0 - avg_distance / 1.2) * 100)
        )
    )

    if confidence >= 80:
        label = "Excellent"
    elif confidence >= 60:
        label = "High"
    elif confidence >= 40:
        label = "Medium"
    else:
        label = "Low"

    return confidence, label