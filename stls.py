import numpy as np


class StlsComponent:
    """
    Base class for Sternberg's triangular love scale (STLS) component.
    """

    def __init__(self, scale_boundaries, factor):
        self.__scale = self.__create_scale_with_labels(
            scale_boundaries, factor)

    def score_answers(self, answers):
        """
        Computes the score for the given STLS component answers.

        Args:
            answers - the answers that are to be scored.

        Returns:
            The score and grouping for the given answers.
        """
        total_score = sum(map(lambda s: int(s), answers))
        closest_scale_boundary = min(self.__scale.keys(),
                                     key=lambda s: abs(total_score - s))

        return total_score, self.__scale[closest_scale_boundary]

    def __create_scale_with_labels(self, scale_boundaries, factor):
        group_labels = ["Significantly below average", "Somewhat below average",
                        "Average", "Somewhat above average", "Significantly above average"]

        return {round(score * factor): label for score,
                label in zip(scale_boundaries, group_labels)}


class IntimacyStls(StlsComponent):
    """
    Represents the intimacy component of STLS.
    """

    def __init__(self, factor=1):
        super().__init__([93, 102, 111, 120, 129], factor)


class PassionStls(StlsComponent):
    """
    Represents the passion component of STLS.
    """

    def __init__(self, factor=1):
        super().__init__([73, 85, 98, 110, 123], factor)


class CommitmentStls(StlsComponent):
    """
    Represents the commitment component of STLS.
    """

    def __init__(self, factor=1):
        super().__init__([85, 96, 108, 120, 131], factor)


class StlsEvaluator:
    def __init__(self, scale_factor):
        self.__component_strategies = [
            IntimacyStls(scale_factor), PassionStls(scale_factor), CommitmentStls(scale_factor)]

    def score(self, answers):
        answers_groups = np.array_split(
            answers, len(self.__component_strategies))

        return [strategy.score_answers(component_answers) for strategy, component_answers in zip(self.__component_strategies, answers_groups)]
