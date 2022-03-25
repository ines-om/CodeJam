n = input("Number of messages: ")

i = 0
messages = []
for i in range(0, int(n)):
    message = input("Insert message: ")
    messages.append(message)
    i+1

i = 0
for i in range(0, int(n)):
    i_1 = i+1
    print("Case " + "#" + str(i_1) + ":")
    dash = "-"
    dash_nr = len(messages[i])
    dash_n = int(dash_nr)*dash
    print("+-" + str(dash_n) + "-+")
    print("| " + str(messages[i]) + " |")
    print("+-" + str(dash_n) + "-+")