# Подключаем модуль случайных чисел 
import random
# Подключаем модуль для Телеграма
import telebot
# Указываем токен
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
# Заготовки для трёх предложений

r=0
k=0
s=0
users =[]
users2=[]
chats=[]
answers_questen =["П","Правда","правда"]
answers_action =["Д","Действие","Действо"]
questen = ["Назовите любые три вещи, о которых вы думаете, сидя на сиденье унитаз","Назовите последнее, что вы искали в Google", "Какую самую большую ложь ты кому-то сказал?", "Назовите любую из своих худших привычек, от которой вы хотите избавиться.","Если бы у вас была машина времени, в какой период вы бы поехали?","Вы когда-нибудь были загипнотизированы?","За кого вы голосовали? Или за кого бы вы проголосовали?","Если бы вам пришлось выбирать ум или красоту, что бы вы выбрали?","Какой самый худший подарок вы когда-либо получали?","Если бы вашу жизнь сняли в кино, кто бы вас сыграл?", "Сколько раз вы тайком убегали из дома?","Можете ли вы прикоснуться языком к носу?","Если бы вы могли жить где угодно в мире, где бы вы жили?","Какой день в вашей жизни был лучшим?","Вы занимаетесь каким-нибудь спортом?","Был ли какой-нибудь учитель, которого вы считали горячим?","Вы ведете дневник?","Вы бы когда-нибудь начали использовать сайт знакомств?","Какой самый мерзкий розыгрыш вы над кем-то разыграли?","Какой был ваш худший поцелуй?","Вас когда-нибудь рвало в чьей-то машине?","Вы бы предпочли быть умным или счастливым, и почему?","Вы когда-нибудь болели заболеванием, передающимся половым путем?","Когда вы научились ездить на велосипеде?","Если бы не было денег, что бы вы делали со своей жизнью?","Вы когда-нибудь ходили во сне?","Вы спите голым?","Вы когда-нибудь что-то ломали и обвиняли кого-то другого в этом?","Вы когда-нибудь приводили кого-нибудь в дом без разрешения?","Что в вас самое странное? Вы этим гордитесь?","Кто ваш любимый персонаж Диснея?","Что бы вы сделали, если бы на день были невидимы?","Самое странное место, где вы занимались любовью?","Что вы делали в сексе, что никогда не сделаете снова?","Самая дикая фантазия, которая исполнилась?"]
questen2=[]
action= ["Выпей рюмку алкоголя или литр воды","Спародируй любого человека из присутствующих","Встань на стул и прочитай стихотворение","Скажи на видео, что Синий Кофе лучший просто, заебись усы", "Изобрази свой дьявольский смех","Покажи любой фокус","Покажи, как ты надеваешь нижнее белье по утрам или принимаешь душ","Признайся в любви кому-то из присутствующих и пригласи на свидание","Назови свой пароль от социальной сети, а потом поменяй его","Придумай историю со словами «девушка», «кот», «лифчик», «чемодан», «поцелуй»","Скажи комплимент и гадость каждому игроку","Говори 3 минуты «мяу» после каждого слова или предложения других людей","Придумай всем клички, характеризующие их","Изобрази известную личность, чтобы другие игроки угадали","Расскажи смешной анекдот или историю, произошедшую с тобой","Устрой случайному человеку «прожарку». Высмеивай его недостатки 2 минуты"]
action2=[]
user_game=()
questen_msg=()
action_msg=()

def rand():
    r=random.randint (1,4)
    r1=r=random.randint (1,5)

    questen2=questen[r1::r]
    action2=action[r1::r]
    for i in questen2:
        questen.remove(i)

    for i in action2:
        action.remove(i)
    

rand()

@bot.message_handler(commands=["exit"])  
def exit_game(message):
    global users, users2,s,k
    user_exit=str(message.from_user.username)
    if user_exit=='None':
        user_exit=str(message.from_user.first_name)
    if  user_exit in  users:
        users.remove(user_exit)
        poka="@"+user_exit + " покинул(а) игру"
        bot.send_message(message.chat.id, text=poka)
    else:
        poka="@"+user_exit + ", вы не были в списке игроков!"
        bot.send_message(message.chat.id, text=poka)

@bot.message_handler(commands=["stop"])  
def stop_game(message):
    global users, users2,s,k
    s=0
    k=0
    users =[]
    users2=[]
