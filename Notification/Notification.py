from win10toast import ToastNotifier
import time
toaster = ToastNotifier()
toaster.show_toast("I am reza latifi",
                   "I am python Developer",
                   icon_path=None,
                   duration=5)


toaster.show_toast("Good morning Dear",
                   "How are you today?",
                   icon_path=None,
                   duration=5,
                   threaded=True)

# Wait for threaded notification to finish
while toaster.notification_active(): 
    time.sleep(0.1)
