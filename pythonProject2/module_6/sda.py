import itertools
def read_telemetry(file_name):
    data = [] # initialize a list to store the data
    with open(file_name, 'r') as file: # open the file
        num_satellites = int(file.readline().strip())

        for line in range(num_satellites): # read each line in the file
            line = file.readline().strip()
            country,altitude,velocity = line.split(',')
            satellite_data = {'country':country,'altitude':int(altitude),'velocity':float(velocity)}
            data.append(satellite_data) # store data in the list

            # data.append(line.strip()) # store data in the list
    return data

# define the collision rule
def check_for_collision(sat1,sat2):
    if sat1['altitude'] == sat2['altitude']: # same altitude
        if sat1['velocity'] * sat2['velocity'] < 0: # opposite directions
            return True
        if sat1['velocity'] != sat2['velocity']: # same direction, different speeds
            return True
    return False # if none of the conditions are met, no collision


def check_collisions(satellites):
    collision_results = {}
    # use itertools.combinations to check each pair of satellites
    for sat1,sat2 in itertools.combinations(satellites,2):
        if check_for_collision(sat1,sat2):  # check collision before appending
            if sat1['country'] not in collision_results:
                collision_results[sat1['country']] = []
            collision_results[sat1['country']].append(sat2['country'])
            if sat2['country'] not in collision_results:
                collision_results[sat2['country']] = []
            collision_results[sat2['country']].append(sat1['country'])
    return collision_results


def print_output(simulation_number, satellites, collision_results,out_file=None):
    header = f"\n##### Space Command Simulation {simulation_number} #####"
    print(header)
    if out_file:
        with open(out_file,'w') as f:
            f.write(header + '\n')

    for satellite in satellites:
        if isinstance(satellite, dict): # ensure satellite is a dictionary
            country = satellite['country']
            if country in collision_results and collision_results[country]:
                alert = f"{country} is at risk of colliding with {collision_results[country]}"
            else:
                alert = f"{country} is not at risk for a collision."
            print(alert)
            if out_file:
                with open(out_file,'a') as f:
                    f.write(alert + '\n')

def main():
    satellites1 = read_telemetry('satellites1.txt')
    satellites2 = read_telemetry('satellites2.txt')

    # simulation 1
    collision_results1 = check_collisions(satellites1)
    print_output(1, satellites1, collision_results1, 'satellites1_alerts.txt')

    # simulation 2
    collision_results2 = check_collisions(satellites2)
    print_output(2, satellites2, collision_results2, 'satellites2_alerts.txt')

if __name__ == '__main__':
    main()