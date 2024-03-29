from pyrogram import Client, filters, idle
from pyrogram.types import InlineQueryResultPhoto, InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle, InputTextMessageContent
from pyrogram import enums
TOKEN = 'Token'
app = Client(
'ystbot', 25939451, '243853dc20929b33d40435f2606ad50e', bot_token=TOKEN
)
######################
LOG = -1002016082222 #
######################

@app.on_message(filters.command("start") & filters.private)
async def startmsg(app, message):
   text = '''
👋 Hi {}
اهلا بيك بهمسة الزنوج السرية 🧑🏿

Devs : @znoghnews

طريقة الاستعمال
@znoghsecretsbot 😋 @NB_JG
أو
@znoghsecretsbot + Message + User

'''.format(message.from_user.mention)
   key = InlineKeyboardMarkup (
     [[
       InlineKeyboardButton ("تجربه", switch_inline_query='شلونك @NB_JG') ]]
   )
   await message.reply(text, reply_markup=key, quote=True)


@app.on_inline_query(filters.regex("@"))
async def whisper(app, iquery):
    user = iquery.query.split("@")[1]
    if " " in user: return 
    user_id = iquery.from_user.id
    query = iquery.query.split("@")[0]
    if user == "all":
      text = "🎊 الهمسه للكل"
      username = "all"
    else:
      get = await app.get_chat(user)
      user = get.id
      username = get.first_name
      text = f"**🔒 الهمسه للزنجي :  ( {username} ) .ا**"
    send = await app.send_message(LOG, query)
    reply_markup = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("📪 الدخول للهمسه", callback_data=f"{send.id}جلب{user}from{user_id}")
      ]]
    )
    await iquery.answer(
      results=[
       InlineQueryResultArticle(
          title=f"📪  ارسال الهمسه للزنجي {username}",
          url="http://t.me/znoghnews",
          input_message_content=InputTextMessageContent(
            message_text=text,
            parse_mode=enums.ParseMode.MARKDOWN 
          ),
          reply_markup=reply_markup
       )
      ],
      cache_time=1
    )

@app.on_inline_query()
async def whisper(app, query):
    text = '''
اهلا بيك بهمسة الزنوج السرية 🧑🏿

Devs : @znoghnews

طريقة الاستعمال
@Znoghsecretsbot 😋 @NB_JG
أو
@Znoghsecretsbot + Message + User
'''
    await query.answer(
        results=[
            InlineQueryResultPhoto(
                title="🔒 اكتب الهمس + اسم المستخدم",
                photo_url='https://unmakable-attribute.000webhostapp.com/one.png',
                description='@znoghsecretsbot  شلونك @NB_JG',
                reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("🔗", url='t.me/znoghnews')]]),
                input_message_content=InputTextMessageContent(text)
            ),
        ],
        cache_time=1
    )
    
@app.on_callback_query(filters.regex("جلب"))
async def get_whisper(app,query):
    sp = query.data.split("جلب")[1]
    user = sp.split("from")[0]
    from_user = int(sp.split("from")[1])
    reply_markup = InlineKeyboardMarkup(
      [
      [
        InlineKeyboardButton("الزنجي شاف الهمسه تكدر تمسحها", callback_data=query.data)
      ],
      [
        InlineKeyboardButton("🗑️", callback_data=f"DELETE{from_user}")
      ],
      ]
    )
    if user == "all":
       msg = await app.get_messages(LOG, int(query.data.split("جلب")[0]))
       await query.answer(msg.text, show_alert=True)
       try:
         await query.edit_message_reply_markup(
           reply_markup
         )
       except:
         pass
       try:
         alert0 = f"📭 {query.from_user.mention} الفتح من @all همسه ."
         await app.send_message(from_user, alert0)
       except:
         pass
       return 
    
    else:
      if str(query.from_user.id) == user:
        msg = await app.get_messages(LOG, int(query.data.split("جلب")[0]))
        await query.answer(msg.text, show_alert=True)
        try:
         await query.edit_message_reply_markup(
           reply_markup
         )
        except:
         pass
        return 

      if query.from_user.id == from_user:
        msg = await app.get_messages(LOG, int(query.data.split("جلب")[0]))
        await query.answer(msg.text, show_alert=True)
        return
      
      else:
        get = await app.get_chat(int(user))
        touser = get.first_name
        alert = f"ℹ️ اشعار حماية همسة الزنوج واحد راد يفتح الهمسة بس ماكدر {touser}:\n\n"
        alert += f"👤 اسمه : {query.from_user.mention}\n"
        alert += f"🆔 ايديه : {query.from_user.id}\n"
        if query.from_user.username:
          alert += f"🔍 يوزره : @{query.from_user.username}\n"
        alert += "\n\n📭"
        await query.answer("🔒 الفضول قتل القطه", show_alert=True)
        try:
          await app.send_message(
            from_user,
            alert
          )
        except:
          pass
        return 

@app.on_callback_query(filters.regex("DELETE"))
async def del_whisper(app,query):
   user = int(query.data.split("DELETE")[1])
   if not query.from_user.id == user:
     return await query.answer("❓ لازم الشخص الرسل الهمسه يكدر يحذفها / حماية الزنوج")
   
   else:
     reply_markup = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("المطور", url="https://t.me/NB_JG")
      ]]
    )
     await query.edit_message_text(f"**🗑️ تم الحذف بواسطة :  ( {query.from_user.mention} ) .**",
       reply_markup=reply_markup
     )
     

app.start()
print("🎖️")
idle()
