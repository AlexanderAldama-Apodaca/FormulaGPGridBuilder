import random

print("FormulaGP Grid Builder\n")

# Historical Formula One data (seasons, teams, and drivers) with speed ratings
f1_database = {
    "2021": {
        "Alfa Romeo": {"drivers": ["Kimi Raikkonen", "Antonio Giovinazzi"], "speed": "slow"},
        "AlphaTauri": {"drivers": ["Pierre Gasly", "Yuki Tsunoda"], "speed": "medium"},
        "Alpine": {"drivers": ["Fernando Alonso", "Esteban Ocon"], "speed": "fast"},
        "Aston Martin": {"drivers": ["Sebastian Vettel", "Lance Stroll"], "speed": "medium"},
        "Ferrari": {"drivers": ["Charles Leclerc", "Carlos Sainz Jr."], "speed": "fast"},
        "Haas": {"drivers": ["Nikita Mazepin", "Mick Schumacher"], "speed": "slow"},
        "McLaren": {"drivers": ["Daniel Ricciardo", "Lando Norris"], "speed": "fast"},
        "Mercedes": {"drivers": ["Lewis Hamilton", "Valtteri Bottas"], "speed": "very fast"},
        "Red Bull": {"drivers": ["Sergio Perez", "Max Verstappen"], "speed": "very fast"},
        "Williams": {"drivers": ["Nicholas Latifi", "George Russell"], "speed": "slow"}
    },
    "2022": {
        "Alfa Romeo": {"drivers": ["Zhou Guanyu", "Valtteri Bottas"], "speed": "medium"},
        "AlphaTauri": {"drivers": ["Pierre Gasly", "Yuki Tsunoda"], "speed": "slow"},
        "Alpine": {"drivers": ["Fernando Alonso", "Esteban Ocon"], "speed": "fast"},
        "Aston Martin": {"drivers": ["Sebastian Vettel", "Lance Stroll"], "speed": "medium"},
        "Ferrari": {"drivers": ["Charles Leclerc", "Carlos Sainz Jr."], "speed": "very fast"},
        "Haas": {"drivers": ["Kevin Magnussen", "Mick Schumacher"], "speed": "slow"},
        "McLaren": {"drivers": ["Daniel Ricciardo", "Lando Norris"], "speed": "fast"},
        "Mercedes": {"drivers": ["Lewis Hamilton", "George Russell"], "speed": "very fast"},
        "Red Bull": {"drivers": ["Max Verstappen", "Sergio Perez"], "speed": "very fast"},
        "Williams": {"drivers": ["Nicholas Latifi", "Alexander Albon"], "speed": "very fast"}
    },
    "2023": {
        "Alfa Romeo": {"drivers": ["Zhou Guanyu", "Valtteri Bottas"], "speed": "slow"},
        "AlphaTauri": {"drivers": ["Nyck de Vries", "Yuki Tsunoda"], "speed": "slow"},
        "Alpine": {"drivers": ["Pierre Gasly", "Esteban Ocon"], "speed": "medium"},
        "Aston Martin": {"drivers": ["Fernando Alonso", "Lance Stroll"], "speed": "fast"},
        "Ferrari": {"drivers": ["Charles Leclerc", "Carlos Sainz Jr."], "speed": "fast"},
        "Haas": {"drivers": ["Kevin Magnussen", "Nico Hulkenberg"], "speed": "slow"},
        "McLaren": {"drivers": ["Lando Norris", "Oscar Piastri"], "speed": "fast"},
        "Mercedes": {"drivers": ["Lewis Hamilton", "George Russell"], "speed": "fast"},
        "Red Bull": {"drivers": ["Max Verstappen", "Sergio Perez"], "speed": "very fast"},
        "Williams": {"drivers": ["Logan Sargeant", "Alexander Albon"], "speed": "slow"}
    },
    "2024": {
        "Alpine": {"drivers": ["Pierre Gasly", "Esteban Ocon"], "speed": "medium"},
        "Aston Martin": {"drivers": ["Fernando Alonso", "Lance Stroll"], "speed": "medium"},
        "Ferrari": {"drivers": ["Charles Leclerc", "Carlos Sainz Jr."], "speed": "very fast"},
        "Haas": {"drivers": ["Kevin Magnussen", "Nico Hulkenberg"], "speed": "medium"},
        "Kick Sauber": {"drivers": ["Zhou Guanyu", "Valtteri Bottas"], "speed": "slow"},
        "McLaren": {"drivers": ["Lando Norris", "Oscar Piastri"], "speed": "very fast"},
        "Mercedes": {"drivers": ["Lewis Hamilton", "George Russell"], "speed": "very fast"},
        "Racing Bulls": {"drivers": ["Daniel Ricciardo", "Yuki Tsunoda"], "speed": "medium"},
        "Red Bull": {"drivers": ["Max Verstappen", "Sergio Perez"], "speed": "very fast"},
        "Williams": {"drivers": ["Logan Sargeant", "Alexander Albon"], "speed": "slow"}
    },
    "2025": {
        "Alpine": {"drivers": ["Jack Doohan", "Pierre Gasly"], "speed": "slow"},
        "Aston Martin": {"drivers": ["Fernando Alonso", "Lance Stroll"], "speed": "medium"},
        "Ferrari": {"drivers": ["Charles Leclerc", "Lewis Hamilton"], "speed": "fast"},
        "Haas": {"drivers": ["Esteban Ocon", "Oliver Bearman"], "speed": "slow"},
        "Kick Sauber": {"drivers": ["Gabriel Bortoleto", "Nico Hulkenberg"], "speed": "slow"},
        "McLaren": {"drivers": ["Lando Norris", "Oscar Piastri"], "speed": "very fast"},
        "Mercedes": {"drivers": ["Kimi Antonelli", "George Russell"], "speed": "very fast"},
        "Racing Bulls": {"drivers": ["Isack Hadjar", "Yuki Tsunoda"], "speed": "medium"},
        "Red Bull": {"drivers": ["Max Verstappen", "Liam Lawson"], "speed": "very fast"},
        "Williams": {"drivers": ["Alexander Albon", "Carlos Sainz Jr."], "speed": "fast"}
    },
    "2026": {
        "Alpine": {"drivers": ["Pierre Gasly", "Franco Colapinto"], "speed": "medium"},
        "Aston Martin": {"drivers": ["Fernando Alonso", "Lance Stroll"], "speed": "slow"},
        "Audi": {"drivers": ["Gabriel Bortoleto", "Nico Hulkenberg"], "speed": "slow"},
        "Cadillac": {"drivers": ["Sergio Perez", "Valtteri Bottas"], "speed": "slow"},
        "Ferrari": {"drivers": ["Charles Leclerc", "Lewis Hamilton"], "speed": "fast"},
        "Haas": {"drivers": ["Esteban Ocon", "Oliver Bearman"], "speed": "medium"},
        "McLaren": {"drivers": ["Lando Norris", "Oscar Piastri"], "speed": "fast"},
        "Mercedes": {"drivers": ["Kimi Antonelli", "George Russell"], "speed": "fast"},
        "Racing Bulls": {"drivers": ["Liam Lawson", "Arvid Lindblad"], "speed": "medium"},
        "Red Bull": {"drivers": ["Max Verstappen", "Isack Hadjar"], "speed": "medium"},
        "Williams": {"drivers": ["Alexander Albon", "Carlos Sainz Jr."], "speed": "slow"}
    }
}

