from selenium import webdriver
import time
import random


browser = webdriver.Chrome()
browser.get('https://docs.google.com/forms/d/e/1FAIpQLSe_L0RlbG9Ag2Qhl3IaM1lal_pz3RrHi1DLlVBBbgQWUfcwRA/viewform')


def click_next(token):
    click = browser.find_element("xpath", token)
    click.click()

def click(a, b, c, d, f, n):
    token = ''
    rd = random.randint(0, n)

    if rd == 0:
        token = a
    elif rd == 1:
        token = b
    elif rd == 2:
        token = c
    elif rd == 3:
        token = d
    else:
        token = f

    click =browser.find_element("xpath", token)
    click.click()

def sex():
    mem = '//*[@id="i5"]/div[3]/div'
    women = '//*[@id="i8"]/div[3]/div'

    click(mem, women, '', '', '', 1)

def old():
    le30 = '//*[@id="i15"]/div[3]/div'
    fr30to40 = '//*[@id="i18"]/div[3]/div'
    fr40to50 = '//*[@id="i21"]/div[3]/div'
    mo50 = '//*[@id="i24"]/div[3]/div'

    click(fr30to40, fr40to50, '', '', '', 1)


def lever():
    inter = '//*[@id="i31"]/div[3]/div'
    coll  = '//*[@id="i34"]/div[3]/div'
    af_coll = '//*[@id="i37"]/div[3]/div'

    click(inter, coll, '', '', '', 1)

def position():
    doc = '//*[@id="i47"]/div[3]/div'
    nur ='//*[@id="i50"]/div[3]/div'
    phar = '//*[@id="i53"]/div[3]/div'

    click( nur, '', '', '', '', 0)

def years():
    le1y = '//*[@id="i63"]/div[3]/div'
    fr1t5y = '//*[@id="i66"]/div[3]/div'
    fr5t10y = '//*[@id="i69"]/div[3]/div'
    mo10y = '//*[@id="i72"]/div[3]/div'

    click(fr1t5y, fr5t10y, '', '', '', 1)

def salary():
    le6mi ='//*[@id="i79"]/div[3]/div'
    fr6t8mi =' //*[@id="i82"]/div[3]/div'
    fr8t10mi ='//*[@id="i85"]/div[3]/div'
    mo10mi = '//*[@id="i88"]/div[3]/div'

    click( fr6t8mi, fr8t10mi, mo10mi, '', '', 2)

def qiz_1():
    modegre = '//*[@id="i5"]/div[3]/div'
    degre = '//*[@id="i8"]/div[3]/div'
    leagre = '//*[@id="i11"]/div[3]/div'
    agre = '//*[@id="i14"]/div[3]/div'
    moagre = '//*[@id="i17"]/div[3]/div'

    click(modegre, degre, leagre, agre, moagre, 4)

def qiz_2():
    modegre = '//*[@id="i24"]/div[3]/div'
    degre = '//*[@id="i27"]/div[3]/div'
    leagre = '//*[@id="i30"]/div[3]/div'
    agre = '//*[@id="i33"]/div[3]/div'
    moagre = '//*[@id="i36"]/div[3]/div'

    click(modegre, degre, leagre, agre, moagre, 4)

def qiz_3():
    modegre = '//*[@id="i43"]/div[3]/div'
    degre = '//*[@id="i46"]/div[3]/div'
    leagre = '//*[@id="i49"]/div[3]/div'
    agre = '//*[@id="i52"]/div[3]/div'
    moagre = '//*[@id="i55"]/div[3]/div'

    click(modegre, degre, leagre, agre, moagre, 4)

def qiz_4():
    modegre = '//*[@id="i62"]/div[3]/div'
    degre = '//*[@id="i65"]/div[3]/div'
    leagre = '//*[@id="i68"]/div[3]/div'
    agre = '//*[@id="i71"]/div[3]/div'
    moagre = '//*[@id="i74"]/div[3]/div'

    click(modegre, degre, leagre, agre, moagre, 4)

def qiz_5():
    modegre = '//*[@id="i81"]/div[3]/div'
    degre = '//*[@id="i84"]/div[3]/div'
    leagre = '//*[@id="i87"]/div[3]/div'
    agre = '//*[@id="i90"]/div[3]/div'
    moagre = '//*[@id="i93"]/div[3]/div'

    click(modegre, degre, leagre, agre, moagre, 4)

def qiz_6():
    modegre = '//*[@id="i100"]/div[3]/div'
    degre = '//*[@id="i103"]/div[3]/div'
    leagre = '//*[@id="i106"]/div[3]/div'
    agre = '//*[@id="i109"]/div[3]/div'
    moagre = '//*[@id="i112"]/div[3]/div'

    click(modegre, degre, leagre, agre, moagre, 4)


def page2():
    sex()
    old()
    lever()
    position()
    years()
    salary()

    #page 2
    str_next = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span'
    click_next(str_next)

def page4():    
    qiz_1()
    qiz_2()
    qiz_3()
    qiz_4()
    qiz_5()
    qiz_6()

    #page 4
    str_next = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span'
    click_next(str_next)

def page5():    
    qiz_1()
    qiz_2()
    qiz_3()
    qiz_4()
    qiz_5()
    qiz_6()

    #page 5
    str_next = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span'
    click_next(str_next)

def page6():    
    qiz_1()
    qiz_2()
    qiz_3()
    qiz_4()
    qiz_5()

    #page 6
    str_next = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span'
    click_next(str_next)

def page7():    
    qiz_1()
    qiz_2()
    qiz_3()
    qiz_4()

    #page 7
    str_next = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span'
    click_next(str_next)

def page8():    
    qiz_1()
    qiz_2()
    qiz_3()
    qiz_4()
    qiz_5()

    #page 8
    str_next = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span'
    click_next(str_next)

def page9():    
    qiz_1()
    qiz_2()
    qiz_3()
    qiz_4()
    qiz_5()
    qiz_6()

    #page 5
    str_next = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span'
    click_next(str_next)

def main():
    for i in range(5):
        print(i)
        #page 1
        str_next = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span'
        click_next(str_next)
        time.sleep(2)

        page2()

        #page 3
        str_next = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span'
        click_next(str_next)

        page4()
        page5()
        page6()
        page7()
        page8()
        page9()
        browser.get('https://docs.google.com/forms/d/e/1FAIpQLSe_L0RlbG9Ag2Qhl3IaM1lal_pz3RrHi1DLlVBBbgQWUfcwRA/viewform')


if __name__=="__main__":
    main()