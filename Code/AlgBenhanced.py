############
############ ALTHOUGH I GIVE YOU THIS TEMPLATE PROGRAM WITH THE NAME 'skeleton.py', 
############ YOU CAN RENAME IT TO ANYTHING YOU LIKE. HOWEVER, FOR THE PURPOSES OF 
############ THE EXPLANATION IN THESE COMMENTS, I ASSUME THAT THIS PROGRAM IS STILL 
############ CALLED 'skeleton.py'.
############
############ IF YOU WISH TO IMPORT STANDARD MODULES, YOU CAN ADD THEM AFTER THOSE BELOW.
############ NOTE THAT YOU ARE NOT ALLOWED TO IMPORT ANY NON-STANDARD MODULES! TO SEE
############ THE STANDARD MODULES, TAKE A LOOK IN 'validate_before_handin.py'.
############

import os
import sys
import time
import random



############
############ NOW PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS.
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############ BY 'DO NOT TOUCH' I REALLY MEAN THIS. EVEN CHANGING THE SYNTAX, BY
############ ADDING SPACES OR COMMENTS OR LINE RETURNS AND SO ON, COULD MEAN THAT
############ CODES WILL NOT RUN WHEN I RUN THEM!
############


def read_file_into_string(input_file, ord_range):
    the_file = open(input_file, 'r') 
    current_char = the_file.read(1) 
    file_string = ""
    length = len(ord_range)
    while current_char != "":
        i = 0
        while i < length:
            if ord(current_char) >= ord_range[i][0] and ord(current_char) <= ord_range[i][1]:
                file_string = file_string + current_char
                i = length
            else:
                i = i + 1
        current_char = the_file.read(1)
    the_file.close()
    return file_string

def remove_all_spaces(the_string):
    length = len(the_string)
    new_string = ""
    for i in range(length):
        if the_string[i] != " ":
            new_string = new_string + the_string[i]
    return new_string

def integerize(the_string):
    length = len(the_string)
    stripped_string = "0"
    for i in range(0, length):
        if ord(the_string[i]) >= 48 and ord(the_string[i]) <= 57:
            stripped_string = stripped_string + the_string[i]
    resulting_int = int(stripped_string)
    return resulting_int

def convert_to_list_of_int(the_string):
    list_of_integers = []
    location = 0
    finished = False
    while finished == False:
        found_comma = the_string.find(',', location)
        if found_comma == -1:
            finished = True
        else:
            list_of_integers.append(integerize(the_string[location:found_comma]))
            location = found_comma + 1
            if the_string[location:location + 5] == "NOTE=":
                finished = True
    return list_of_integers

def build_distance_matrix(num_cities, distances, city_format):
    dist_matrix = []
    i = 0
    if city_format == "full":
        for j in range(num_cities):
            row = []
            for k in range(0, num_cities):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    elif city_format == "upper_tri":
        for j in range(0, num_cities):
            row = []
            for k in range(j):
                row.append(0)
            for k in range(num_cities - j):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    else:
        for j in range(0, num_cities):
            row = []
            for k in range(j + 1):
                row.append(0)
            for k in range(0, num_cities - (j + 1)):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    if city_format == "upper_tri" or city_format == "strict_upper_tri":
        for i in range(0, num_cities):
            for j in range(0, num_cities):
                if i > j:
                    dist_matrix[i][j] = dist_matrix[j][i]
    return dist_matrix

