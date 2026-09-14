import tulip
import lvgl as lv
import requests
import machine

# webhook stuff
WEBHOOK_URLS = {
    "lamp aan/uit": "http://homeassistant.local:8123/api/webhook/-Q_FOvAWzpGNMYOEoU24iaIxL",
    "alles uit": "http://homeassistant.local:8123/api/webhook/-h8EgXtgZ55psC0-Ti_6-B_FL",
    "huiswerk": "http://homeassistant.local:8123/api/webhook/-0PWk91O6w9tFgbQSU9BMQh3P",
}

def webhook(label):
    try:
        response = requests.post(WEBHOOK_URLS[label])
        code = response.status_code
        response.close()
    except Exception as e:
        error = str(e)
        print(f"Error sending webhook: {error}")

def update_time_cb(time_label, timer):
    rtc = machine.RTC()
    now = rtc.datetime()
    time_label.label.set_text(f"{now[4]:02d}:{now[5]:02d}:{now[6]:02d}")

def clock():
    url = "https://world-time-api3.p.rapidapi.com/timezone/Europe/Amsterdam"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "x-rapidapi-host": "world-time-api3.p.rapidapi.com",
	    "x-rapidapi-key": "3fdf540233msh63becb7ea0fc6a9p1e874cjsna6a075c58654",
    }

    res = requests.get(url, headers=headers)
    data = res.json()
    dt_str = data.get('datetime')
    if not dt_str:
        #print(data)
        return

    year   = int(dt_str[0:4])    # "2025"
    month  = int(dt_str[5:7])    # "08"
    day    = int(dt_str[8:10])   # "03"
    hour   = int(dt_str[11:13])  # "07"
    minute = int(dt_str[14:16])  # "32"
    second = int(dt_str[17:19])  # "19"

    rtc = machine.RTC()
    rtc.datetime((year, month, day, 0, hour, minute, second, 0))

    now = rtc.datetime()
    time_label = f"{now[4]:02d}:{now[5]:02d}:{now[6]:02d}"
    return time_label

# end of da webhook logic

def button_cb(label):
    def cb(*args, **kwargs): # AI found this out, but it means 'I love everything now'
        webhook(label)
    return cb

def run(screen):
    # setup 
    screen.bg_color = 0
    screen.offset_y = 100

    screen.group.set_style_text_font(lv.font_montserrat_12,0)
    screen.add(tulip.UILabel("hai matthias, welcome back :)", font=lv.font_montserrat_24, w=600), x=125, y=100)

# webhookie

    time_text = clock()
    time_label = tulip.UILabel(time_text if time_text else "--:--:--", font=lv.font_montserrat_36, w=600)
    screen.add(time_label, x=175, y=250)
    
    # Update time every second
    lv.timer_create(lambda timer: update_time_cb(time_label, timer), 1000, None)
    
# end of da webhook

    screen.add(tulip.UIButton("lamp aan/uit", fg_color=0, bg_color=178, callback=button_cb("lamp aan/uit"), w=200, h=100,font=lv.font_montserrat_24),x=175, y=450)
    screen.add(tulip.UIButton("alles uit", fg_color=255, bg_color=178, callback=button_cb("alles uit")),x=300, y=350)
    screen.add(tulip.UIButton("huiswerk", fg_color=255, bg_color=178, callback=button_cb("huiswerk")),x=400, y=350)


    screen.present() # we are ready