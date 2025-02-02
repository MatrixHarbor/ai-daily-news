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
    return data # return data

# def check_collisions(satellites):
#

input_files = ["satellites1.txt","satellites2.txt"] # input 2 files
for input_file in input_files: # for each file, go through the function
    telemetry_data = read_telemetry(input_file) # go through read_telemetry function
    print(telemetry_data) # print 2 outcomes


# if __name__ == '__main__':
#     main()