def read_in_algorithm_codes_and_tariffs(alg_codes_file):
    flag = "good"
    code_dictionary = {}   
    tariff_dictionary = {}  
    if not os.path.exists(alg_codes_file):
        flag = "not_exist"  
        return code_dictionary, tariff_dictionary, flag
    ord_range = [[32, 126]]
    file_string = read_file_into_string(alg_codes_file, ord_range)  
    location = 0
    EOF = False
    list_of_items = []  
    while EOF == False: 
        found_comma = file_string.find(",", location)
        if found_comma == -1:
            EOF = True
            sandwich = file_string[location:]
        else:
            sandwich = file_string[location:found_comma]
            location = found_comma + 1
        list_of_items.append(sandwich)
    third_length = int(len(list_of_items)/3)
    for i in range(third_length):
        code_dictionary[list_of_items[3 * i]] = list_of_items[3 * i + 1]
        tariff_dictionary[list_of_items[3 * i]] = int(list_of_items[3 * i + 2])
    return code_dictionary, tariff_dictionary, flag

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY!
############
############ THE RESERVED VARIABLE 'input_file' IS THE CITY FILE UNDER CONSIDERATION.
############
############ IT CAN BE SUPPLIED BY SETTING THE VARIABLE BELOW OR VIA A COMMAND-LINE
############ EXECUTION OF THE FORM 'python skeleton.py city_file.txt'. WHEN SUPPLYING
############ THE CITY FILE VIA A COMMAND-LINE EXECUTION, ANY ASSIGNMENT OF THE VARIABLE
############ 'input_file' IN THE LINE BELOW iS SUPPRESSED.
############
############ IT IS ASSUMED THAT THIS PROGRAM 'skeleton.py' SITS IN A FOLDER THE NAME OF
############ WHICH IS YOUR USER-NAME, E.G., 'abcd12', WHICH IN TURN SITS IN ANOTHER
############ FOLDER. IN THIS OTHER FOLDER IS THE FOLDER 'city-files' AND NO MATTER HOW
############ THE NAME OF THE CITY FILE IS SUPPLIED TO THIS PROGRAM, IT IS ASSUMED THAT 
############ THE CITY FILE IS IN THE FOLDER 'city-files'.
############

input_file = "AISearchfile012.txt"

############
############ PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS.
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############

if len(sys.argv) > 1:
    input_file = sys.argv[1]

##### begin change 1 #####
the_particular_city_file_folder = "city-files"
path_for_city_files = "../" + the_particular_city_file_folder
##### end change 1   #####
    
if os.path.isfile(path_for_city_files + "/" + input_file):
    ord_range = [[32, 126]]
    file_string = read_file_into_string(path_for_city_files + "/" + input_file, ord_range)
    file_string = remove_all_spaces(file_string)
    print("I have found and read the input file " + input_file + ":")
else:
    print("*** error: The city file " + input_file + " does not exist in the folder '" + the_particular_city_file_folder + "'.")
    sys.exit()

location = file_string.find("SIZE=")
if location == -1:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()
    
comma = file_string.find(",", location)
if comma == -1:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()
    
num_cities_as_string = file_string[location + 5:comma]
num_cities = integerize(num_cities_as_string)
print("   the number of cities is stored in 'num_cities' and is " + str(num_cities))

comma = comma + 1
stripped_file_string = file_string[comma:]
distances = convert_to_list_of_int(stripped_file_string)

counted_distances = len(distances)
if counted_distances == num_cities * num_cities:
    city_format = "full"
elif counted_distances == (num_cities * (num_cities + 1))/2:
    city_format = "upper_tri"
elif counted_distances == (num_cities * (num_cities - 1))/2:
    city_format = "strict_upper_tri"
else:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()

dist_matrix = build_distance_matrix(num_cities, distances, city_format)
print("   the distance matrix 'dist_matrix' has been built.")

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY!
############
############ YOU NOW HAVE THE NUMBER OF CITIES STORED IN THE INTEGER VARIABLE 'num_cities'
############ AND THE TWO_DIMENSIONAL MATRIX 'dist_matrix' HOLDS THE INTEGER CITY-TO-CITY 
############ DISTANCES SO THAT 'dist_matrix[i][j]' IS THE DISTANCE FROM CITY 'i' TO CITY 'j'.
############ BOTH 'num_cities' AND 'dist_matrix' ARE RESERVED VARIABLES AND SHOULD FEED
############ INTO YOUR IMPLEMENTATIONS.
############

############
############ THERE NOW FOLLOWS CODE THAT READS THE ALGORITHM CODES AND TARIFFS FROM
############ THE TEXT-FILE 'alg_codes_and_tariffs.txt' INTO THE RESERVED DICTIONARIES
############ 'code_dictionary' AND 'tariff_dictionary'. DO NOT AMEND THIS CODE!
############ THE TEXT FILE 'alg_codes_and_tariffs.txt' SHOULD BE IN THE SAME FOLDER AS
############ THE FOLDER 'city-files' AND THE FOLDER WHOSE NAME IS YOUR USER-NAME, E.G., 'abcd12'.
############

