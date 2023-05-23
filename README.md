# Virtual Pet Bot


เป็นโปรแกรมที่เขียนด้วยภาษา python


## Table of content

- [Getting started](#getting-started)
- [Features](#features)
- [Commands](#commands)


## Getting started

### Installation

``` bash
git  clone  https://github.com/DRepresser/CSS131-PetBot-project.git

cd  CSS131-PetBot-project

pip  install  -r  requirements.txt
```

### Setup Discord bot

1. ไปที่ user setting ของ discord เลือกไปที่ Advanced แล้วเปิด Developer Mode

<img src="https://lh3.google.com/u/1/d/1CnBgky18wUVS9oFgT4xzNz0hzGi84nZh=w1879-h1008-iv2" width="80%">

2. กดไปที่ Discord API แล้วเข้าไปที่ Applications

<img src="https://lh3.google.com/u/1/d/1yKBpciZl91Xu0_TFq8XLb68F0n34oj95=w1879-h1008-iv1" width="50%">

3. กด New Application

<img src="https://lh3.google.com/u/1/d/12a98D99jWXDHyhaR-AC-KCiKIDwL9QHR=w1879-h1008-iv1" width="50%">

<img src="https://lh3.google.com/u/1/d/1Xj6XY1fyYwNc0-VkRXFJyTnQotXJkgin=w1879-h1008-iv1" width="100%">

4. ไปที่ OAuth2 URL Generator เลือก SCOPES เป็น bot และ BOT PERMISSIONS ตามภาพ

<img src="https://lh3.google.com/u/1/d/18ZwpExU-tTVo_FDF4vLInTgJkDmZTr9S=w1879-h1008-iv1" width="100%">

5. คัดลอก URL จาก GENERATED URL ไปวางในบราวเซอร์แล้วเลือก server ที่จะเพิ่มบอทเข้าไป

<img src="https://lh3.google.com/u/1/d/17vqGXMlMmg2wqHUj7Qml9o3ZQLEthRcB=w1879-h1008-iv1" width="50%">

6. ไปที่ Bot แล้วกด Reset Token จากนั้น Copy ไปวางในคำสั่ง

<img src="https://lh3.google.com/u/1/d/1cigYuhKQJ8SiBYyMQH-Le_3cA7NZDgDx=w1879-h1008-iv1" width="50%">

``` bash
echo "DISCORD_TOKEN = 'INSERT_YOUR_TOKEN_HERE'" > .env
```

### Starting the application

``` bash
python run.py
```


## Commands & Features

- [Create](#create)
- [Status](#status)
- [Balance](#balance)
- [Shop](#shop)
- [Feed](#feed)
- [Play](#play)
- [Study](#study)

- [Release](#release)

### create

สร้างสัตว์เลี้ยงจากชื่อและสปีชีส์

`!create PET_NAME PET_SPECIES`

**species** จะมีทั้งหมด 3 ชนิด ได้แก่ **Crow** (กา), **Pot** (หม้อ), **Manotham** (คน)

<img src="https://lh3.google.com/u/1/d/1J6x0WvwnE3pgqgtjsbltHVzugK6O0BqX=w1879-h1008-iv1" width="34%">  <img src="https://lh3.google.com/u/1/d/1nIdeLThf6g81c2ILfV5YHx0QN723nFYe=w1879-h1008-iv1" width="25%">  <img src="https://lh3.google.com/u/1/d/1hyqAV4x4bVPpNl1W8tM9hdiNbeLENw_H=w1879-h1008-iv1" width="20%">

### Status

ตรวจสอบค่าสถานะของสัตว์เลี้ยง

`!status`

<img src="https://lh3.google.com/u/1/d/1E6CNcDzoPYuPwZWOh9eWbbT3z9yoz88_=w1879-h1008-iv1" width="27%">

ค่าสถานะที่ระบุจะมี **Species**, **Hunger**, **Energy**, **Mood**, **Age** และ **Birthdate**

ซึ่ง **Hunger**, **Energy** และ **Mood** จะมึค่าเริ่มต้นอยู่ที่ 50

### Balance

ตรวจสอบจำนวน **Credit** ของตัวเอง

`!balance`

จำนวน **credit เริ่มต้นคือ 100**

### Shop

เปิดร้านค้าประจำวัน ขายอาหารสัตว์เลี้ยงหลายชนิด สินค้าจะถูกเปลี่ยนในทุก ๆ วัน

`!shop`

### Feed

ให้อาหารสัตว์เลี้ยง โดยอาหารที่จะให้ได้จะดูได้จากร้านค้ารายวัน

`!feed ITEM_NAME`

หาก **hunger ของสัตว์เลี้ยงมากกว่า 90** จะไม่สามารถให้อาหารเพิ่มได้อีก

### Play

จ่าย **40 credit** เพื่อเล่นกับสัตว์เลี้ยงของคุณ

`!play`

คุณจะไม่สามารถเล่นกับสัตว์เลี้ยงได่ถ้าหาก **energy ของสัตว์เลี้ยงน้อยกว่า 30**

### Study

ตั้งใจเรียนเพื่อรับ **credit**

`!study TIME_IN_HOUR`

คุณจะได้รับ **70 credit ต่อ 1 ชั่วโมง**

### Release

ปล่อยสัตว์เลี้ยงคืนสู่ป่า

`!release`
