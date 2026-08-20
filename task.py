import re

print("Learning progress tracker")

adding_student_mode = False
adding_points_mode = False
find_mode = False
statistic_mode = False

student_count = 0
student_count_session = 0

student_id = 10000
student_id_number = 0
python_score = 0
dsa_score = 0
database_score = 0
flask_score = 0

enrolled_python = 0
enrolled_dsa = 0
enrolled_database = 0
enrolled_flask = 0

python_count = 0
dsa_count = 0
database_count = 0
flask_count = 0

max_python = 600
max_dsa = 400
max_database = 480
max_flask = 550

logbook = {}
student_dict = {}
notified_dict_python = []
notified_dict_dsa = []
notified_dict_databases = []
notified_dict_flask = []

def check_length(split_input):
    if len(split_input) < 3:
        print('Incorrect credentials')
        return False
    else:
        return True

def check_first_name(split_input):
    first_name = split_input[0]
    if re.fullmatch(r"(?=.{2,})[a-zA-Z]+(?:['-][a-zA-Z]+)*", first_name):
        return True
    else:
        print('Incorrect first name.')
        return False

def check_last_name(split_input):
    for x in range(1, len(split_input) - 1):
        last_name = split_input[x]
        if re.fullmatch(r"(?=.{2,})[a-zA-Z]+(?:['-][a-zA-Z]+)*", last_name):
            return True
        else:
            print('Incorrect last name.')
            return False

    return True

def check_email(split_input):
    email = split_input[-1]

    if re.fullmatch(r"[a-zA-Z0-9.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+", email):
        if duplicate_email(email) and len(student_dict) > 0:
            print('This email is already taken')
            return False

        return True

    else:
        print('Incorrect email.')
        return False

def check_all(student_input):
    global adding_student_mode, student_count, student_count_session, student_id

    if student_input == 'back':
        print(f'Total {student_count_session} students have been added.')
        student_count_session = 0
        adding_student_mode = False
        return

    split = student_input.split(' ')
    length_check = check_length(split)
    if not length_check:
        return

    first_name_check = check_first_name(split)
    last_name_check = check_last_name(split)
    email_check = check_email(split)

    if not first_name_check or not last_name_check or not email_check:
        return

    print('The student has been added.')

    first_name, *last_name, email = split

    student_dict[student_id] = [first_name, *last_name, email, 0, 0, 0, 0]
    logbook[student_id] = []
    print(student_dict[student_id][2])
    student_id += 1
    student_count += 1
    student_count_session += 1

def duplicate_email(email):
    for value in student_dict.values():
        if value[2] == email:
            return True
        else:
            continue
    return False

def add_points(points_input):
    global adding_points_mode, student_id_number, python_score, dsa_score, database_score, flask_score, python_count, dsa_count, database_count, flask_count

    if points_input == 'back':
        adding_points_mode = False
        return

    split = points_input.split(' ')

    if len(split) == 5:

        if not re.fullmatch(r"[0-9]+", split[0]):
            print(f'No student id is found for id={split[0]}')
            return

        student_id_number = int(split[0])

        if not student_id_number in student_dict.keys():
            print(f'No student id is found for id={student_id_number}')
            return

        for s in split:
            if not re.fullmatch(r"[0-9]+", s):
                print('Incorrect points format.')
                return

        if student_id_number < 0 or python_score < 0 or dsa_score < 0 or database_score < 0 or flask_score < 0:
            print('Incorrect points format.')
            return
        python_score = int(split[1])
        dsa_score = int(split[2])
        database_score = int(split[3])
        flask_score = int(split[4])


        student_dict[student_id_number][3] += python_score
        student_dict[student_id_number][4] += dsa_score
        student_dict[student_id_number][5] += database_score
        student_dict[student_id_number][6] += flask_score

        logbook[student_id_number].append([python_score, dsa_score, database_score, flask_score])
        print('Points updated')


    else:
        print('Incorrect points format.')
        return

def find_student(student_input):
    global find_mode
    if student_input == 'back':
        find_mode = False
        return

    split = student_input.split(' ')

    if not re.fullmatch(r"[0-9]+", split[0]):
        print(f'No student is found for id={split[0]}')
        return

    student_number = int(split[0])

    if not student_number in student_dict.keys():
        print(f'No student is found for id={split[0]}')
        return


    print_python = student_dict[student_number][3]
    print_dsa = student_dict[student_number][4]
    print_database = student_dict[student_number][5]
    print_flask = student_dict[student_number][6]

    print(f'{student_number} points: Python={print_python}; DSA={print_dsa}; Databases={print_database}; Flask={print_flask};')

# 182365 4 0 0 8
# 182365 0 0 0 5
# 182366 0 8 0 4

