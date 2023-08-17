# ITU-Markovian_Dynamic_programming-HW
Markovian Dynamic Programming for Living-Donor Liver Transplantation Model

(This task has been a homework of the course "advanced topics in Industrial Engineering) in Fall 2022 during my MSc)

In this GitHub repository, you will find code implementations that tackle the challenging problem of optimizing living-donor liver transplantation using Markovian dynamic programming techniques. 
**Please note that, due to strict data confidentiality and legal restrictions, only code files are provided here. The data files necessary for the complete execution of the code, as described in the assignment, cannot be shared.**

Task Overview:
The primary task of this assignment is to implement and apply a standard solution algorithm for Markov Decision Processes (MDPs) to the living-donor liver transplantation model. Specifically, given a patient characterized by a state space S = {1, 2, ..., H, Δ}, where integers from 1 to H represent MELD scores and Δ represents death, along with a known organ quality ℓ for a donor, the following optimality equations are solved:
v(h) = max(
    rT(h, ℓ),
    rW(h) + λ * Σ[h'∈S] (H{h' | h} * v(h'))
) for h ∈ S \ {Δ}, (1)

v(Δ) = 0, (2)

Key Components:
rT(h, ℓ): Represents the life expectancy from transplanting an organ of quality ℓ when the patient is in health state h.
rW(h): Indicates the life expectancy between two successive decision epochs.
λ: Denotes the daily discount rate.
H{h' | h}: Represents the probability of transitioning to state h' in time t+1, given that the patient is in state h in time t.
v(h): Represents the maximum life expectancy while the patient is in state h.


Feel free to explore, experiment, and adapt the provided code to solve similar optimization problems in the realm of healthcare and decision-making under uncertainty. Your feedback and contributions are highly appreciated!
