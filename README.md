# IOT_Project: 人體監測系統
由人體紅外線感測器感測人體方向，再由step motor帶著相機轉至偵測方向並進行拍攝，並可於網頁上看到目前鏡頭畫面。<br /><br />
Input：人體紅外線感測器。<br />
Output：鏡頭畫面顯示於網頁、拍攝照片存於本機。<br />
Video Demo: https://drive.google.com/open?id=1eMStMv6OOEz_Fmdua6y77xWdLzWBTzqE <br /><br />
所需材料：<br />
樹莓派 * 1 <br />
麵包板 * 1 <br />
鏡頭 * 1 <br />
人體紅外線感測器 * 6 <br />
步進馬達 * 1 <br />
杜邦線 約80條 <br />
筷子一雙 <br />
雙面膠 * 1 <br />
泡綿膠 * 1

# 步驟一：安裝Node.js 
參考教學：https://www.w3schools.com/nodejs/nodejs_raspberrypi.asp <br /> 
Update your system package list: <br />
`pi@w3demopi:~ $ sudo apt-get update` <br />
Upgrade all your installed packages to their latest version: <br />
`pi@w3demopi:~ $ sudo apt-get dist-upgrade` <br />
Doing this regularly will keep your Raspberry Pi installation up to date.<br />
To download and install newest version of Node.js, use the following command: <br />
`pi@w3demopi:~ $ curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -` <br />
Now install it by running: <br />
`pi@w3demopi:~ $ sudo apt-get install -y nodejs` <br />
Check that the installation was successful, and the version number of Node.js with: <br />
`pi@w3demopi:~ $ node -v`

# 步驟二：建立於網頁上監控鏡頭畫面的Server端檔案 
參考教學：http://thejackalofjavascript.com/rpi-live-streaming/ <br />
在Terminal中run <br />
`mkdir node_programs` <br />
To step inside that folder, run <br />
`cd node_programs` <br />
For this post, we will create a new folder named liveStreaming and will step inside this folder. Run <br />
`mkdir liveStreaming && cd liveStreaming` <br />
First we will initialize a new node project here. Run <br />
`npm init` <br />
Fill it up as applicable. <br />
Now, we will install express and socket.io modules on our pi. Run <br />
`npm install express socket.io --save` <br />
Once they are installed, create a new file named index.js. <br />
於index.js中拷入index.js的程式碼 <br />
Now we will create a new folder named stream at the root of the liveStreaming folder. This is where our image will be saved.

# 步驟三：建立於網頁上監控鏡頭畫面的Client端檔案
參考教學：http://thejackalofjavascript.com/rpi-live-streaming/ <br />
在livestreaming資料夾中建立index.html檔 <br />
於index.html中拷入index.html的程式碼 <br /> 
程式碼完成後，即可執行 <br />
`node index.js` <br />
執行後，於瀏覽器網址列輸入自己的IP位址＋:3000即可看到鏡頭的畫面 <br />
`http://Your_IP_Address:3000` <br />

# 步驟四：接電路與鏡頭
樹莓派GPIO參考：https://pinout.xyz/ <br />
步進馬達使用、連接參考：https://www.youtube.com/watch?v=LUbhPKBL_IU&t=182s <br />
人體感測器連接參考：http://iot.pcsalt.com/detecting-obstacle-with-ir-infrared-sensor-raspberry-pi-3/ <br />
鏡頭連接參考：https://projects.raspberrypi.org/en/projects/getting-started-with-picamera <br />
我們一共會使用樹莓派的10個Pin（BCM制）：<br />
人體感應器使用PIN 5, 6, 13, 19, 26, 21 <br />
馬達使用PIN 4, 17, 27, 22 <br />
接法請參考上述連結

# 步驟五：撰寫人體感測與鏡頭旋轉程式
IR.py檔案即為我們主要邏輯控制的Python檔 <br />
首先載入我們所需的套件與設定GPIO的格式 <br />
`from picamera import PiCamera` <br />
`from gpiozero import LED` <br />
`from signal import pause` <br />
`import sys` <br />
`import RPi.GPIO as GPIO` <br />
`import time` <br />
`GPIO.setmode(GPIO.BCM)` <br />
`GPIO.setwarnings(False)` <br /><br />

再來，設定相機、人體感測器、和步進馬達的PIN <br />
`camera = PiCamera()` <br />
`LED_PIN = 12` <br />
`IR_PIN1 = 5 ` <br />
`IR_PIN2 = 6` <br />
`IR_PIN3 = 13` <br />
`IR_PIN4 = 19` <br />
`IR_PIN5 = 26` <br />
`IR_PIN6 = 21` <br />

`ControlPin = [4,17,27,22]` <br />

`for pin in ControlPin:` <br />
 `   GPIO.setup(pin, GPIO.OUT)` <br />
 `   GPIO.output(pin,0)` <br />

`indicator = LED(LED_PIN)` <br />
`GPIO.setup(IR_PIN1, GPIO.IN)` <br />
`GPIO.setup(IR_PIN2, GPIO.IN)` <br />
`GPIO.setup(IR_PIN3, GPIO.IN)` <br />
`GPIO.setup(IR_PIN4, GPIO.IN)` <br />
`GPIO.setup(IR_PIN5, GPIO.IN)` <br />
`GPIO.setup(IR_PIN6, GPIO.IN)` <br />