##### begin change 2 #####
the_particular_alg_codes_and_tariffs = "alg_codes_and_tariffs.txt"
path_for_alg_codes_and_tariffs = "../" + the_particular_alg_codes_and_tariffs
##### end change 2   #####

code_dictionary, tariff_dictionary, flag = read_in_algorithm_codes_and_tariffs(path_for_alg_codes_and_tariffs)

if flag != "good":
    print("*** error: The text file 'alg_codes_and_tariffs.txt' does not exist.")
    sys.exit()

print("The codes and tariffs have been read from 'alg_codes_and_tariffs.txt':")

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY! SORRY TO GO ON ABOUT THIS BUT YOU NEED TO BE 
############ AWARE OF THIS FACT!
############
############ YOU NOW NEED TO SUPPLY SOME PARAMETERS.
############
############ THE RESERVED STRING VARIABLE 'my_user_name' SHOULD BE SET AT YOUR
############ USER-NAME, E.G., "abcd12"
############

my_user_name = "rmvc61"

############
############ YOU CAN SUPPLY, IF YOU WANT, YOUR FULL NAME. THIS IS NOT USED AT ALL BUT SERVES AS
############ AN EXTRA CHECK THAT THIS FILE BELONGS TO YOU. IF YOU DO NOT WANT TO SUPPLY YOUR
############ NAME THEN EITHER SET THE STRING VARIABLES 'my_first_name' AND 'my_last_name' AT 
############ SOMETHING LIKE "Mickey" AND "Mouse" OR AS THE EMPTY STRING (AS THEY ARE NOW;
############ BUT PLEASE ENSURE THAT THE RESERVED VARIABLES 'my_first_name' AND 'my_last_name'
############ ARE SET AT SOMETHING).
############

my_first_name = "Owen"
my_last_name = "Shaw"

############
############ YOU NEED TO SUPPLY THE ALGORITHM CODE IN THE RESERVED STRING VARIABLE 'algorithm_code'
############ FOR THE ALGORITHM YOU ARE IMPLEMENTING. IT NEEDS TO BE A LEGAL CODE FROM THE TEXT-FILE
############ 'alg_codes_and_tariffs.txt' (READ THIS FILE TO SEE THE CODES).
############

algorithm_code = "AC"

############
############ DO NOT TOUCH OR ALTER THE CODE BELOW! YOU HAVE BEEN WARNED!
############

if not algorithm_code in code_dictionary:
    print("*** error: the algorithm code " + algorithm_code + " is illegal")
    sys.exit()
print("   your algorithm code is legal and is " + algorithm_code + " -" + code_dictionary[algorithm_code] + ".")

############
############ YOU CAN ADD A NOTE THAT WILL BE ADDED AT THE END OF THE RESULTING TOUR FILE IF YOU LIKE,
############ E.G., "in my basic greedy search, I broke ties by always visiting the first 
############ city found" BY USING THE RESERVED STRING VARIABLE 'added_note' OR LEAVE IT EMPTY
############ IF YOU WISH. THIS HAS NO EFFECT ON MARKS BUT HELPS YOU TO REMEMBER THINGS ABOUT
############ YOUR TOUR THAT YOU MIGHT BE INTERESTED IN LATER.
############

added_note = ""

############
############ NOW YOUR CODE SHOULD BEGIN.
############








