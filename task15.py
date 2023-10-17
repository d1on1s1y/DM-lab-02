data_tuple = [
    ["Іванов Іван Іванович", "10-01-1980"],
    ["Петров Петро Петрович", "15-03-1995"],
    ["Сидоров Андрій Олександрович", "05-07-1989"],
    ["Миколаєнко Олена Павлівна", "20-11-1985"],
    ["Захарченко Марія Ігорівна", "30-09-1990"],
    ["Григоренко Василь Володимирович", "18-04-1976"]
]


def sort_by_birthdate(data):
    sorted_data = sorted(data, key=lambda x: int(x[1].split('-')[2])) 
    return sorted_data


sorted_data = sort_by_birthdate(data_tuple)
for item in sorted_data:
    print(item)
