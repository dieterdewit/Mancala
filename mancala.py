import random as r
import copy

player_1 = [4, 4, 4, 4, 4, 4]
intelligence = [4, 4, 4, 4, 4, 4]
row_1 = 0
row_2 = 0
total = player_1 + [row_1] + intelligence + [row_2]
simulated_games = 10000


def monte_carlo_ia(player, mc_intelligence, actual_total):
    simulation_results = [0, 0, 0, 0, 0, 0]
    for simulated_game in range(0, simulated_games):
        decision = 0
        check_position = 0
        new_position = r.choices([1, 2, 3, 4, 5, 6])
        human = copy.deepcopy(player)
        artificial_intelligence = copy.deepcopy(mc_intelligence)
        game_total = copy.deepcopy(actual_total)
        game_counter = True
        human_loop_finished = False
        ia_loop_finished = False

        while game_counter:
            # Artificial Intelligence Block Code
            while not ia_loop_finished:
                intelligence_moves = [(a + 1) for a, b in enumerate(artificial_intelligence) if b == 0]
                intelligence_decision = 0
                conditional = 0
                while conditional == 0:
                    if decision == 0:
                        intelligence_decision = new_position[0]
                        decision = 1
                    else:
                        intelligence_decision = r.randint(1, 6)

                    if intelligence_decision not in intelligence_moves:
                        conditional = 1

                game_positions = game_total[7 + intelligence_decision - 1]
                game_total[7 + intelligence_decision - 1] = 0
                game_copy = copy.deepcopy(game_total)

                for game_position in range(0, game_positions):
                    if (7 + intelligence_decision + game_position) > 13:
                        intelligence_decision = -game_position - 7
                    game_total[7 + intelligence_decision + game_position] += 1
                    check_position = 7 + intelligence_decision + game_position

                if (7 <= check_position <= 12) and (game_copy[check_position] == 0) and (
                        game_total[check_position] != 0) and (game_total[12 - check_position] != 0):
                    game_total[13] += game_total[check_position] + game_total[12 - check_position]
                    game_total[check_position] = 0
                    game_total[12 - check_position] = 0

                human = game_total[0:6]
                artificial_intelligence = game_total[7:13]
                human_game = game_total[6]
                intelligence_game = game_total[13]

                if sum(human) == 0 or sum(artificial_intelligence) == 0:
                    if intelligence_game > human_game:
                        simulation_results[new_position[0] - 1] += 1
                        game_counter = False
                        human_loop_finished = True
                        ia_loop_finished = True
                    else:
                        game_counter = False
                        human_loop_finished = True
                        ia_loop_finished = True

                if check_position != 13:
                    break

            # Human Block Code
            while not human_loop_finished:
                human_moves = [(a + 1) for a, b in enumerate(human) if b == 0]
                human_decision = 0
                conditional_human = 0

                while conditional_human == 0:
                    human_decision = r.randint(1, 6)
                    if human_decision not in human_moves:
                        conditional_human = 1

                game_positions = game_total[human_decision - 1]
                game_total[human_decision - 1] = 0
                game_copy = copy.deepcopy(game_total)

                for game_position in range(0, game_positions):
                    if (human_decision + game_position) > 12:
                        human_decision = -game_position
                    game_total[human_decision + game_position] += 1
                    check_position = human_decision + game_position

                if (0 <= check_position <= 5) and (game_copy[check_position] == 0) and (
                        game_total[check_position] != 0) and (game_total[12 - check_position] != 0):
                    game_total[6] += game_total[check_position] + game_total[12 - check_position]
                    game_total[check_position] = 0
                    game_total[12 - check_position] = 0

                human = game_total[0:6]
                artificial_intelligence = game_total[7:13]
                human_game = game_total[6]
                intelligence_game = game_total[13]

                if sum(human) == 0 or sum(artificial_intelligence) == 0:
                    if intelligence_game > human_game:
                        simulation_results[new_position[0] - 1] += 1
                        game_counter = False
                        human_loop_finished = True
                        ia_loop_finished = True
                    else:
                        game_counter = False
                        human_loop_finished = True
                        ia_loop_finished = True

                if check_position != 6:
                    break

    for x in range(0, len(simulation_results)):
        simulation_results[x] = simulation_results[x] / simulated_games

    return simulation_results.index(max(simulation_results)) + 1


