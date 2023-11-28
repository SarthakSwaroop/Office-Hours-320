from DBCalls import DBCalls


dbconn = DBCalls();
dbconn.connect_to_db();

def print_result(result):
    """prints the result set, which is a list of tuples.
       prints no matches found if no tuples in list."""
    res_list = result[0]
    if len(res_list) == 0:
        print('no matches found')
    for i in range(len(res_list)):
        print(res_list[i])

not_done = True

print("Welcome to the Shapley Prime DB Call Test")

print("Pick what you would like to do")

while not_done:
    print("1- Get the list of all of the student emails\n"+
          "2- Get the hour rankings of a student.\n"+
          "3- Insert a new Student\n"+
          "X- to quit.")

    choice = input();
    if choice == 'X' or choice == 'x':
        break
    elif choice == '1':
        result = dbconn.get_emails();
        print(result)



dbconn.close_db()

if __name__=="__main__":
    print("Have a nice day!")