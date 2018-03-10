import csv
# import pandas as pd

# csv_input = pd.read_csv('attendees_v2.csv')
# csv_input['Email'] = csv_input['First Name'] + '@gmail.com'
# csv_input.to_csv('attendees_with_email_v2.csv', index = False)

attendees1 = []
attendees2 = []

def generate_set(file_name, input_list):
    f = open(file_name)

    csv_f = csv.reader(f)

    for attendee in csv_f:
        input_list.append(attendee[2])

    f.close()

    return set(input_list)

attendees1_set = generate_set('attendees_with_email_v1.csv', attendees1)
attendees2_set = generate_set('attendees_with_email_v2.csv', attendees2)

print(attendees2_set.difference(attendees1_set))
print(attendees1_set.difference(attendees2_set))