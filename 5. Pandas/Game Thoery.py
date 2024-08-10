import numpy as np

# Payoff Matrix for Prisoner's Dilemma
payoff_matrix = np.array([
    [(1, 1), (10, 0)],  # Cooperate, Cooperate  | Cooperate, Defect
    [(0, 10), (9, 9)]   # Defect, Cooperate    | Defect, Defect
])

def play_round(player1_strategy, player2_strategy):
    return payoff_matrix[player1_strategy][player2_strategy]

def play_multiple_rounds(num_rounds, player1_strategy, player2_strategy):
    total_payoff = [0, 0]
    for _ in range(num_rounds):
        round_payoff = play_round(player1_strategy, player2_strategy)
        total_payoff[0] += round_payoff[0]
        total_payoff[1] += round_payoff[1]
    return total_payoff

# Example usage
player1_strategy = 1  # 1 for Defect, 0 for Cooperate
player2_strategy = 1

round_payoff = play_round(player1_strategy, player2_strategy)
print("Single round payoff:", round_payoff)

multiple_rounds_payoff = play_multiple_rounds(5, player1_strategy, player2_strategy)
print("Payoff after 5 rounds:", multiple_rounds_payoff)