import tulip
import lvgl as lv
import requests

WEBHOOK_URLS = {
    "lamp aan/uit": "http://homeassistant.local:8123/api/webhook/-Q_FOvAWzpGNMYOEoU24iaIxL",
    "huiswerk": "http://homeassistant.local:8123/api/webhook/-h8EgXtgZ55psC0-Ti_6-B_FL",
    "alles uit": "http://homeassistant.local:8123/api/webhook/-0PWk91O6w9tFgbQSU9BMQh3P",
}

def webhook(label):
    try:
        response = requests.post(WEBHOOK_URLS[label])
        code = response.status_code
        response.close()
    except Exception as e:
        error = str(e)
        print(f"Error sending webhook: {error}")

def button_cb(evt):
    if evt.code == lv.EVENT.CLICKED:
        btn = evt.get_target()
        label = btn.get_child(0).get_text()
        webhook(label)

def run(screen):
    # setup
    screen.bg_color = 0
    screen.offset_y = 100

    screen.group.set_style_text_font(lv.font_tulip_11,0)
    screen.add(tulip.UILabel("hai matthias, welcome back :)"), x=400,y=100)

    screen.add(tulip.UIButton("lamp aan/uit", fg_color=255, bg_color=200, callback=button_cb),x=10, y=10)
    screen.add(tulip.UIButton("huiswerk", fg_color=255, bg_color=200, callback=button_cb),x=10, y=70)
    screen.add(tulip.UIButton("alles uit", fg_color=255, bg_color=200, callback=button_cb),x=10, y=130)

    screen.present() # we are ready