#    print (s)
    bot.send_message(message.chat.id, 'Игра остановлена')

@bot.message_handler(commands=["start"])  
def start_game(message):
    global users,s
    
    if s < 3:
        if len(users)!=0:
            s=s+1
            next_game(message)
        else:
            bot.send_message(message.chat.id, "Слишком мало игроков!  Вступайте в игру командой /reg")
            s=s+1
    else:
        bot.send_message(message.chat.id, 'Игра уже запущена')

@bot.message_handler(commands=["reg"])
def reg_game(message):
    global users,chat
    
    user=str(message.from_user.username)
    if user=='None':
        user=str(message.from_user.first_name)
    if  user not in  users:
#Если пользователь не зарегистрирован, то он регается 
        users.append(user)
        user_reg="@"+user + ", вы успешно зарегистрированы"
        bot.send_message(message.chat.id, user_reg)
    else:
        user_reg="@"+user + ", вы уже зарегистрированы"
        bot.send_message(message.chat.id, user_reg)
            
    
@bot.message_handler(commands=["next"])
def next_game(message):
    global k, users, users2, user_game

    k=0
    if len(users)!=0:
        user_game=str(random.choice(users))
        usr="@"+user_game + ", правда или действие?"
        bot.send_message(message.chat.id, usr)
        if user_game not in users2:
                users.remove(user_game)
                users2.append (user_game)
        go_game(message)
    else:
        user_game=str(random.choice(users2))
        users=users2.copy ()
        users2=[]
        usr="@"+user_game + ", правда или действие?"
        bot.send_message(call.message.chat.id, usr)
    print (users)# Формируем вопросы
    print (users2)    
    
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global k
    global users
    global users2
    global user_game
    k=0
    
    if call.data == "next_q":

        if len(users)!=0:
            user_game=str(random.choice(users))
            usr="@"+user_game + ", правда или действие?"
            bot.send_message(call.message.chat.id, usr)
            if user_game not in users2:
                users.remove(user_game)
                users2.append (user_game)
        else:
            if len(users2)!=0:
                user_game=random.choice(users2)
                users=users2.copy ()
                users2=[]
                usr="@"+user_game + ", правда или действие?"
                bot.send_message(call.message.chat.id, usr)
            
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
   
        
            
    print (users)# Формируем вопросы
    print (users2)      
        
@bot.message_handler(content_types=['text'])
def go_game(message):     
    prevAnswer = message.text
    prevAnswer=prevAnswer.title()
    global user_game, questen2,questen,k,questen_msg,action,action2, action_msg,answers_questen,answers_action, msg
    
    

    
        
    if ((prevAnswer in answers_questen) or (prevAnswer in answers_action)) and ((message.from_user.username or message.from_user.first_name) == user_game):
        k=k+1
        print(k)
        
    if k==1:
        if (prevAnswer in answers_questen): # and (message.from_user.username == user_game) 
            if (len (questen) > 1):
                questen_msg = random.choice(questen)
                questen2.append (questen_msg)
                questen.remove(questen_msg)
        
            else:
                questen_msg = random.choice(questen2)
                questen=questen2.copy ()
                questen2=[]
                rand()
            msg = "@"+user_game + " " +  questen_msg
            
#            bot.send_message(message.chat.id, msg)
        if (prevAnswer in answers_action): #and (message.from_user.username == user_game):
            if len (action) != 0:
                action_msg = random.choice(action)
                action2.append(action_msg)
                action.remove(action_msg)
        
            else:
                action_msg = random.choice(action2)
                action=action2.copy ()
                action2=[]
                rand()
            msg = "@"+user_game + " " +  action_msg      
#            bot.send_message(message.chat.id, msg)
            
        keyboard = types.InlineKeyboardMarkup()
        next_q = types.InlineKeyboardButton(text='Следующий ход', callback_data='next_q')
        keyboard.add(next_q)
        bot.send_message(message.chat.id, text=msg,reply_markup=keyboard)
        k=k+1
        print(k)
#    if k > 2:
#        msg = "@"+user_game + " заменить нельзя"        
#        bot.send_message(message.chat.id, msg)
    print (len (questen2))
    print (len (questen))
    

bot.polling(none_stop=True, interval=0)

