# ai generated to test
import time
import tulip
import lvgl as lv

class TimezoneClockApp(tulip.UIScreen):
    def __init__(self):
        # Initialize a standard Tulip UI screen
        super().__init__()
        
        # Define timezones with manual UTC offsets (in hours)
        self.zones = [
            {"name": "UTC", "offset": 0},
            {"name": "New York (EST)", "offset": -5},
            {"name": "London (GMT/BST)", "offset": 0},
            {"name": "Amsterdam (CET)", "offset": 1},
            {"name": "Tokyo (JST)", "offset": 9}
        ]
        self.current_zone_index = 0

        # Create a container to hold our UI elements nicely
        self.cont = lv.obj(self.screen)
        self.cont.set_size(400, 250)
        self.cont.center()
        self.cont.set_flex_flow(lv.FLEX_FLOW.COLUMN)
        self.cont.set_flex_align(lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER)

        # 1. Title Label
        self.title_label = lv.label(self.cont)
        self.title_label.set_text("World Clock")

        # 2. Main Large Time Label
        self.time_label = lv.label(self.cont)
        # Apply built-in large font for clarity
        self.time_label.set_style_text_font(lv.font_unscii_8, 0)
        
        # 3. Timezone Dropdown Selector
        self.dropdown = lv.dropdown(self.cont)
        options = "\n".join([z["name"] for z in self.zones])
        self.dropdown.set_options(options)
        self.dropdown.add_event_cb(self.on_zone_change, lv.EVENT.VALUE_CHANGED, None)

        # Start background timer task to refresh every 500ms
        self.timer = lv.timer_create(self.update_clock, 500, None)

    def on_zone_change(self, e):
        # Update active timezone index based on selection
        self.current_zone_index = self.dropdown.get_selected()

    def update_clock(self, timer_obj):
        # Get system time (Assumes system clock tracks UTC time)
        now = time.time()
        
        # Apply selected timezone offset (convert hours to seconds)
        active_zone = self.zones[self.current_zone_index]
        local_timestamp = now + (active_zone["offset"] * 3600)
        
        # Break timestamp into time components
        t = time.localtime(local_timestamp)
        
        # Format and display time string
        time_str = f"{t[3]:02d}:{t[4]:02d}:{t[5]:02d}"
        self.time_label.set_text(time_str)

    def on_exit(self):
        # Clean up the background timer when closing the application
        if self.timer:
            self.timer.delete()

# Launch the LVGL application on Tulip
app = TimezoneClockApp()
app.present()
