css = '''
<style>
.chat-msg{
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex;
}
.chat-msg.bot{
    background-color: #475063;
}
.chat-msg.user{
    background-color: #2b313e;
}
.chat-msg .avatar{
    width: 15%;
}
.chat-msg .avatar img{
    width: 80px; height: 80px; border-radius: 50%; object-fit: cover;
}
.chat-msg .message{
    width: 85%; padding: 0 1.5rem; color: #fff;
}
.chat-msg h1{
    text-align: center;
}
</style>
'''

bot_template = '''
<div class="chat-msg bot">
    <div class="avatar">
        <img src="https://media.tenor.com/3_hOO8r0lZYAAAAC/robot-anime.gif">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-msg user">
    <div class="avatar">
        <img src="https://64.media.tumblr.com/4a5361e3f016fda2d6b4a7501f91d1ca/13ef9ecd4c994832-74/s540x810/553ceaf935aac5a83c0a13631676585b3ec64263.gif">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

summary_template = '''
<div class="chat-msg user">
    <h1>Summary</h1>
    <div class="message">{{MSG}}</div>
</div>
'''

question_template = '''
<div class="chat-msg bot">
    <h1>Summary</h1>
    <div class="message">{{MSG}}</div>
</div>
'''
