# 💀 Bad Discord Nuker 💀


<p align="center">
 <img src="https://img.shields.io/github/last-commit/Bad-Discord/Discord-Nuker?color=blue&style=flat-square" </a>
 <img src="https://img.shields.io/github/stars/Bad-Discord/Discord-Nuker?color=blue&label=Stars&style=flat-square" </a>
 <img src="https://img.shields.io/github/forks/Bad-Discord/Discord-Nuker?color=blue&label=Forks&style=flat-square" </a>
</p>

<p align="center">
[<a href="https://github.com/Bad-Discord/Discord-Nuker/#installation"> How to install</a> ] - 
[<a href="https://github.com/Bad-Discord/Discord-Nuker/#Screenshots"> Screenshots</a> ]

</p>

### *قابلیت ها :*
> - [x] *اسپم در تمامی چنل ها*
> - [x] *دیلیت دادن تمامی رول ها*
> - [x] *عوض کردن اسم تمامی رول ها*
> - [x] *دیلیت دادن تمامی چنل ها*
> - [x] *عوض کردن اسم تمامی چنل ها*
> - [x] *دیلیت دادن تمامی اموجی ها*
> - [x] *ساخت تعداد بسیاری چنل*
> - [x] *بن کردن تمامی ممبر ها*
> - [x] *اسپم با وبهوک*
> - [x] *اسپم با بات*
> - [x] *دایرکت دادن به همه*
> - [x] *عوض کردن نیک نیم همه*
> - [x] *عوض کردن عکس سرور*
> - [x] *عوض کردن اسم سرور*
> - [x] *دور زدن بات های امنیتی*
> - [x] *پشتیبانی از پراکسی*
> - [x] *پشتیبانی از سشن*
## ⚗ Installation

- اطمینان حاصل کنید که پایتون رو روی پیسی تون نصب کردید. 
- [Python3.7.12](https://www.python.org/downloads/release/python-3712/) یا ورژن های بعد تر (بجز [Python3.12.0](https://www.python.org/downloads/release/python-3120/) چون اشغاله)


### ویندوز: 
- روی دکمه ی سبز رنگ Code کلیک کنید و روی Download ZIP بزنید تا فایل زیپ رو دانلود کنید
- فایل زیپ رو استخراج کنید و واردش بشید
- توی فولدر فایل ها ، یک ترمینال باز کنید و کامند زیری رو توش پیست کنید:
```bash
pip install -r requirements.txt; python main.python
``` 
- **یا** فقط فایل `main.py` رو باز کنید و بذارید خودش پیش نیاز هاشو نصب کنه 


### ترموکس
- کامند یک خطی برای نصب در ترموکس:
```shell
pkg update -y && pkg upgrade -y && pkg install python git && git clone https://github.com/Bad-Discord/Discord-Nuker && cd Discord-Nuker && pip install -r requirements.txt && python main.py
```
- فقط کافیه که کپیش کنید و توی ترمینال ترموکس پیست کنید



## 🤔 استفاده

### استفاده معمولی
- از `python main.py` استفاده کنید یا با دابل کلیک فایل رو باز کنید

### استفاده از سشن

 - یک [سشن فایل](https://github.com/Bad-Discord/Discord-Nuker/persian_docs/#سشن-ها) بسازید و بعد از `python main.py <سشن شما>` استفاده کنید

```bash
python main.py session.json
```


## سشن ها
### سشن چیست؟?
در صورتی که بسیار تنبل هستید تا همان توکن بات معمولی خودتون رو هرسری توی سورس کد ما وارد کنید میتونید از سشن فایل ها استفاده کنید تا یکسری اطلاعات از پیش تعیین شده رو عین توکن توی سورستون استفاده کنید. 

- یک فایل با فورمت `.json` توی فولدر اصلی بسازید و کد زیر رو توش پیست کنید

```json
{
    "Token": "توکن شما ",
    "SpamTexts": ["چند تکست", "برای اسپم"],
    "SpamAmount": 50,
    "ServerName": "اقو لاجیک اینجارو ناک کرد پسر",
    "SpamInviteLink": "discord.gg/cool-people"
}
```

`Token`: توکن ربات شما

`Spam Texts`: چند تکست برای فرستادن توی چنل ها و اسپم 

`SpamAmount`: تعداد دفعاتی که قرار است تکست ها اسپم شوند و چنل ها ساخته شوند 

`ServerName`: یک اسم برای تغییر دادن اسم سرور

`SpamInviteLink`: اینوایت لینک سرور شما برای اسپم کردن 

## 📸 اسکرین شات ها

<img src="Screenshots/Screenshot1.png">

## ⚠ Disclaimer

This script is educational and fully coded by M. logique aka @1ogi in discord
if you choose to abuse this tool it's are your fault and M. logique will not accept anything about you're mistake