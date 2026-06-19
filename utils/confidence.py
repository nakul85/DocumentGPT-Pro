from typing import List, Tuple


def calculate_confidence(
    results: List[Tuple]
) -> tuple[int, str]:
    """
    Calculate confidence from Chroma similarity scores.

    Returns
    -------
    (confidence_percentage, label)
    """

    if not results:
        return 0, "No Match"

    scores = []

    for _, distance in results:
        scores.append(distance)

    avg_distance = sum(scores) / len(scores)

    confidence = max(
        0,
        min(
            100,
            round((1 - avg_distance) * 100)
        )
    )

    if confidence >= 85:
        label = "High"

    elif confidence >= 65:
        label = "Medium"

    else:
        label = "Low"

    return confidence, label