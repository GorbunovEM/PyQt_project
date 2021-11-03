from bs4 import BeautifulSoup
import requests

def get_data_from_page(cad_numb):

    response = requests.get('https://rosreestrgov.ru/object/'+cad_numb.replace(':', '-'))
    soup = BeautifulSoup(response.text, 'lxml')

    lists = []
    quotes = soup.find_all('div', class_='object__table-td')
    for quote in quotes:
        lists.append(quote.text)


    adress_full = lists[(int(lists.index('Адрес полный:'))+1)]
    type = lists[(int(lists.index('Тип:'))+1)]
    area = str(lists[(int(lists.index('Площадь:'))+1)]).replace(".",",")
    floor = lists[(int(lists.index('Этаж:'))+1)]
    form_ownership = lists[(int(lists.index('Форма собственности:'))+1)]
    date_register = lists[(int(lists.index('Для постановки на учёт:'))+1)]
    cad_price = str(lists[(int(lists.index('Кадастровая стоимость:'))+1)]).replace(".",",")
    price_determine = lists[(int(lists.index('Дата определения стоимости:'))+1)]
    price_base = lists[(int(lists.index('Дата внесения стоимости в базу:'))+1)]
    category_land = lists[(int(lists.index('Категория земели:'))+1)]

    return  [adress_full, type, area, floor, form_ownership, date_register, cad_price, price_determine, price_base, category_land]


