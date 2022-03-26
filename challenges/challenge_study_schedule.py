def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    counter = 0

    for initial_index, final_index in permanence_period:
        if not (
            isinstance(initial_index, int) and isinstance(final_index, int)
        ):
            return None

        if initial_index <= target_time <= final_index:
            counter += 1

    return counter


# permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

# print(study_schedule(permanence_period, 2))
