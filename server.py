from base64 import encode
from concurrent.futures import thread
from email import message
from ipaddress import ip_address
from operator import index
from os import remove
import socket
from threading import Thread
from webbrowser import get

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port =5500

server.bind((ip_address, port))
server.listen()

list_of_clients = []

questions=[
    "what is the italian word for PIE? \n a.Mozarella\n b.pasty\n c.patty\n d.pizza",
    "water boils at 212 units at which ascale? \n a.Fahrenbeit\n b.celaius\n c.rankine\n d.kelvin",
    "who gifted the statue of liberty to the US? \n a.brazil\n b.france\n c.wales\n d.germany"
    "which planet is closest to the sun? \n a.mercury\n b.pluto\n c.earth\n d.venus"
]

answers=['d','a','b','a']

def clientthread(conn, questions):
     score=0
     conn.send("Welcome to the quiz game!".encode('utf-8'))
     conn.send("You will recive a question.the answer to that question should be one of a,b,c,d\n".encode('utf-8'))
     conn.send("Good luck!\n\n".encode('utf-8'))
     index,question,answer = get_random_answer_question(conn)
     while True:
        try:
             message = conn.recv(2048).decode('utf-8')
             if message:
                if message.lower() == answer:
                    score +=1
                    conn.send(f"bravo!your score is {score}\n\n".encode('utf-8')

                else:
                    conn.send("Incorrect answer! Better luck next time!\n\n".encode('utf-8'))
                remove_question(index)
                index,question,answer = get_random_answer_question(conn)
            else:
                remove(conn)
        except:
            continue
            



def get_random_answer_question(conn):
    random_index = random.randint(0,len(questions)-1)
    random_question = questions[random_index]
    random_answer = answers[random_index]
    conn.send(random_question.encode('utf-8'))
    return random_index,random_question,random_answer

def remove_question(index):
    questions.pop(index)
    answers.pop(index)








while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    new_thread = Thread(target=clientthread,args=(conn, questions))
    new_thread.start()

    conn.send("welcome to this quiz game!".encode{'utf-8'})

   