def game_state():
    print("Select a position from 1 to 6")
    print("----------------------------------")
    print("PLayer Monte Carlo        Player 1 ")
    print("_" + " | " + ' | '.join('{}'.format(k) for k in intelligence[::-1]) + " |" + "_")
    print("{0}".format(row_2, row_1) + " | " + "                     " + " | " + "{1}".format(row_2, row_1))
    print("_ |                       | _")
    print(" " + " | " + ' | '.join('{}'.format(k) for k in player_1) + " |" + " ")


def determine_winner(top_row, down_row):
    if top_row > down_row:
        print("Player 1 WINS!")
    elif row_2 > row_1:
        print("MONTE CARLO Artificial Intelligence WON!")
    else:
        print("... tie")


def select_position(p):
    selection = 0
    while (selection <= 0) or (selection > 6):
        try:
            selection = int(input("Player {0}, select a position from 1 to 6: ".format(p)))
        except ValueError:
            print("Try again...")
            pass
    return selection


game_state()
game_counter_final = True
first_loop_end = False
final_loop_end = False
check_final_position = 0

while game_counter_final:
    # Human Block Code
    while not first_loop_end:
        human_final_moves = [(a + 1) for a, b in enumerate(player_1) if b == 0]
        print(human_final_moves)
        human_secondary_decision = 0
        conditional_human_final = 0

        while conditional_human_final == 0:
            print("----------------------------- Player 1 TURN ---------------------------")
            human_secondary_decision = select_position(1)
            if human_secondary_decision not in human_final_moves:
                conditional_human_final = 1

        game_final_positions = total[human_secondary_decision - 1]
        total[human_secondary_decision - 1] = 0
        game_copy_final = copy.deepcopy(total[:])

        for i in range(0, game_final_positions):
            if (human_secondary_decision + i) > 12:
                human_secondary_decision = -i
            total[human_secondary_decision + i] += 1
            check_final_position = human_secondary_decision + i

        if (0 <= check_final_position <= 5) and (game_copy_final[check_final_position] == 0) and (
                total[check_final_position] != 0) and (total[12 - check_final_position] != 0):
            total[6] += total[check_final_position] + total[12 - check_final_position]
            total[check_final_position] = 0
            total[12 - check_final_position] = 0

        player_1 = total[0:6]
        intelligence = total[7:13]
        row_1 = total[6]
        row_2 = total[13]
        game_state()

        if sum(player_1) == 0 or sum(intelligence) == 0:
            determine_winner(row_1, row_2)
            game_counter_final = False
            first_loop_end = True
            final_loop_end = True

        if check_final_position != 6:
            break

    # Artificial Intelligence Block Code
    while not final_loop_end:
        intelligence_secondary_moves = [(a + 1) for a, b in enumerate(intelligence) if b == 0]
        intelligence_secondary_decision = 0
        cond_b = 0
        while cond_b == 0:
            print("-------------------------- Monte Carlo Artificail Intelligence TURN ----------------------")
            intelligence_secondary_decision = monte_carlo_ia(player_1, intelligence, total)
            if intelligence_secondary_decision not in intelligence_secondary_moves:
                print("I, Monte Carlo, choose intelligently the following position: " + str(
                    intelligence_secondary_decision))
                cond_b = 1

        game_final_positions = total[7 + intelligence_secondary_decision - 1]
        total[7 + intelligence_secondary_decision - 1] = 0
        game_copy_final = total[:]

        for i in range(0, game_final_positions):
            if (7 + intelligence_secondary_decision + i) > 13:
                intelligence_secondary_decision = -i - 7
            total[7 + intelligence_secondary_decision + i] += 1
            check_final_position = 7 + intelligence_secondary_decision + i

        if (7 <= check_final_position <= 12) and (game_copy_final[check_final_position] == 0) and (
                total[check_final_position] != 0) and (total[12 - check_final_position] != 0):
            total[13] += total[check_final_position] + total[12 - check_final_position]
            total[check_final_position] = 0
            total[12 - check_final_position] = 0

        player_1 = total[0:6]
        intelligence = total[7:13]
        row_1 = total[6]
        row_2 = total[13]
        game_state()

        if sum(player_1) == 0 or sum(intelligence) == 0:
            determine_winner(row_1, row_2)
            game_counter_final = False
            first_loop_end = True
            final_loop_end = True

        if check_final_position != 13:
            break

key = input('Press ENTER to Exit')
