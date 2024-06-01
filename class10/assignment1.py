class Device:
    brand = "ABC"
    model = "1"

class OperatingSystem:
    os_name = "Android"
    version = "11"

class Smartphone(Device):
    battery_capacity = 4000

class AndroidOS(OperatingSystem):
    google_services = "enabled"

class iOS(OperatingSystem):
    app_store = "enabled"

class AndroidSmartphone(Smartphone, AndroidOS):
    brand = "Samsung"
    model = "Galaxy S21"
    os_name = "Android"
    version = 11
    battery_capacity = 4000
    google_services = "Enabled"

    def details(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"OS Name : {self.os_name}")
        print(f"Version : {self.version}")
        print(f"Battery Capacity : {self.battery_capacity} mAh")
        print(f"Google Services : {self.google_services}")

class iPhone(Smartphone, iOS):
    brand = "Apple"
    model = "iPhone 12"
    os_name = "iOS"
    version = 14
    battery_capacity = 2815
    app_store = "enabled"

    def details(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"OS Name : {self.os_name}")
        print(f"Version : {self.version}")
        print(f"Battery Capacity : {self.battery_capacity} mAh")
        print(f"App Store : {self.app_store}")

# Usage
android_smartphone = AndroidSmartphone()
iphone = iPhone()

android_smartphone.details()
# Output:
# Brand : Samsung
# Model : Galaxy S21
# OS Name : Android
# Version : 11
# Battery Capacity : 4000 mAh
# Google Services : Enabled

iphone.details()
# Output:
# Brand : Apple
# Model : iPhone 12
# OS Name : iOS
# Version : 14
# Battery Capacity : 2815 mAh
# App Store : enabled