def alg_b_enhanced(dist_matrix, max_iter, p, alpha, beta, mutation_rate, initial_temp, end_temp, cooling_rate, w=0):
    from AlgAbasic import alg_a
    import random
    import operator
    from copy import deepcopy
    import math

    from datetime import datetime

    start = datetime.now()
    time_taken = datetime.now() - start

    tour_alg_a, tour_length_alg_a = alg_a(dist_matrix)

    def standard_pheremone_deposit(ants, edge_matrix):
        # use an ant method to find pheremone deposit for each edge
        for ant in ants:
            # deposit 1/ant.path_cost on every edge that this ant touched
            for i in range(len(ant.path) - 1):
                current_vertex = ant.path[i]
                next_vertex = ant.path[i + 1]
                edge = edge_matrix[current_vertex][next_vertex]
                edge.pheremone_level += 1/ant.path_cost
    
    def rank_based_pheremone_deposit(ants, edge_matrix, w):
        # rank ants by path cost
        sorted_ants = sorted(ants, key=operator.attrgetter('path_cost'))
        # only retain top w ants
        top_w_ants = sorted_ants[:w]

        for rank, ant in enumerate(top_w_ants):
            # deposit 1/ant.path_cost on every edge that this ant touched
            for i in range(len(ant.path) - 1):
                current_vertex = ant.path[i]
                next_vertex = ant.path[i + 1]
                edge = edge_matrix[current_vertex][next_vertex]
                pheremone_deposit = (w-rank)*(1/ant.path_cost)
                edge.pheremone_level += pheremone_deposit
    
    
    # Enhancement: SA
    def simulated_annealing(ant, initial_temp, end_temp, cooling_rate):
        temp = initial_temp
        while temp > end_temp:
            trial_ant = Ant()
            trial_path, trial_path_cost = trial_ant.route(alpha, beta, edge_matrix)
            path_cost_difference = trial_path_cost - path_cost
            if path_cost_difference <= 0 or (math.exp(-path_cost_difference/temp) > random.random()):
                ant = trial_ant
            temp *= cooling_rate
        
        return ant

    #  Enhancement: Diversity
    def diversity(ants):
        sorted_ants = sorted(ants, key=operator.attrgetter('path_cost'))
        best_path_cost = sorted_ants[0].path_cost
        second_best_path_cost = sorted_ants[1].path_cost
        worst_path_cost = sorted_ants[-1].path_cost
        sorted_ants_without_best = sorted_ants[1:]
        average_path_cost = sum([ant.path_cost for ant in sorted_ants_without_best]) / len(sorted_ants_without_best)
        average_difference_from_best_path_cost = best_path_cost - average_path_cost


        if second_best_path_cost - worst_path_cost != 0:
            diversity = ((average_difference_from_best_path_cost - worst_path_cost)/(second_best_path_cost - worst_path_cost))**-1
        else: 
            diversity = 0
        return diversity
        

    # "Initialise tau 0 on each edge":
    n = len(dist_matrix)
    if w == 0:
        t_0 = n/tour_length_alg_a
    else:
        t_0 = 0.5*w*(w-1)/(p*tour_length_alg_a)

    # Define Edge classes and create instances of it within a new matrix which contains the length of each edge and its pheremone level
    class Edge:
        def __init__(self, length, t_0, destination):
            self.length = length
            self.pheremone_level = t_0
            self.probability = 0
            self.destination = destination
        
        def dissapate_pheremone_level(self, p):
            self.pheremone_level = (1-p)*self.pheremone_level
    
    # "Initialise best route"
    best = [tour_alg_a, tour_length_alg_a]

    # "Place ants on verticies"
    class Ant:
        def __init__(self):
            self.starting_position = random.randint(0, len(dist_matrix) - 1)
            self.current_position = self.starting_position
            self.path = [self.starting_position]
            self.path_cost = 0
            self.mutated = "normal"

        # Enhancement: Mutation
        def mutation(self, mutation_rate):
            if random.uniform(0, 1) < mutation_rate:
                self.mutated = "mutated"

        def route(self, alpha, beta, edge_matrix):
            def probability(alpha, beta, vertex):
                # Edges should be found by edge_matrix[vertex]
                possible_edges = edge_matrix[vertex]
                edge_numerators = []
                sum_of_edge_numerators = 0
                possible_verticies = [x for x in range(len(edge_matrix[vertex]))]

                # Needs to find sum product of tau and heuristic desirability to the power of alpha and beta of each edge, store in list and also return variable of sum of that list/sum of products
                # Set probability as 0 if itself or ant has been there before
                if len(self.path) == len(possible_edges) - 1:
                    for i in range(len(possible_edges)):
                        if i not in self.path:
                            next_vertex = i
                else:
                    # calculate probabilities for potential next vertex
                    for edge in possible_edges:
                        if edge.length != 0 and edge.destination not in self.path:
                            numerator = (edge.pheremone_level**alpha)*((1/edge.length)**beta)
                        else:
                            numerator = 0
                        edge_numerators.append(numerator)
                        sum_of_edge_numerators += numerator                    

                    # Use probabilities to find next vertex and gen cost = distance between current vertex and next vertex
                    if self.mutated == "normal":
                        next_vertex = random.choices(possible_verticies, edge_numerators, k = 1)[0]
                    elif self.mutated == "mutated":
                        next_vertex = random.choice(possible_verticies)
                cost = edge_matrix[self.current_position][next_vertex].length


                return next_vertex, cost
            
            # reset ant to starting position and clear path from last time
            if self.mutated == "normal":
                self.current_position = self.starting_position
                self.path = [self.starting_position]
                self.path_cost = 0
            elif self.mutated == "mutated":
                self.mutated == "normal"

            # run probability function and move to chosen vertex and repeat until gone to all verticies
            while len(self.path) < len(edge_matrix):
                self.current_position, cost = probability(alpha, beta, self.current_position)
                self.path.append(self.current_position)
                self.path_cost += cost
            self.path_cost += edge_matrix[self.current_position][self.starting_position].length
            
            return self.path, self.path_cost
    
    edge_matrix = deepcopy(dist_matrix)

    for row in range(len(edge_matrix)):
        for column in range(len(edge_matrix[row])):
            edge = Edge(edge_matrix[row][column], t_0, column)
            edge_matrix[row][column] = edge
    

    # Create n ants and store them in a list
    ants = list()
    for i in range(n):
        ants.append(Ant())

    # Cycle of ants going around routes and then changing pheremone levels on each edge
    t = 0
    while t < max_iter and time_taken.total_seconds() < 50:
        time_taken = datetime.now() - start
        for ant in ants:
            # build ant route
            path, path_cost = ant.route(alpha, beta, edge_matrix)
            # if route is better than "best" route, replace best route with new route
            if path_cost < best[1]:
                best = [path, path_cost]
        
        # Dissapate pheremone levels
        for vertex in edge_matrix:
            for edge in vertex:
                edge.dissapate_pheremone_level(p)

        if w == 0:
            standard_pheremone_deposit(ants, edge_matrix)
        else:           
            rank_based_pheremone_deposit(ants, edge_matrix, w)
        
        # Enhancement:
        # Calculate diversity of ants path cost
        ants_diversity = diversity(ants)
        
        ant = random.choice(ants)
        # If diversity > 0.5, Simulated Annealing to bring it down
        if ants_diversity > 0.5:
            ant = simulated_annealing(ant, initial_temp, end_temp, cooling_rate)
            # print("SA")
        # If diversity < 0.5, Mutation to bring it up
        # One ant which is randomly chosen has probability of being mutated, according to mutation rate
        elif ants_diversity < 0.5:
            ant.mutation(mutation_rate)      

        t += 1

    return best

