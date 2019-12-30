import unittest
import sys
from os.path import dirname, abspath
BASE_PATH = dirname(dirname(abspath(__file__)))
sys.path.append(BASE_PATH)
from common.hmi_test import HmiTest
from page.hmi_page import HMIPage
from time import sleep
from appium.webdriver.common.touch_action import TouchAction


class TestHMILogin(HmiTest):

    def test_login(self):
        driver = self.driver
        page = HMIPage(driver)
        driver.implicitly_wait(10)
        # 系统初始化化自检成功，点击『下一步』
        page.next_btn.click()

        # 系统化自检通过，点击登录
        page.loggin.click()
        # driver.implicitly_wait(5)

        # sleep(5)

        # 选择登录其他账号
        another_count = driver.find_element_by_accessibility_id("登录其他帐号")
        TouchAction(driver).tap(another_count).release().perform()
        # 账号输入『Apollo_hmi』
        count = driver.find_element_by_class_name("android.widget.EditText")
        count.send_keys("apollo_hmi")
        try:
            # 点击下一步
            next_button = driver.find_element_by_accessibility_id("下一步")
            TouchAction(driver).tap(next_button).release().perform()
        except:
            # 点击换个方式
            change_way = driver.find_element_by_accessibility_id("换个登录方式")
            TouchAction(driver).tap(change_way).release().perform()
            sleep(2)
            # 帐号密码登录
            TouchAction(driver).tap(x=950, y=990).release().perform()
            count = driver.find_element_by_class_name("android.widget.EditText")
            count.clear()
            count.send_keys("apollo_hmi")
        # 密码输入『holygogo』
        password = driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='登录百度帐号']/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.widget.EditText")
        password.send_keys("holygogo")
        # 点击登录
        login_btn = driver.find_element_by_accessibility_id("登 录")
        TouchAction(driver).tap(login_btn).release().perform()

        # 进入主页后，点击左侧『消息』按钮
        driver.implicitly_wait(15)
        page.msg_btn.click()

        # 点击"故障"
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[2]").click()
        # 点击"消息"
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[3]").click()
        # 点击收起按钮，收起消息框
        driver.find_element_by_id("com.baidu.adu.hmi.pilotpanel:id/notify_closed_btn").click()

        # 点击『任务』按钮，展开任务消息页
        driver.find_element_by_id("com.baidu.adu.hmi.pilotpanel:id/tv_dv_task_tab").click()
        # 再次点击，关闭
        driver.find_element_by_id("com.baidu.adu.hmi.pilotpanel:id/tv_dv_task_tab").click()

        # 点击视图
        page.map_view.click()
        # 切换俯视视图
        driver.find_element_by_xpath("//android.widget.TextView[2]").click()
        # 切换地图视图
        page.map_view.click()
        driver.find_element_by_xpath("//android.widget.TextView[3]").click()
        # 切换默认视图
        page.map_view.click()
        driver.find_element_by_xpath("//android.widget.TextView[1]").click()

        # 查看排班
        page.schedule_btn.click()
        # 筛选最近3天
        driver.find_element_by_accessibility_id("最近三天").click()
        sleep(2)
        # 筛选本车
        driver.find_element_by_accessibility_id("只看本车").click()
        sleep(2)
        # 筛选本人
        driver.find_element_by_accessibility_id("只看本人").click()
        sleep(2)
        # 筛选今日
        driver.find_element_by_accessibility_id("今天").click()
        sleep(2)
        # 自定义查看起止日期
        driver.find_element_by_xpath("//android.widget.EditText[contains(@text,'开始时间')]").click()
        # 选择日期
        # TouchAction(driver).tap(x=755, y=715).perform()
        # TouchAction(driver).tap(x=945, y=715).perform()
        # driver.find_element_by_xpath("//android.view.View[@content-desc='22']").click()
        # driver.find_element_by_xpath("//android.view.View[@content-desc='27']").click()
        # 确认
        driver.find_element_by_accessibility_id("确认").click()
        # 点击刷新
        driver.find_element_by_accessibility_id("javascript:;").click()
        # 返回首页
        driver.find_element_by_class_name("android.widget.Button").click()

        # 系统设置
        driver.implicitly_wait(15)
        driver.find_element_by_id("com.baidu.adu.hmi.pilotpanel:id/btn_system").click()
        # 关机
        driver.find_element_by_id("com.baidu.adu.hmi.pilotpanel:id/content").click()
        # 取消
        driver.find_element_by_id("com.baidu.adu.hmi.pilotpanel:id/md_buttonDefaultNegative").click()
        # 重启
        driver.find_element_by_id("com.baidu.adu.hmi.pilotpanel:id/btn_system").click()
        driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '重启')]").click()
        # 确认重启
        driver.find_element_by_id("com.baidu.adu.hmi.pilotpanel:id/md_buttonDefaultPositive").click()




if __name__ == '__main__':
    unittest.main()