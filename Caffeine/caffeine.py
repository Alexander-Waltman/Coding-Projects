import math
import matplotlib.pyplot as plt

# half life in hours
HALF_LIFE = 5
# mg of caffeine in morning coffee
COFFEE = 200

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
    days = 5

    x_vals = list(range(8, 9 + 24*days))
    y_vals = []

    caff_lvl = 0
    for t in x_vals:
        # caffeine decay
        caff_lvl = caffeine_decay(caff_lvl, 1)

        # drink coffee at 8am
        if t % 24 == 8:
            caff_lvl += COFFEE
        
        y_vals.append(caff_lvl)

    plt.plot(x_vals, y_vals)
    plt.xlabel("Time (hours)")
    plt.ylabel("Caffeine (mg)")
    plt.title("Caffeine Levels over Time")
    plt.show()


if __name__ == "__main__":
    main()