tour, tour_length = alg_b_enhanced(dist_matrix, 300, 0.1, 1, 5, 0.5, 10^50, 0.1, 0.99, 6)











############
############ YOUR CODE SHOULD NOW BE COMPLETE AND WHEN EXECUTION OF THIS PROGRAM 'skeleton.py'
############ REACHES THIS POINT, YOU SHOULD HAVE COMPUTED A TOUR IN THE RESERVED LIST VARIABLE 'tour', 
############ WHICH HOLDS A LIST OF THE INTEGERS FROM {0, 1, ..., 'num_cities' - 1} SO THAT EVERY INTEGER
############ APPEARS EXACTLY ONCE, AND YOU SHOULD ALSO HOLD THE LENGTH OF THIS TOUR IN THE RESERVED
############ INTEGER VARIABLE 'tour_length'.
############

############
############ YOUR TOUR WILL BE PACKAGED IN A TOUR FILE OF THE APPROPRIATE FORMAT AND THIS TOUR FILE'S,
############ NAME WILL BE A MIX OF THE NAME OF THE CITY FILE, THE NAME OF THIS PROGRAM AND THE
############ CURRENT DATA AND TIME. SO, EVERY SUCCESSFUL EXECUTION GIVES A TOUR FILE WITH A UNIQUE
############ NAME AND YOU CAN RENAME THE ONES YOU WANT TO KEEP LATER.
############

