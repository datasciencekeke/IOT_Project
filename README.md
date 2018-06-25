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






步進馬達使用教學：https://www.youtube.com/watch?v=LUbhPKBL_IU&t=182s
