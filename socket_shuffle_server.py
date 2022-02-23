import random, string, threading, socket


default_characters = (" ","!", "@", "#", "$", "%", "^", "*", "(", ")", ",", ".", "'", ";", ":")


def Map_chars():
    global char_to_encrypted_mapping, encrypted_to_char_mapping
    encrypted_chars = ['KFE@B','wt%cV','#UP^Z','PD!ds','uwU^{','D(Avy',']*kCu','A]Q$o','fo*rU','{tlvd','WZJMX','lhcLL','GS#ck','gABIs','OcH[m',')dX){','TxZwM','&R}N(','zrpWO','rcr!#','kK]wy','pCCLK','Y#fHI','EWXps','uGdIc','oNP)Z','Vjy^q','l%MHs','wNtnb','#*ci#','cMt]y','zvkO!','wnJPN','blC!q','y@ULR','fe(vP','&q{Mb','[^NAr','km#tJ','yOKnH','PpbfW','GAwMF','trJS!','^d$Ro','C!]gj','hpt!h','%HjUM','cin^L','AfCeV','nShgx','R(ivD','C&wgh','D*eIS','b]pJk','*Wq&p','*&uBD','AK^Tl','WouCZ','w&F%]','qGtBC','E@F[g','ZvA(e','^dybR','ulhKY','kbt]P','&KDZZ']
    char_to_encrypted_mapping = {}
    encrypted_to_char_mapping = {}
    for i in range(len(string.ascii_letters)):
        single_map_1 = {string.ascii_letters[i] : encrypted_chars[i]}
        single_map_2 = {encrypted_chars[i] : string.ascii_letters[i]}
        char_to_encrypted_mapping.update(single_map_1)
        encrypted_to_char_mapping.update(single_map_2)


def Shuffle():
    # TODO
    global server_char_map
    # TODO
    server_char_map = {}
    letters = []
    shuffled_letters = []
    for char in string.ascii_letters:
        letters.append(char)
        shuffled_letters.append(char)
    random.shuffle(shuffled_letters)
    random.shuffle(letters)
    for i in range(len(letters) - 1):
        char_pair = {letters[i] : shuffled_letters[i]}
        server_char_map.update(char_pair)

#TODO replace clients encrypt mapping
def Encrypt_mapping(char_mapping):
    # TODO
    global encrypted_mapping
    # TODO
    encrypted_mapping = ""
    for key, value in char_mapping.items():
        pair = {char_to_encrypted_mapping.get(key) : char_to_encrypted_mapping.get(value)}
        for key, value in pair.items():
            encrypted_mapping += key + value



#TODO otestovat encrypt decrypt mapping a zkopirovat do clienta
def Decrypt_mapping(mapping_to_decrypt):
    # TODO
    global decrypted_mapping
    # TODO
    mapping_to_decrypt_dictionary = {}
    decrypted_mapping = {}
    for i in range(0, 520, 10):
        pair = {mapping_to_decrypt[i:i+5] : mapping_to_decrypt[i+5:i+10]}
        mapping_to_decrypt_dictionary.update(pair)
    for key, value in mapping_to_decrypt_dictionary.items():
        pair = {encrypted_to_char_mapping.get(key) : encrypted_to_char_mapping.get(value)}
        decrypted_mapping.update(pair)
    print("decrypted mapping")


def Encode_message(message, char_mapping):
    # TODO
    global encoded_message
    # TODO
    encoded_message = ""
    for char in message:
        get_char = char_mapping.get(char)
        if get_char != None:
            encoded_message += char_mapping.get(char)
            continue
        elif char in default_characters:
            encoded_message += char
        elif get_char == None:
            encoded_message += "_"
    print(f"Encoded message : {encoded_message}")


def Decode_message(message, char_mapping):
    # TODO
    global decoded_message
    # TODO
    decoded_message = ""
    for char in message:
        appended = False
        if char in default_characters:
            decoded_message += char
            continue
        for decrypted, encrypted in char_mapping.items():
            if encrypted == char:
                decoded_message += decrypted
                appended = True
                break
        if not appended:
            decoded_message += "_"
    print(f"Decoded message : {decoded_message}")

def Get_server_info():
    # TODO
    global CLIENT, PORT, ADDRESS
    # TODO
    PORT = 50000
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDRESS = (SERVER, PORT)

def Client():
    global connection, address, server, disconnected
    disconnected = False
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDRESS)
    server.listen()
    connection, address = server.accept()


def Send(message, encrypted_char_mapping):
    message = message.encode()
    encrypted_char_mapping = encrypted_char_mapping.encode()
    connection.send(message)
    connection.send(encrypted_char_mapping)

def Receive():
    while not disconnected:
        try:
            client_decoded_message = connection.recv(1024).decode()
            encrypted_client_mapping = connection.recv(1024).decode()
            Decrypt_mapping(encrypted_client_mapping)
            Decode_message(client_decoded_message, decrypted_mapping)
            print("Enter a message : ")
        except:
            pass

print("Server is starting ...")
Map_chars()
Get_server_info()
Client()
receive_threading = threading.Thread(target=Receive)
receive_threading.start()

while not disconnected:
    Shuffle()
    msg = input("Enter a message : ")
    if msg.lower() == "quit" or msg.lower() == "exit":
        disconnected = True
        try:
            connection.close()
        except:
            pass
    try:
        Encode_message(msg, server_char_map)
        Encrypt_mapping(server_char_map)
        Send(encoded_message, encrypted_mapping)
    except:
        pass