############
############ DO NOT TOUCH OR ALTER THE CODE BELOW THIS POINT! YOU HAVE BEEN WARNED!
############

flag = "good"
length = len(tour)
for i in range(0, length):
    if isinstance(tour[i], int) == False:
        flag = "bad"
    else:
        tour[i] = int(tour[i])
if flag == "bad":
    print("*** error: Your tour contains non-integer values.")
    sys.exit()
if isinstance(tour_length, int) == False:
    print("*** error: The tour-length is a non-integer value.")
    sys.exit()
tour_length = int(tour_length)
if len(tour) != num_cities:
    print("*** error: The tour does not consist of " + str(num_cities) + " cities as there are, in fact, " + str(len(tour)) + ".")
    sys.exit()
flag = "good"
for i in range(0, num_cities):
    if not i in tour:
        flag = "bad"
if flag == "bad":
    print("*** error: Your tour has illegal or repeated city names.")
    sys.exit()
check_tour_length = 0
for i in range(0, num_cities - 1):
    check_tour_length = check_tour_length + dist_matrix[tour[i]][tour[i + 1]]
check_tour_length = check_tour_length + dist_matrix[tour[num_cities - 1]][tour[0]]
if tour_length != check_tour_length:
    flag = print("*** error: The length of your tour is not " + str(tour_length) + "; it is actually " + str(check_tour_length) + ".")
    sys.exit()
print("You, user " + my_user_name + ", have successfully built a tour of length " + str(tour_length) + "!")

local_time = time.asctime(time.localtime(time.time()))
output_file_time = local_time[4:7] + local_time[8:10] + local_time[11:13] + local_time[14:16] + local_time[17:19]
output_file_time = output_file_time.replace(" ", "0")
script_name = os.path.basename(sys.argv[0])
if len(sys.argv) > 2:
    output_file_time = sys.argv[2]
output_file_name = script_name[0:len(script_name) - 3] + "_" + input_file[0:len(input_file) - 4] + "_" + output_file_time + ".txt"

f = open(output_file_name,'w')
f.write("USER = " + my_user_name + " (" + my_first_name + " " + my_last_name + "),\n")
f.write("ALGORITHM CODE = " + algorithm_code + ", NAME OF CITY-FILE = " + input_file + ",\n")
f.write("SIZE = " + str(num_cities) + ", TOUR LENGTH = " + str(tour_length) + ",\n")
f.write(str(tour[0]))
for i in range(1,num_cities):
    f.write("," + str(tour[i]))
f.write(",\nNOTE = " + added_note)
f.close()
print("I have successfully written your tour to the tour file:\n   " + output_file_name + ".")
    
    











    





# dist_matrix = [[0, 12, 21, 4, 17, 13, 8, 35, 8, 7, 11, 14], [12, 0, 7, 9, 50, 31, 30, 12, 40, 20, 5, 21], [21, 7, 0, 15, 31, 14, 40, 5, 32, 30, 13, 9], [4, 9, 15, 0, 8, 9, 6, 30, 3, 10, 9, 15], [17, 50, 31, 8, 0, 4, 2, 30, 5, 40, 27, 15], [13, 31, 14, 9, 4, 0, 7, 10, 10, 34, 35, 4], [8, 30, 40, 6, 2, 7, 0, 53, 3, 20, 29, 15], [35, 12, 5, 30, 30, 10, 53, 0, 32, 50, 20, 6], [8, 40, 32, 3, 5, 10, 3, 32, 0, 25, 21, 16], [7, 20, 30, 10, 40, 34, 20, 50, 25, 0, 6, 32], [11, 5, 13, 9, 27, 35, 29, 20, 21, 6, 0, 25], [14, 21, 9, 15, 15, 4, 15, 6, 16, 32, 25, 0]] 

# alg_b_basic(dist_matrix, 100, 0.5)

    
    


    
