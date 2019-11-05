from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from xvfbwrapper import Xvfb


def before_all(context):
    context.vdisplay = Xvfb()
    context.vdisplay.start()
    print("> Starting the browser")
    capabilities = DesiredCapabilities.FIREFOX.copy()
    capabilities['acceptSslCerts'] = True
    context.driver = webdriver.Firefox(
        capabilities=capabilities,
        executable_path='/app/geckodriver'
    )
    context.driver.set_window_size(1024, 768)


def after_all(context):
    print("< Closing the browser")
    try:
        context.driver.close()
        context.driver.quit()
    except:
        pass
    context.vdisplay.stop()