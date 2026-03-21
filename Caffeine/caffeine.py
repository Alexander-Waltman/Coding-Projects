import math

HALF_LIFE = 5

def caffeine_decay(initial_mg: float, time: float, half_life: float = HALF_LIFE):
    """
    Calculates the amount of caffeine left in someone's body after a given amount of time

    Parameters:
    initial_mg (type: float) - initial amount of caffeine in mg
    time (type: float) - time passed in hours
    half_life (type: float) - half life of caffeine in hours

    Returns:
    (type: float) - amount of caffeine in mg left after given amount of time has passed
    """

    #input validation
    if (initial_mg < 0) or (time < 0) or (half_life < 0):
        raise ValueError("Negative value input in caffeine_left function")
    

    # decay calculation
    rate_constant = math.log(2)/half_life
    final_mg = initial_mg * (math.e ** (-rate_constant * time))

    return final_mg


def main():
    # mg caffeine in morning coffee
    coffee = 200

    # days to run simulation for
    days = 100

    caffeine_8am = coffee
    for i in range(days):
        caffeine_10pm = caffeine_decay(caffeine_8am, 14)
        caffeine_8am = caffeine_decay(caffeine_10pm, 10) + coffee

    print(f"Caffeine at bedtime: {caffeine_10pm}")
    print(f"Caffeine just before coffee: {caffeine_8am - coffee}")


if __name__ == "__main__":
    main()
