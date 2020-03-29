from csv import reader
from csv import writer

if __name__ == '__main__':
    questions = []
    answers = []
    with open('data.csv', 'r') as read_file:
        csv_reader = reader(read_file)
        for row in csv_reader:
            if row[0] == 'Participant Code':
                for value in row:
                    questions.append(value)
            elif row[0] == 'KEY':
                for value in row:
                    answers.append(value)

    q_dict = {questions[i] : answers[i] for i in range(len(questions))}
    
    with open ('data.csv', 'r') as read_file, \
        open ('new_data.csv', 'w', newline='') as write_file:
        csv_reader = reader(read_file)
        csv_writer = writer(write_file)
        for row in csv_reader:
            if row[0] == 'Participant Code':
                row.append('Test Score')
            else:
                cur_score = 0
                for col in range(6,33):
                    if row[col] == answers[col]:
                        cur_score = cur_score + 1
                row.append(round(cur_score/27*100,2))
            csv_writer.writerow(row)
        
            