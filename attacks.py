import json
import random

# Load JSON data
with open('attacks.json', 'r') as file:
    attacks_data = json.load(file)

# Prompt the user for a group name
group_name = input("Enter the group name: ")

# Find attacks by the group
group_attacks = [attack for attack in attacks_data if attack['group'] == group_name]

# Check if the group is found
if not group_attacks:
    print(":(")  # ASCII frowning face
else:
    # Sort attacks by phase and select one attack per phase randomly
    phases = sorted(set(attack['phase'] for attack in group_attacks))
    attack_chain = []
    for phase in phases:
        phase_attacks = [attack for attack in group_attacks if attack['phase'] == phase]
        attack_chain.append(random.choice(phase_attacks))

    # Display the attack chain
    for attack in attack_chain:
        print(f"Phase: {attack['phase']}")
        print(f"Attack: {attack['attack']}")
        data_sources = attack['data_sources']
        if isinstance(data_sources, list):
            print("Data Sources:")
            for source in data_sources:
                print(f"- {source}")
        else:
            print(f"Data Source: {data_sources}")
        print()  # Newline for separation between attacks