# Map classifications to numerical selection probabilities (weights)
SPEED_WEIGHTS = {
    "very fast": 40,
    "fast": 30,
    "medium": 20,
    "slow": 10
}

GRID_LIMIT = 6
active_grid = []
chosen_teams = set() # Tracks teams already taken

# Determine players and bots
player_count = int(input(f"Enter number of human players (1-{GRID_LIMIT}): "))
bot_count = GRID_LIMIT - player_count
print(f"Setting up game with {player_count} players and {bot_count} bots.\n")

# Choose Formula One season
selected_season = input("Enter F1 Season (2021-2026): ")
all_teams = f1_database[selected_season]

# Collect player selections
for i in range(1, player_count + 1):
    print(f"\nPlayer {i} Setup")

    # Filter out teams that have already been chosen
    available_teams = [team for team in all_teams.keys() if team not in chosen_teams]
    print("Available teams:", ", ".join(available_teams))

    # Loop until the player inputs a valid, unchosen team
    while True:
        team = input(f"Player {i}, pick a team: ")
        if team in available_teams:
            break
        print(f"Invalid choice. Please pick an available team from the list.")

    # Track the chosen team so it cannot be chosen again
    chosen_teams.add(team)

    drivers_list = all_teams[team]["drivers"]
    print("Available drivers:", ", ".join(drivers_list))
    driver = input(f"Player {i}, pick a driver: ")

    active_grid.append({
        "type": "Human",
        "team": team,
        "driver": driver
    })

# Automatically fill the remaining grid with weighted bots
for b in range (1, bot_count + 1):
    # Dynamically filter available teams for this specific bot pick
    remaining_teams = [team for team in all_teams.keys() if team not in chosen_teams]

    # Generate matching weights based on the speed classification
    current_weights = [SPEED_WEIGHTS[all_teams[team]["speed"]] for team in remaining_teams]

    # Weighted random selection of exactly one team
    bot_team = random.choices(remaining_teams, weights=current_weights, k=1)[0]
    chosen_teams.add(bot_team)

    # Pick a random driver from that team
    bot_driver = random.choice(all_teams[bot_team]["drivers"])

    active_grid.append({
        "type": "Bot",
        "team": bot_team,
        "driver": bot_driver
    })

# Display final starting grid
print("\nFormulaGP Grid")
for position, car in enumerate(active_grid, 1):
    print(f"P{position}: {car['driver']} ({car['team']}) - [{car['type']}]")
