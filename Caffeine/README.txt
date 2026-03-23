This script calculates the amount of caffeine left in someone's body after drinking coffee every day for a certain amount of time.
I used equations based on chemistry's first order integrated rate law, but it could also be done by thinking about it as exponential decay.
I made this script because I just randomly wondered if the amount of caffeine in someone's body would slowly accumulate over time if they always drank coffee, and I realized I had the knowledge and skills to just figure out it out.

The HALF_LIFE variable is based on an a number I found by googling the half-life of caffeine in the human body. It is by no means accurate for every person.

half life = ln(2)/k
ln([A]) = -kt + ln([A]_initial)
