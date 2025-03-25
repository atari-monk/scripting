import sys
sys.path.append('C:\\atari-monk\\code\\scripting')
from libs.chrome import open_url_with_selenium, wait_and_notify, create_chrome_options

options = create_chrome_options()
driver = open_url_with_selenium("https://chat.openai.com/", options)
wait_and_notify('ChatGPT should be opened', 10)
