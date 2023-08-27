import random
import matplotlib.pyplot as plt

# Simulate the game of randomly selecting coins from a box
def simulation(num_simulations):
    correct_answers = 0
    answers = []
    red_count = 0
    white_count = 0
    
    total_answers = 0
    
    for i in range(num_simulations):
        # Simulate selecting a coin randomly from the box with colors ['RR', 'WW', 'RW']
        coins = ['RR', 'WW', 'RW'][random.randint(0, 2)]
        # Randomly determine which side of the selected coin is facing up
        top_side = coins[random.randint(0, 1)]
        bottom_side = coins[1 - coins.index(top_side)]
        
        # Check if the bottom side is red ('R') to count correct answers
        if bottom_side == 'R':
            correct_answers += 1
        
        # Count the occurrences of red and white on the top side
        if top_side == 'R':
            red_count += 1
        else:
            white_count += 1
            
        total_answers += 1
        
        # Calculate probabilities of red and white colors based on current counts
        red_probability = red_count / total_answers
        white_probability = white_count / total_answers
        
        # Store simulation results in a dictionary and append to the list
        result_data = {
            'total_answers': total_answers,
            'top_side': top_side,
            'bottom_side': bottom_side,
            'correct_answers': correct_answers,
            'red_probability': red_probability,
            'white_probability': white_probability
        }
        answers.append(result_data)
    
    return answers

num_simulations = 10000

# Run the simulation
results = simulation(num_simulations)

# Print the results for each round of the simulation
for result in results:
    print(f"Round {result['total_answers']}:")
    print(f"Color on top side: {result['top_side']}")
    print(f"Color on bottom side: {result['bottom_side']}")
    print(f"Guessed correctly: {'Yes' if result['correct_answers'] else 'No'}")
    print(f"Probability for Red: {result['red_probability']:.2f}")
    print(f"Probability for White: {result['white_probability']:.2f}")
    print("-----------------------")

# Extract data for visualization
total_answers = [result['total_answers'] for result in results]
red_probabilities = [result['red_probability'] for result in results]
white_probabilities = [result['white_probability'] for result in results]

# Plot the probabilities of red and white colors over rounds
plt.plot(total_answers, red_probabilities, label='Red')
plt.plot(total_answers, white_probabilities, label='White')
plt.xlabel('Number of Rounds')
plt.ylabel('Probability')
plt.title('Probability of Colors over Rounds')
plt.legend()
plt.show()