def popular():
    global enrolled_python, enrolled_dsa, enrolled_database, enrolled_flask

    if len(student_dict.keys()) == 0:
        return 'n/a', 'n/a'

    popular_dict = {'Python': 0, 'DSA': 0, 'Databases': 0, 'Flask': 0}

    for k, v in student_dict.items():
        if v[3] > 0:
            popular_dict['Python'] += 1
        if v[4] > 0:
            popular_dict['DSA'] += 1
        if v[5] > 0:
            popular_dict['Databases'] += 1
        if v[6] > 0:
            popular_dict['Flask'] += 1


    max_pop = sorted(popular_dict.items(), key=lambda x: x[1], reverse=True)
    min_pop = sorted(popular_dict.items(), key=lambda x: x[1])

    highest_n = max_pop[0][1]
    lowest_n = min_pop[0][1]

    final_highest = []
    final_lowest = []

    for y in max_pop:
        if y[1] == highest_n:
            final_highest.append(y[0])
        else:
            continue

    for z in min_pop:
        if z[1] == lowest_n:
            if not z[0] in final_highest:
                final_lowest.append(z[0])
        else:
            continue

    if len(final_lowest) == 0:
        final_lowest.append('n/a')

    return final_highest, final_lowest

def difficulty():
    global enrolled_python, enrolled_dsa, enrolled_database, enrolled_flask

    activity_dict = {'Python': 0.0, 'DSA': 0.0, 'Database': 0.0, 'Flask': 0.0}

    if len(student_dict.keys()) == 0:
        return 'n/a', 'n/a'

    for k, v in student_dict.items():
        if v[3] > 0:
            activity_dict['Python'] += v[3]
        if v[4] > 0:
            activity_dict['DSA'] += v[4]
        if v[5] > 0:
            activity_dict['Database'] += v[5]
        if v[6] > 0:
            activity_dict['Flask'] += v[6]
        else:
            return 'n/a', 'n/a'

    p_count = get_logbook(0)
    dsa_count = get_logbook(1)
    database_count = get_logbook(2)
    flask_count = get_logbook(3)

    if p_count > 0:
        activity_dict['Python'] = activity_dict['Python'] / p_count
    if dsa_count > 0:
        activity_dict['DSA'] = activity_dict['DSA'] / dsa_count
    if database_count > 0:
        activity_dict['Database'] = activity_dict['Database'] / database_count
    if flask_count > 0:
        activity_dict['Flask'] = activity_dict['Flask'] / flask_count


    sorted_activity = sorted(activity_dict.items(), key=lambda x: x[1], reverse=True)
    reverse_activity = sorted(activity_dict.items(), key=lambda x: x[1])

    name_highest = sorted_activity[0][0]
    name_lowest = reverse_activity[0][0]

    return name_highest, name_lowest

def get_logbook(x):
    count = 0
    for k,v in logbook.items():
        standard = 0
        for i in v:
            if i[x] != standard:
                standard = i[x]
                count += 1
            else:
                continue

    return count

def acitvity():

    logbook_dict = {'Python': 0, 'DSA': 0, 'Databases': 0, 'Flask': 0}

    if len(logbook.keys()) == 0:
        return 'n/a', 'n/a'

    logbook_dict['Python'] = get_logbook(0)
    logbook_dict['DSA'] = get_logbook(1)
    logbook_dict['Databases'] = get_logbook(2)
    logbook_dict['Flask'] = get_logbook(3)

    highest = sorted(logbook_dict.items(), key=lambda x: x[1], reverse=True)
    lowest = sorted(logbook_dict.items(), key=lambda x: x[1])

    highest_n = highest[0][1]
    lowest_n = lowest[0][1]

    final_highest = []
    final_lowest = []

    for y in highest:
        if y[1] == highest_n:
            final_highest.append(y[0])
        else:
            continue

    for z in lowest:
        if z[1] == lowest_n:
            if not z[0] in final_highest:
                final_lowest.append(z[0])
        else:
            continue

    if len(final_lowest) == 0:
        final_lowest.append('n/a')

    return final_highest, final_lowest


def print_statistics():
    easy, difficult = difficulty()
    highest, lowest = acitvity()
    max_p, min_p = popular()
    print(f'Most popular: {max_p}')
    print(f'Least popular: {min_p}')
    print(f'Highest activity: {highest}')
    print(f'Lowest activity: {lowest}')
    print(f'Easiest course: {easy}')
    print(f'Hardest course: {difficult}')

