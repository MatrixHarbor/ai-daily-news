from time import sleep
def process_data(data):
    modified_data = data + " that has been modified"
    sleep(3)
    return modified_data
def read_data_from_web():
    data = "Data from web"
    return data
def write_data_to_web(data):
    print(data)
    # return data

def main():
    data = read_data_from_web()
    modified_data = process_data(data)
    write_data_to_web(modified_data)

if __name__ == '__main__':
    main()