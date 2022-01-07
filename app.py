from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from linebot.models.send_messages import ImageSendMessage
from mod import(
    screenshot,conversion
)
import os

app = Flask(__name__)

line_bot_api = LineBotApi('qjhCu72uiG68tLkOVhyW2k7R/wds/dwMlHV2+1wxddSMRIiVC51ehpc3G8Q4oZnxHJA3QnKDJPpayIkM8mmTbQkosIzwfLMneEpfMJxN/U+n/3y4FmrROoKEfRacl5GT9orgjLZobyrfRTCfe3O/wwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('375c2cc62e5aaaef6cc60cbc5f784627')




@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    search_word=conversion(event.message.text,'.')
    screenshot(search_word)
    line_bot_api.reply_message(
        event.reply_token,
        ImageSendMessage(image=os.path.join(os.path.dirname(os.path.abspath(__file__)), "image/screen.png")))




if __name__ == "__main__":
    app.run()

#app.run(port=5000,debug=False)
