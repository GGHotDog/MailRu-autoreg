<br/>
<p align="center">
  <img src='https://cdn.icon-icons.com/icons2/2429/PNG/512/mail_ru_logo_icon_147267.png' width=100>
  <h3 align="center">Mail Ru autoreg</h3>

  <p align="center">
    Mail.ru mail autoreg generator
    <br/>
    <br/>
  </p>
</p>



## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Authors](#authors)

## About The Project

This repository is an automatic e-mail generator on the mail.ru platform. It is designed to create random e-mail addresses on mail.ru for various purposes, as well as it bypasses captcha with the help of rucaptcha service.

## Built With

This project is based on the selenium library 

## Getting Started

Basic project assembly

### Prerequisites

To work, we need Python 3 and install dependencies on it:

* selenium

```sh
pip3 install selenium
```
* requests
```sh
pip3 install requests
```

### Installation

1. Create an account at https://rucaptcha.com, top up the balance and release the API key

2. Enter your API key in `src/config.py`
```python
      token = 'ENTER YOUR TOKEN'
```

3. Install the chromedriver of your version https://github.com/jsnjack/chromedriver/releases and put it in the src folder.

4. Run the script with the command ```python3 main.py``` in the ```src``` directory


## Usage

Enter the number of autoregs we need, after the program will appear file ```autoreg[?????].txt```  where will be stored our autoregs in the format ``mail:password``.




### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Authors

* [GGHotDog](https://github.com/GGHotDog)
