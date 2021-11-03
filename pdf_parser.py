import pdfplumber



def pdf_MO(path):

    with pdfplumber.open(path) as pdf:
        list_page = []
        for page in pdf.pages:
            extract_text = page.extract_text()
            if 'раздела 1' or "раздела 2" or "Кадастровый номер:" in extract_text:
                list_page.append(page.page_number)

        numb_pages = len(list_page)
        extract_table = []
        for numb_page in range(numb_pages):
            page = pdf.pages[numb_page]
            extract_table.append(page.extract_tables())


    sum_extract = sum(extract_table, [])
    sum_extract_next = sum(sum_extract, [])


    #2
    try:
        obj_name_2 = sum_extract_next[0][0]
    except:
        obj_name_2 = "Нет данных"
    #3
    try:
        if not list(filter(lambda x: 'Местоположение:' in x, sum_extract_next)):
            retrieved_elements_3 = list(filter(lambda x: 'Адрес:' in x, sum_extract_next))
            adress_name_3 = retrieved_elements_3[0][1]
        else:
            retrieved_elements_3 = list(filter(lambda x: 'Местоположение:' in x, sum_extract_next))
            adress_name_3 = retrieved_elements_3[0][1]
    except:
        adress_name_3 = "Нет данных"

    #4
    try:
        retrieved_elements_4 = list(filter(lambda x: 'Площадь:' in x, sum_extract_next))
        area_4 = (retrieved_elements_4[0][1]).replace('.', ',')
    except:
        area_4 = "Нет данных"

    #5
    try:
        retrieved_elements_5 = list(filter(lambda x: 'Кадастровый номер:' in x, sum_extract_next))
        cad_numb_5 = retrieved_elements_5[0][1]
    except:
        cad_numb_5 = "Нет данных"
    #6
    try:
        holder_name_6_holder = []
        holder_name_6 = []
        n = 0
        i = 0
        for element in sum_extract_next:
            if 'Правообладатель (правообладатели):' in element:
                n += 1
                if len(element) == 5:
                    holder_name_6_holder.append(f"{n}. {element[4]}")
                elif len(element) == 4:
                    holder_name_6_holder.append(f"{n}. {element[3]}")

        for element in sum_extract_next:
            if 'Вид, номер и дата государственной регистрации права:' in element or 'Вид, номер, дата и время государственной регистрации\nправа:' in element:
                if len(element) == 5:
                    holder_name_6.append(holder_name_6_holder[i] + " " + element[4])
                elif len(element) == 4:
                    holder_name_6.append(holder_name_6_holder[i] + " " + element[3])
                i += 1
        if not holder_name_6:
            holder_name_6 = "Данные о правообладателе отсутствуют"
    except:
        holder_name_6 = "Данные о правообладателе отсутствуют"

    #7
    right_numb_7 = []
    n = 0
    try:
        for names in holder_name_6[0::1]:
            n += 1
            right_numb_7.append(f"{n}. {list(names.split(chr(10)))[1]}")
    except:
        right_numb_7 = "Данные о правообладателе отсутствуют"

    #8
    right_date_8 = []
    n = 0
    try:
        for names in holder_name_6[0::1]:
            n += 1
            right_date_8.append(f"{n}. {list(names.split(chr(10)))[2]}")
    except:
        right_date_8 = "Данные о правообладателе отсутствуют"

    #9
    docs_regster_9 = "-"
    #10
    actual_egrn_10 = "-"
    #11
    try:
        retrieved_elements_11 = list(filter(lambda x: 'Сведения об осуществлении государственной\nрегистрации сделки, права без необходимого в силу\nзакона согласия третьего лица, органа:' in x, sum_extract_next))
        docs_fundamental_11 = retrieved_elements_11[0][4]
    except:
        docs_fundamental_11 = "Данные о правообладателе отсутствуют"

    #12
    vri_12 = "-"
    #13
    try:
        retrieved_elements_13 = list(filter(lambda x: 'Виды разрешенного использования:' in x, sum_extract_next))
        vri_by_document_13 = retrieved_elements_13[0][1]
    except:
        vri_by_document_13 = "Нет данных"
    #14
    try:
        retrieved_elements_14 = list(filter(lambda x: 'Категория земель:' in x, sum_extract_next))
        category_zu_14 = retrieved_elements_14[0][1]
    except:
        category_zu_14 = "Нет данных"

    #15
    try:
        term_restrict_15 = []
        n = 0
        for element in sum_extract_next:
            if 'срок, на который установлено ограничение прав и\nобременение объекта недвижимости:' in element:
                if len(element) == 5:
                    n += 1
                    term_restrict_15.append(f"{n}. {element[3]}")
                elif len(element) == 2:
                    n += 1
                    term_restrict_15.append(f"{n}. {element[1]}")
                elif len(element) == 4:
                    n += 1
                    term_restrict_15.append(f"{n}. {element[3]}")
        if not term_restrict_15:
            term_restrict_15 = "Нет данных"
    except:
        term_restrict_15 = "Нет данных"
    #16
    try:
        numb_res_16 = []
        n = 0
        for element in sum_extract_next:
            if 'вид:' in element:
                if len(element) == 5:
                    n += 1
                    numb_res_16.append(f"{n}. {element[3]}")
                elif len(element) == 2:
                    n += 1
                    numb_res_16.append(f"{n}. {element[1]}")
                elif len(element) == 4:
                    n += 1
                    numb_res_16.append(f"{n}. {element[3]}")

        if not numb_res_16:
            numb_res_16 = "Нет данных"
    except:
        numb_res_16 = "Нет данных"

    #17
    try:
        whom_rest_17 = []
        n = 0
        for element in sum_extract_next:
            if 'лицо, в пользу которого установлено ограничение\nправ и обременение объекта недвижимости:' in element:
                if len(element) == 5:
                    n += 1
                    whom_rest_17.append(f"{n}. {element[3]}")
                elif len(element) == 2:
                    n += 1
                    whom_rest_17.append(f"{n}. {element[1]}")
                elif len(element) == 4:
                    n += 1
                    whom_rest_17.append(f"{n}. {element[3]}")
        if not whom_rest_17:
            whom_rest_17 = "Нет данных"
    except:
        whom_rest_17 = "Нет данных"

    #18
    try:
        retrieved_elements_18 = list(filter(lambda x: 'Статус записи об объекте недвижимости:' in x, sum_extract_next))
        status_18 = retrieved_elements_18[0][1]
    except:
        status_18 = "Нет данных"

    #19
    try:
        retrieved_elements_19 = list(filter(lambda x: 'Особые отметки:' in x, sum_extract_next))
        special_19 = retrieved_elements_19[0][1]
    except:
        special_19 = "Нет данных"

    #20
    try:
        if obj_name_2 == "Земельный участок":
            type_20 = "Земельный участок"
        else:
            retrieved_elements_20 = list(filter(lambda x: 'Наименование:' in x, sum_extract_next))
            type_20 = retrieved_elements_20[0][1]
    except:
        type_20 = "Нет данных"
    #21
    try:
        if obj_name_2 == "Земельный участок":
            retrieved_elements_21 = list(filter(lambda x: 'Кадастровые номера расположенных в пределах земельного\nучастка объектов недвижимости:' in x,sum_extract_next))
            cad_links_21 = retrieved_elements_21[0][1]
        else:
            retrieved_elements_21 = list(filter(lambda x: 'Кадастровые номера иных объектов недвижимости, в пределах\nкоторых расположен объект недвижимости:' in x, sum_extract_next))
            cad_links_21 = retrieved_elements_21[0][1]
    except:
        cad_links_21 = "Нет данных"
    #22
    try:
        retrieved_elements_22 = list(filter(lambda x: 'Кадастровая стоимость, руб.:' in x, sum_extract_next))
        cad_price_22 = (retrieved_elements_22[0][1]).replace('.', ',')
    except:
        cad_price_22 = "Нет данных"

    holder_name_6_fixed = []
    for count in range(len(holder_name_6)):
        holder_name_6_fixed.append(holder_name_6[count].replace(chr(10), """ """))

    return [obj_name_2, adress_name_3, area_4, cad_numb_5, holder_name_6_fixed, right_numb_7, right_date_8,
    docs_regster_9, actual_egrn_10, docs_fundamental_11, vri_12, vri_by_document_13, category_zu_14, term_restrict_15,
    numb_res_16, whom_rest_17, status_18, special_19, type_20, cad_links_21, cad_price_22]



