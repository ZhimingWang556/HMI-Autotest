from poium import Page, PageElement
from config.hmi_config import CAPS


class HMIPage(Page):
    # 系统设置按钮
    setting_btn = PageElement(id_ = "com.baidu.adu.hmi.pilotpanel:id/img_system")
    # 初始化自检
    # 下一步
    next_btn = PageElement(id_ = "com.baidu.adu.hmi.pilotpanel:id/btn_next")
    # 系统化自检
    # 登录按钮
    loggin = PageElement(id_ = "com.baidu.adu.hmi.pilotpanel:id/btn_login")

    # 登录界面
    another_count = PageElement(xpath = "//android.view.View[@content-desc='登录其他帐'")
    # 账号输入
    count = PageElement(xpath = "//android.webkit.WebView[@content-desc='登录百度帐号']/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[1]/android.widget.EditText")
    # 下一步
    next_login = PageElement(xpath = "//android.widget.Button[@content-desc='下一步']")
    # 密码
    password = PageElement(xpath = "//android.webkit.WebView[@content-desc='登录百度帐号']/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.widget.EditText")
    # 登录
    login_btn = PageElement(xpath = "//android.widget.Button[@content-desc='登 录']")

    # 消息
    msg_btn = PageElement(id_ = "com.baidu.adu.hmi.pilotpanel:id/btn_notification")

    # 地图视角
    map_view = PageElement(id_ = "com.baidu.adu.hmi.pilotpanel:id/browse_mode")

    # 排班按钮
    schedule_btn = PageElement(id_ = "com.baidu.adu.hmi.pilotpanel:id/btn_schedule")