def extra_statistics(statistics_input):
    global statistic_mode

    if statistics_input == 'back':
        statistic_mode = False
        return

    courses = ['Python', 'DSA', 'Databases', 'Flask', 'python', 'dsa', 'databases', 'flask']

    if statistics_input not in courses:
        print('Unknown course.')
        return


    if statistics_input == 'Python' or statistics_input == 'python':
        print('Python')
        print('id     points completed')
        if len(student_dict.keys()) > 0:
            python_db = [[k, v[3]] for k, v in student_dict.items()]
            sorted_python_db = sorted(python_db, key=lambda x: x[1], reverse=True)


            for i in range(len(sorted_python_db)):
                points = sorted_python_db[i][1]
                if points > 0:
                    s_id = sorted_python_db[i][0]
                    completed = round(((sorted_python_db[i][1] * 100) / max_python), 2)
                    print(f'{s_id} {points}    {round(completed, 1)}%')

        return

    elif statistics_input == 'DSA' or statistics_input == 'dsa':
        print('DSA')
        print('id     points completed')
        if len(student_dict.keys()) > 0:
            dsa_db = [[k, v[4]] for k, v in student_dict.items()]
            sorted_dsa_db = sorted(dsa_db, key=lambda x: x[1], reverse=True)

            for i in range(len(sorted_dsa_db)):
                points = sorted_dsa_db[i][1]
                if points > 0:

                    s_id = sorted_dsa_db[i][0]
                    completed = round(((sorted_dsa_db[i][1] * 100) / max_dsa), 2)
                    print(f'{s_id} {points}    {round(completed, 1)}%')

        return

    elif statistics_input == 'Databases' or statistics_input == 'databases':
        print('Databases')
        print('id     points completed')
        if len(student_dict.keys()) > 0:

            databases_db = [[k, v[5]] for k, v in student_dict.items()]
            sorted_databases_db = sorted(databases_db, key=lambda x: x[1], reverse=True)

            for i in range(len(sorted_databases_db)):
                points = sorted_databases_db[i][1]
                if points > 0:
                    s_id = sorted_databases_db[i][0]
                    completed = round(((sorted_databases_db[i][1] * 100) / max_database), 2)
                    print(f'{s_id} {points}    {round(completed, 1)}%')

        return

    elif statistics_input == 'Flask' or statistics_input == 'flask':
        print('Flask')
        print('id     points completed')
        if len(student_dict.keys()) > 0:
            flask_db = [[k, v[6]] for k, v in student_dict.items()]
            sorted_flask_db = sorted(flask_db, key=lambda x: x[1], reverse=True)

            for i in range(len(sorted_flask_db)):
                points = sorted_flask_db[i][1]
                if points > 0:
                    s_id = sorted_flask_db[i][0]
                    completed = round(((sorted_flask_db[i][1] * 100) / max_flask), 2)
                    print(f'{s_id} {points}    {round(completed, 1)}%')

        return


def notify_users():
    global notified_dict_python, notified_dict_dsa, notified_dict_databases, notified_dict_flask

    notification_list = []


    for k, v in student_dict.items():
        if not k in notified_dict_python:
            if v[3] == max_python:
                notified_dict_python.append(k)
                notification_list.append(k)
                name = v[0] + ' ' + v[1]
                print_message(v[2], name, 'Python')
        if not k in notified_dict_dsa:
            if v[4] == max_dsa:
                notified_dict_dsa.append(k)
                notification_list.append(k)
                name = v[0] + ' ' + v[1]
                print_message(v[2], name, 'DSA')
        if not k in notified_dict_databases:
            if v[5] == max_database:
                notified_dict_databases.append(k)
                notification_list.append(k)
                name = v[0] + ' ' + v[1]
                print_message(v[2], name, 'Databases')
        if not k in notified_dict_flask:
            if v[6] == max_flask:
                notified_dict_flask.append(k)
                notification_list.append(k)
                name = v[0] + ' ' + v[1]
                print_message(v[2], name, 'Flask')


    notification_set = set(notification_list)

    print(f'Total {len(notification_set)} students have been notified.')


def print_message(email, name, course):
    print(f'TO: {email}')
    print(f'Re: Your Learning Progress')
    print(f'Hello, {name}! You have accomplished our {course} course!')







while(True):
    user_input = input()
    if not statistic_mode:
        if not find_mode:
            if not adding_points_mode:
                if not adding_student_mode:
                    if user_input == 'exit':
                        print('Bye!')
                        break
                    elif user_input == 'back':
                        print("Enter 'exit' to exit the program.")
                    elif not user_input.strip():
                        print('No input')
                    elif user_input == 'add students':
                        print("Enter student credentials or 'back' to return.")
                        adding_student_mode = True
                        check_student_mode = True
                    elif user_input == 'list':
                        if len(student_dict) > 0:
                            print('Students:')
                            for key, value in student_dict.items():
                                print(key)
                        else:
                            print('No students found.')
                    elif user_input == 'add points':
                        print("Enter an id and points or 'back' to return.")
                        adding_points_mode = True
                    elif user_input == 'find':
                        print("Enter an id or 'back' to return.")
                        find_mode = True
                    elif user_input == 'statistics':
                        print("Type the name of a course to see details or 'back' to quit")
                        statistic_mode = True
                        print_statistics()
                    elif user_input == 'notify':
                        notify_users()
                    else:
                        print('Unknown command!')
                else:
                    if adding_student_mode:
                        check_all(user_input)
            else:
                add_points(user_input)
        else:
            find_student(user_input)
    else:
        extra_statistics(user_input)