接著定義步進馬達的旋轉速度與方向<br />
步進馬達的運作模式可參考：https://www.youtube.com/watch?v=LUbhPKBL_IU&t=182s <br />
seq1為順時鐘旋轉、seq2為逆時鐘旋轉<br />
`seq1 = [ [1,0,0,0],` <br />
`       [1,1,0,0],` <br />
`        [0,1,0,0],` <br />
`        [0,1,1,0],` <br />
`        [0,0,1,0],` <br />
`        [0,0,1,1],` <br />
`        [0,0,0,1],` <br />
`        [1,0,0,1]]` <br />

`seq2 = [ [1,0,0,0],` <br />
`        [1,0,0,1],` <br />
`        [0,0,0,1],` <br />
`        [0,0,1,1],` <br />
`        [0,0,1,0],` <br />
`        [0,1,1,0],` <br />
`        [0,1,0,0],` <br />
`        [1,1,0,0]]` <br />

接著定義使步進馬達旋轉的函數<br />
用count作為觀測目前程式跑了多久的指標，以及用current_position紀錄目前步進馬達的位置<br />
`count = 1` <br />
`current_position = 1` <br />

rotate旋轉函數主要判斷<br />
(1) 偵測到的位置在目前位置的相對方向<br />
(2) 偵測到的位置距離目前位置多少個半圈（128）<br />
來決定要用順時鐘旋轉還是逆時針旋轉，以及旋轉多少角度<br />
最後在旋轉完後開啟相機進行拍攝<br />
`def rotate(current, detect):` <br />
`    print(current)` <br />
`    print(detect)` <br />
`    if current == detect:` <br />
`        range_num = 0` <br />
`        seq = seq1` <br />
`    elif current > detect:` <br />
`        seq = seq1` <br />
`        if current - detect == 1:` <br />
`            range_num = 128` <br />
`        elif current - detect == 2:` <br />
`            range_num = 256` <br />
`        elif current - detect == 3:` <br />
`            range_num = 384` <br />
`        elif current - detect == 4:` <br />
`            range_num = 512` <br />
`        elif current - detect == 6:` <br />
`            range_num = 640` <br />
`    elif current < detect:` <br />
`        seq = seq2` <br />
`        if detect - current == 1:` <br />
`            range_num = 128` <br />
`        elif detect - current == 2:` <br />
`            range_num = 256` <br />
`        elif detect - current == 3:` <br />
`            range_num = 384` <br />
`        elif detect - current == 4:` <br />
`            range_num = 512` <br />
`        elif detect - current == 5:` <br />
`            range_num = 640` <br />
`    for i in range(range_num):` <br />
`        for halfstep in range(8):` <br />
`            for pin in range(4):` <br />
`                GPIO.output(ControlPin[pin], seq[halfstep][pin])` <br />
`            time.sleep(0.001)` <br />
`    camera.start_preview()` <br />
`    camera.capture('/home/pi/Desktop/image.jpg')` <br />
`    camera.stop_preview()` <br />

最後，開一個無限迴圈進行人體監測，若監測到後輸入監測到的感測器方位執行rotate函數，步進馬達即會旋轉到該方位<br />
`while True:` <br />
`  detect_1 = GPIO.input(IR_PIN1)` <br />
`  detect_2 = GPIO.input(IR_PIN2)` <br />
`  detect_3 = GPIO.input(IR_PIN3)` <br />
`  detect_4 = GPIO.input(IR_PIN4)` <br />
`  detect_5 = GPIO.input(IR_PIN5)` <br />
`  detect_6 = GPIO.input(IR_PIN6)` <br />
`  if detect_1 == False:` <br />
`    print("{:>3} Sensor1 Detected!".format(count))` <br />
`    time.sleep(0.5)` <br />
`    rotate(current_position, 1)` <br />
`    current_position = 1` <br />
`  elif detect_2 == False:` <br />
`    print("{:>3} Sensor2 Detected!".format(count))` <br />
`    rotate(current_position, 2)` <br />
`    time.sleep(0.5)` <br />
`    current_position = 2` <br />
`  elif detect_3 == False:` <br />
`    print("{:>3} Sensor3 Detected!".format(count))` <br />
`    time.sleep(0.5)` <br />
`    rotate(current_position, 3)` <br />
`    current_position = 3` <br />
`  elif detect_4 == False:` <br />
`    print("{:>3} Sensor4 Detected!".format(count))` <br />
`    time.sleep(0.5)` <br />
`    rotate(current_position, 4)` <br />
`    current_position = 4` <br />
`  elif detect_5 == False:` <br />
`    print("{:>3} Sensor5 Detected!".format(count))` <br />
`    time.sleep(0.5)` <br />
`    rotate(current_position, 5)` <br />
`    current_position = 5` <br />
`  elif detect_6 == False:` <br />
`    print("{:>3} Sensor6 Detected!".format(count))` <br />
`    time.sleep(0.5)` <br />
`    rotate(current_position, 6)` <br />
`    current_position = 6` <br />
`  else:` <br />
`    indicator.off()` <br />
`    print("{:>3} Nothing detected".format(count))` <br />
`  count += 1` <br />
`  time.sleep(0.2)  ` <br />
`GPIO.cleanup()` <br />

# 步驟六：固定相機及執行IR.py程式
利用1/4的竹筷利用雙面膠＋泡綿膠固定於步進馬達的轉軸上 <br />
再將相機固定於竹筷上即可使相機隨著步進馬達轉動
最後，再將步進馬達同樣使用雙面膠＋泡綿膠固定於樹莓派的塑膠殼上即可完成本次人體監控系統的專案！
