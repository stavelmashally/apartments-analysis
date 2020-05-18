import os
from csv import DictWriter


def to_csv(data):
    # Save data to csv file
    with open(f'apartments.csv', 'w') as file:
        headers = list(data[0].keys())
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        csv_writer.writerows(data)


def read_from_folder(folder_path):
    pass























def main():
    pass


if __name__ == "__main__":
    main()