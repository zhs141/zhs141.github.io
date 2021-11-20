#该程序只能适用于qpython 0H中！
import qpy
import androidhelper
import urllib.request as ur
from qsl4ahelper.fullscreenwrapper2 import *

droid = androidhelper.Android()

class MainScreen(Layout):
    def __init__(self):
        super(MainScreen,self).__init__(str("""<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
	android:layout_width="fill_parent"
	android:layout_height="fill_parent"
	android:background="#ff0E4200"
	android:orientation="vertical"
	xmlns:android="http://schemas.android.com/apk/res/android">
	
	<LinearLayout
		android:layout_width="fill_parent"
		android:layout_height="0px"
		android:orientation="horizontal"
		android:layout_weight="20">

		<TextView
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:textSize="15dp"
			android:text="clipboard修改"
			android:textColor="#ffffffff"
			android:layout_weight="1"
			android:gravity="center"
		/>
    </LinearLayout>

	<ListView
		android:id="@+id/data_list"
		android:layout_width="fill_parent"
		android:layout_height="0px"
		android:layout_weight="55"/>

	<LinearLayout
		android:layout_width="fill_parent"
		android:layout_height="0px"
		android:orientation="horizontal"
		android:layout_weight="8">
		<Button
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:text="Writer's URL"
			android:id="@+id/but_ex"
			android:textSize="5dp"
			android:background="#ffEFC802"
			android:textColor="#ffffffff"
			android:layout_weight="1"
			android:gravity="center"/>
		<Button
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:text="退出"
			android:id="@+id/but_exit"
			android:textSize="10dp"
			android:background="#ff06AF00"
			android:textColor="#ffffffff"
			android:layout_weight="1"
			android:gravity="center"/>
		<Button
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:text="剪切板内容\n修改"
			android:id="@+id/but_ow"
			android:textSize="5dp"
			android:background="#ffEFC803"
			android:textColor="#ffffffff"
			android:layout_weight="1"
			android:gravity="center"/>

	</LinearLayout>
</LinearLayout>
<h1>Python yyds!</h1>
"""),"SL4AApp")

    def on_show(self):
        self.views.but_exit.add_event(click_EventHandler(self.views.but_exit, self.exit))
        self.views.but_ex.add_event(click_EventHandler(self.views.but_ex, self.ex))
        self.views.but_ow.add_event(click_EventHandler(self.views.but_ow, self.ow))

        pass

    def on_close(self):
        pass

    def exit(self, view, dummy):
        droid = FullScreenWrapper2App.get_android_instance()
        droid.makeToast("退出")
        FullScreenWrapper2App.close_layout()
        
    def ow(self, view, dummy):
        droid = FullScreenWrapper2App.get_android_instance()
        message = droid.dialogGetInput('TTS', '你想把什么放入剪切板?').result
        if message == None:
            abcdefghijklmnopqrstuvwxyz = 1
        else:
            droid.setClipboard(message)
            droid.makeToast("已将\'" + message + "\'放入剪切板")

    def ex(self, view, dummy):
        droid = FullScreenWrapper2App.get_android_instance()
        droid.makeToast("https://zhs141.github.io\n      (已放入剪切板！)")
        droid.setClipboard("https://zhs141.github.io")

if __name__ == '__main__':
    FullScreenWrapper2App.initialize(droid)
    FullScreenWrapper2App.show_layout(MainScreen())
    FullScreenWrapper2App.eventloop()

print('>>>版权信息：©2021 zhs141.github.io<<<')
