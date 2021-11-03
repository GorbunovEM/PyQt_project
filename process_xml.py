from bs4 import BeautifulSoup

def egrn_MO(path):
    with open(path, newline='', encoding="utf-8") as text:
        f = text.read()
        soup = BeautifulSoup(f, "xml")

        if soup.land_record:
            #2
            try:
                obj_name_2 = soup.common_data.type.value.text
            except:
                obj_name_2 = "нет данных"
            #3
            try:
                adress_name_3 = soup.readable_address.text
            except:
                adress_name_3 = "нет данных"
            #4
            try:
                areas = soup.params.area.text.replace('.', ',')
                area_4 = areas.split("\n")[5]
            except:
                area_4 = "нет данных"
            #5
            try:
                cad_numb_5 = soup.common_data.cad_number.text
            except:
                cad_numb_5 = "нет данных"
            #6
            holder_name_6 = []
            holders = soup.find_all("right_record")
            n = 0
            try:
                for holder in holders:
                    n += 1
                    if holder.right_data.share_description:
                        holder_name_6.append(f'{n}. {holder.right_holders.right_holder.text.replace(chr(10), """ """)}, '
                        f'{holder.right_data.right_type.value.text.replace(chr(10), """ """)}, '
                        f'{holder.right_data.share_description.text.replace(chr(10), """ """)}')
                    else:
                        holder_name_6.append(f'{n}. {holder.right_holders.right_holder.text.replace(chr(10), """ """)}'
                                             f'{holder.right_data.right_type.value.text.replace(chr(10), """ """)}')
                if not holder_name_6:
                    holder_name_6 = 'данные о правообладателе отсутствуют'
            except:
                holder_name_6.append('данные о правообладателе отсутствуют')
            #7
            right_numb_7 = []
            register = soup.find_all("right_record")
            n = 0
            try:
                for reg in register:
                    n += 1
                    right_numb_7.append(f'{n}. {reg.right_data.right_number.text.replace(chr(10), """ """)}')
                if not right_numb_7:
                    right_numb_7 = 'данные о правообладателе отсутствуют'
            except:
                right_numb_7.append('данные о правообладателе отсутствуют')
            #8
            right_date_8 = []
            dats = soup.find_all("right_record")
            n = 0
            try:
                for dat in dats:
                    n += 1
                    right_date_8.append(f'{n}. {dat.record_info.registration_date.text.replace(chr(10), """ """)}')
                if not right_date_8:
                    right_date_8 = 'данные о правообладателе отсутствуют'
            except:
                right_date_8.append('данные о правообладателе отсутствуют')
            #9
            docs_regster_9 = "-"
            #10
            actual_egrn_10 = "-"
            #11
            docs_fundamental_11 = "-"
            #12
            vri_12 = "-"
            #13
            try:
                vri_by_document_13 = soup.params.permitted_use.permitted_use_established.by_document.text
            except:
                vri_by_document_13 = "нет данных"
            #14
            try:
                category_zu_14 = soup.params.category.type.value.text
            except:
                category_zu_14 = "нет данных"
            #15
            term_restrict_15 = []
            restriction = soup.find_all("restrict_record")
            n = 0
            try:
                for res in restriction:
                    n += 1
                    term_restrict_15.append(f'{n}. {res.restrictions_encumbrances_data.period.text.replace(chr(10), """ """)}')
                if not term_restrict_15:
                    term_restrict_15 = "данные не зарегистрированы"
            except:
                term_restrict_15.append('период не установлен')
            #16
            numb_res_16 = []
            restriction = soup.find_all("restrict_record")
            n = 0
            try:
                for res in restriction:
                    n += 1
                    numb_res_16.append(f'{n}. {res.restrictions_encumbrances_data.restriction_encumbrance_type.value.text.replace(chr(10), """ """)}')
                if not numb_res_16:
                    numb_res_16 = "данные не зарегистрированы"
            except:
                numb_res_16.append('данные не зарегистрированы')
            #17
            whom_rest_17 = []
            restriction = soup.find_all("restrict_record")
            n = 0
            try:
                for res in restriction:
                    n += 1
                    whom_rest_17.append(f'{n}. {res.right_holders.right_holder.text.replace(chr(10), """ """)}')
                if not whom_rest_17:
                    whom_rest_17 = "данные не зарегистрированы"
            except:
                whom_rest_17.append('данные не зарегистрированы')
            #18
            try:
                status_18 = soup.status.text
            except:
                status_18 = "нет данных"
            #19
            try:
                special_19 = soup.land_record.special_notes.text
            except:
                special_19 = "нет данных"
            #20
            try:
                type_20 = soup.object.common_data.type.value.text
            except:
                type_20 = "нет данных"
            #21
            try:
                cad_links_21 = soup.land_record.cad_links.text.replace(chr(10), """ """)
            except:
                cad_links_21 = "нет данных"
            #22
            try:
                cad_price_22 = soup.land_record.cost.value.text.replace('.', ',')
            except:
                cad_price_22 = "нет данных"
            return [obj_name_2, adress_name_3, area_4, cad_numb_5, holder_name_6, right_numb_7, right_date_8,
                    docs_regster_9, actual_egrn_10, docs_fundamental_11, vri_12, vri_by_document_13, category_zu_14, term_restrict_15,
                    numb_res_16, whom_rest_17, status_18, special_19, type_20, cad_links_21, cad_price_22]

        elif soup.build_record:
            #2
            try:
                obj_name_2 = soup.find("name").text
            except:
                obj_name_2 = "Нежилое здание"
            #3
            try:
                adress_name_3 = soup.readable_address.text
            except:
                adress_name_3 = "нет данных"
            #4
            try:
                area_4 = soup.params.area.text.replace('.', ',')
            except:
                area_4 = "нет данных"
            #5
            try:
                cad_numb_5 = soup.common_data.cad_number.text
            except:
                cad_numb_5 = "нет данных"
            #6
            holder_name_6 = []
            holders = soup.find_all("right_record")
            n = 0
            try:
                for holder in holders:
                    n += 1
                    if holder.right_data.share_description:
                        holder_name_6.append(f'{n}. {holder.right_holders.right_holder.text.replace(chr(10), """ """)}, '
                                             f'{holder.right_data.right_type.value.text.replace(chr(10), """ """)}, '
                                             f'{holder.right_data.share_description.text.replace(chr(10), """ """)}')
                    else:
                        holder_name_6.append(f'{n}. {holder.right_holders.right_holder.text.replace(chr(10), """ """)}, '
                                             f'{holder.right_data.right_type.value.text.replace(chr(10), """ """)}')
                if not holder_name_6:
                    holder_name_6 = 'данные о правообладателе отсутствуют'
            except:
                holder_name_6.append('данные о правообладателе отсутствуют')
            #7
            right_numb_7 = []
            register = soup.find_all("right_record")
            n = 0
            try:
                for reg in register:
                    n += 1
                    right_numb_7.append(f'{n}. {reg.right_data.right_number.text.replace(chr(10), """ """)}'+"\n")
                if not right_numb_7:
                    right_numb_7 = 'данные о правообладателе отсутствуют'
            except:
                right_numb_7.append('данные о правообладателе отсутствуют')
            #8
            right_date_8 = []
            dats = soup.find_all("right_record")
            n = 0
            try:
                for dat in dats:
                    n += 1
                    right_date_8.append(f'{n}. {dat.record_info.registration_date.text.replace(chr(10), """ """)}')
                if not right_date_8:
                    right_date_8 = 'данные о правообладателе отсутствуют'
            except:
                right_date_8.append('данные о правообладателе отсутствуют')
            #9
            docs_regster_9 = "-"
            #10
            actual_egrn_10 = "-"
            #11
            docs_fundamental_11 = "-"
            #12
            vri_12 = "-"
            #13
            vri_by_document_13 = "-"
            #14
            category_zu_14 = "-"
            #15
            term_restrict_15 = []
            restriction = soup.find_all("restrict_record")
            n = 0
            try:
                for res in restriction:
                    n += 1
                    term_restrict_15.append(f'{n}. {res.restrictions_encumbrances_data.period.text.replace(chr(10), """ """)}')
                if not term_restrict_15:
                    term_restrict_15 = "данные не зарегистрированы"
            except:
                term_restrict_15.append('период не установлен')
            #16
            numb_res_16 = []
            restriction = soup.find_all("restrict_record")
            n = 0
            try:
                for res in restriction:
                    n += 1
                    numb_res_16.append(f'{n}. {res.restrictions_encumbrances_data.restriction_encumbrance_type.value.text.replace(chr(10), """ """)}')
                if not numb_res_16:
                    numb_res_16 = "данные не зарегистрированы"
            except:
                numb_res_16.append('данные не зарегистрированы')
            #17
            whom_rest_17 = []
            restriction = soup.find_all("restrict_record")
            n = 0
            try:
                for res in restriction:
                    n += 1
                    whom_rest_17.append(f'{n}. {res.right_holders.right_holder.text.replace(chr(10), """ """)}')
                if not whom_rest_17:
                    whom_rest_17 = "данные не зарегистрированы"
            except:
                whom_rest_17.append('данные не зарегистрированы')
            #18
            try:
                status_18 = soup.status.text
            except:
                status_18 = "нет данных"
            #19
            try:
                special_19 = soup.build_record.special_notes.text
            except:
                special_19 = "нет данных"
            #20
            try:
                type_20 = soup.object.common_data.type.value.text
            except:
                type_20 = "нет данных"
            #21
            try:
                cad_links_21 = soup.cad_links.land_cad_numbers.land_cad_number.cad_number.text.replace(chr(10), """ """)
            except:
                cad_links_21 = "нет данных"
            #22
            try:
                cad_price_22 = soup.build_record.cost.value.text.replace('.', ',')
            except:
                cad_price_22 = "нет данных"

            return [obj_name_2, adress_name_3, area_4, cad_numb_5, holder_name_6, right_numb_7, right_date_8,
                    docs_regster_9, actual_egrn_10, docs_fundamental_11, vri_12, vri_by_document_13, category_zu_14, term_restrict_15,
                    numb_res_16, whom_rest_17, status_18, special_19, type_20, cad_links_21, cad_price_22]

        elif soup.room_record:
            #2
            try:
                obj_name_2 = soup.find("name").text
            except:
                obj_name_2 = "Нежилое помещение"
            #3
            try:
                adress_name_3 = soup.readable_address.text
            except:
                adress_name_3 = "нет данных"
            #4
            try:
                area_4 = soup.params.area.text.replace('.', ',')
            except:
                area_4 = "нет данных"
            #5
            cad_numb_5 = soup.common_data.cad_number.text
            #6
            holder_name_6 = []
            holders = soup.find_all("right_record")
            n = 0
            try:
                for holder in holders:
                    n += 1
                    if holder.right_data.share_description:
                        holder_name_6.append(f'{n}. {holder.right_holders.right_holder.text.replace(chr(10), """ """)}, '
                                             f'{holder.right_data.right_type.value.text.replace(chr(10), """ """)}, '
                                             f'{holder.right_data.share_description.text.replace(chr(10), """ """)}')
                    else:
                        holder_name_6.append(f'{n}. {holder.right_holders.right_holder.text.replace(chr(10), """ """)}, '
                                             f'{holder.right_data.right_type.value.text.replace(chr(10), """ """)}')
                if not holder_name_6:
                    holder_name_6 = 'данные о правообладателе отсутствуют'
            except:
                holder_name_6.append('данные о правообладателе отсутствуют')
            #7
            right_numb_7 = []
            register = soup.find_all("right_record")
            n = 0
            try:
                for reg in register:
                    n += 1
                    right_numb_7.append(f'{n}. {reg.right_data.right_number.text.replace(chr(10), """ """)}')
                if not right_numb_7:
                    right_numb_7 = 'данные о правообладателе отсутствуют'
            except:
                right_numb_7.append('данные о правообладателе отсутствуют')
            #8
            right_date_8 = []
            dats = soup.find_all("right_record")
            n = 0
            try:
                for dat in dats:
                    n += 1
                    right_date_8.append(f'{n}. {dat.record_info.registration_date.text.replace(chr(10), """ """)}')
                if not right_date_8:
                    right_date_8 = 'данные о правообладателе отсутствуют'
            except:
                right_date_8.append('данные о правообладателе отсутствуют')
            #9
            docs_regster_9 = "-"
            #10
            actual_egrn_10 = "-"
            #11
            docs_fundamental_11 = "-"
            #12
            vri_12 = "-"
            #13
            vri_by_document_13 = "-"
            #14
            category_zu_14 = "-"
            #15
            term_restrict_15 = []
            restriction = soup.find_all("restrict_record")
            n = 0
            try:
                for res in restriction:
                    n += 1
                    term_restrict_15.append(f'{n}. {res.restrictions_encumbrances_data.period.text.replace(chr(10), """ """)}')
                if not term_restrict_15:
                    term_restrict_15 = "данные не зарегистрированы"
            except:
                term_restrict_15.append('период не установлен')
            #16
            numb_res_16 = []
            restriction = soup.find_all("restrict_record")
            n = 0
            try:
                for res in restriction:
                    n += 1
                    numb_res_16.append(f'{n}. {res.restrictions_encumbrances_data.restriction_encumbrance_type.value.text.replace(chr(10), """ """)}')
                if not numb_res_16:
                    numb_res_16 = "данные не зарегистрированы"
            except:
                numb_res_16.append('данные не зарегистрированы')
            #17
            whom_rest_17 = []
            restriction = soup.find_all("restrict_record")
            n = 0
            try:
                for res in restriction:
                    n += 1
                    whom_rest_17.append(f'{n}. {res.right_holders.right_holder.text.replace(chr(10), """ """)}')
                if not whom_rest_17:
                    whom_rest_17 = "данные не зарегистрированы"
            except:
                whom_rest_17.append('данные не зарегистрированы')
            #18
            try:
                status_18 = soup.status.text
            except:
                status_18 = "нет данных"
            #19
            try:
                special_19 = soup.room_record.special_notes.text
            except:
                special_19 = "-"
            #20
            try:
                type_20 = soup.object.common_data.type.value.text
            except:
                type_20 = "нет данных"
            #21
            try:
                cad_links_21 = soup.cad_links.parent_cad_number.text.replace(chr(10), """ """)
            except:
                cad_links_21 = "нет данных"
            #22
            try:
                cad_price_22 = soup.room_record.cost.value.text.replace('.', ',')
            except:
                cad_price_22 = "нет данных"

            return [obj_name_2, adress_name_3, area_4, cad_numb_5, holder_name_6, right_numb_7, right_date_8,
                    docs_regster_9, actual_egrn_10, docs_fundamental_11, vri_12, vri_by_document_13, category_zu_14, term_restrict_15,
                    numb_res_16, whom_rest_17, status_18, special_19, type_20, cad_links_21, cad_price_22]


        elif soup.construction_record:
            #2
            try:
                obj_name_2 = soup.find("name").text
            except:
                obj_name_2 = "Сооружение"
            #3
            try:
                adress_name_3 = soup.readable_address.text
            except:
                adress_name_3 = "нет данных"
            #4
            try:
                area_4 = soup.params.base_parameters.text.replace('\n', ' ').replace('.', ',')
            except:
                area_4 = "нет данных"
            #5
            try:
                cad_numb_5 = soup.common_data.cad_number.text
            except:
                cad_numb_5 = "нет данных"
            #6
            holder_name_6 = []
            holders = soup.find_all("right_record")
            n = 0
            try:
                for holder in holders:
                    n += 1
                    if holder.right_data.share_description:
                        holder_name_6.append(f'{n}. {holder.right_holders.right_holder.text.replace(chr(10), """ """)}, '
                                             f'{holder.right_data.right_type.value.text.replace(chr(10), """ """)}, '
                                             f'{holder.right_data.share_description.text.replace(chr(10), """ """)}')
                    else:
                        holder_name_6.append(f'{n}. {holder.right_holders.right_holder.text.replace(chr(10), """ """)}, '
                                             f'{holder.right_data.right_type.value.text.replace(chr(10), """ """)}')

                if not holder_name_6:
                    holder_name_6 = 'данные о правообладателе отсутствуют'
            except:
                holder_name_6.append('данные о правообладателе отсутствуют')
            #7
            right_numb_7 = []
            register = soup.find_all("right_record")
            n = 0
            try:
                for reg in register:
                    n += 1
                    right_numb_7.append(f'{n}. {reg.right_data.right_number.text.replace(chr(10), """ """)}')
                if not right_numb_7:
                    right_numb_7 = 'данные о правообладателе отсутствуют'
            except:
                right_numb_7.append('данные о правообладателе отсутствуют')
            #8
            right_date_8 = []
            dats = soup.find_all("right_record")
            n = 0
            try:
                for dat in dats:
                    n += 1
                    right_date_8.append(f'{n}. {dat.record_info.registration_date.text.replace(chr(10), """ """)}')
                if not right_date_8:
                    right_date_8 = 'данные о правообладателе отсутствуют'
            except:
                right_date_8.append('данные о правообладателе отсутствуют')
            #9
            docs_regster_9 = "-"
            #10
            actual_egrn_10 = "-"
            #11
            docs_fundamental_11 = "-"
            #12
            vri_12 = "-"
            #13
            vri_by_document_13 = "-"
            #14
            category_zu_14 = "-"
            #15
            term_restrict_15 = []
            restriction = soup.find_all("restrict_record")
            n = 0
            try:
                for res in restriction:
                    n += 1
                    term_restrict_15.append(f'{n}. {res.restrictions_encumbrances_data.period.text.replace(chr(10), """ """)}')
                if not term_restrict_15:
                    term_restrict_15 = "данные не зарегистрированы"
            except:
                term_restrict_15.append('период не установлен')
            #16
            numb_res_16 = []
            restriction = soup.find_all("restrict_record")
            n = 0
            try:
                for res in restriction:
                    n += 1
                    numb_res_16.append(f'{n}. {res.restrictions_encumbrances_data.restriction_encumbrance_type.value.text.replace(chr(10), """ """)}')
                if not numb_res_16:
                    numb_res_16 = "данные не зарегистрированы"
            except:
                numb_res_16.append('данные не зарегистрированы')
            #17
            whom_rest_17 = []
            restriction = soup.find_all("restrict_record")
            n = 0
            try:
                for res in restriction:
                    n += 1
                    whom_rest_17.append(f'{n}. {res.right_holders.right_holder.text.replace(chr(10), """ """)}')
                if not whom_rest_17:
                    whom_rest_17 = "данные не зарегистрированы"
            except:
                whom_rest_17.append('данные не зарегистрированы')
            #18
            try:
                status_18 = soup.status.text
            except:
                status_18 = "нет данных"
            #19
            try:
                special_19 = soup.construction_record.special_notes.text
            except:
                special_19 = "нет данных"
            #20
            try:
                type_20 = soup.object.common_data.type.value.text
            except:
                type_20 = "нет данных"
            #21
            try:
                cad_links_21 = soup.cad_links.land_cad_numbers.text.replace(chr(10), """ """)
            except:
                cad_links_21 = "нет данных"
            #22
            try:
                cad_price_22 = soup.construction_record.cost.value.text.replace('.', ',')
            except:
                cad_price_22 = "нет данных"

            return [obj_name_2, adress_name_3, area_4, cad_numb_5, holder_name_6, right_numb_7, right_date_8,
                    docs_regster_9, actual_egrn_10, docs_fundamental_11, vri_12, vri_by_document_13, category_zu_14, term_restrict_15,
                    numb_res_16, whom_rest_17, status_18, special_19, type_20, cad_links_21, cad_price_22]

        elif soup.object_under_construction_record:
            #2
            obj_name_2 = "Объект незавершенного строительства"
            #3
            try:
                adress_name_3 = soup.readable_address.text
            except:
                adress_name_3 = "нет данных"
            #4
            try:
                area_4 = soup.params.built_up_area.text.replace('.', ',')
            except:
                area_4 = "нет данных"
            #5
            try:
                cad_numb_5 = soup.common_data.cad_number.text
            except:
                cad_numb_5 = "нет данных"
            #6
            holder_name_6 = []
            holders = soup.find_all("right_record")
            n = 0
            try:
                for holder in holders:
                    n += 1
                    if holder.right_data.share_description:
                        holder_name_6.append(f'{n}. {holder.right_holders.right_holder.text.replace(chr(10), """ """)}, '
                                             f'{holder.right_data.right_type.value.text.replace(chr(10), """ """)}, '
                                             f'{holder.right_data.share_description.text.replace(chr(10), """ """)}')
                    else:
                        holder_name_6.append(f'{n}. {holder.right_holders.right_holder.text.replace(chr(10), """ """)}, '
                                             f'{holder.right_data.right_type.value.text.replace(chr(10), """ """)}')
                if not holder_name_6:
                    holder_name_6 = 'данные о правообладателе отсутствуют'
            except:
                holder_name_6.append('данные о правообладателе отсутствуют')
            #7
            right_numb_7 = []
            register = soup.find_all("right_record")
            n = 0
            try:
                for reg in register:
                    n += 1
                    right_numb_7.append(f'{n}. {reg.right_data.right_number.text.replace(chr(10), """ """)}')
                if not right_numb_7:
                    right_numb_7 = 'данные о правообладателе отсутствуют'
            except:
                right_numb_7.append('данные о правообладателе отсутствуют')
            #8
            right_date_8 = []
            dats = soup.find_all("right_record")
            n = 0
            try:
                for dat in dats:
                    n += 1
                    right_date_8.append(f'{n}. {dat.record_info.registration_date.text.replace(chr(10), """ """)}')
                if not right_date_8:
                    right_date_8 = 'данные о правообладателе отсутствуют'
            except:
                right_date_8.append('данные о правообладателе отсутствуют')
            #9
            docs_regster_9 = "-"
            #10
            actual_egrn_10 = "-"
            #11
            docs_fundamental_11 = "-"
            #12
            vri_12 = "-"
            #13
            vri_by_document_13 = "-"
            #14
            category_zu_14 = "-"
            #15
            term_restrict_15 = []
            restriction = soup.find_all("restrict_record")
            n = 0
            try:
                for res in restriction:
                    n += 1
                    term_restrict_15.append(f'{n}. {res.restrictions_encumbrances_data.period.text.replace(chr(10), """ """)}')
                if not term_restrict_15:
                    term_restrict_15 = "данные не зарегистрированы"
            except:
                term_restrict_15.append('период не установлен')
            #16
            numb_res_16 = []
            restriction = soup.find_all("restrict_record")
            n = 0
            try:
                for res in restriction:
                    n += 1
                    numb_res_16.append(f'{n}. {res.restrictions_encumbrances_data.restriction_encumbrance_type.value.text.replace(chr(10), """ """)}')
                if not numb_res_16:
                    numb_res_16 = "данные не зарегистрированы"
            except:
                numb_res_16.append('данные не зарегистрированы')
            #17
            whom_rest_17 = []
            restriction = soup.find_all("restrict_record")
            n = 0
            try:
                for res in restriction:
                    n += 1
                    whom_rest_17.append(f'{n}. {res.right_holders.right_holder.text.replace(chr(10), """ """)}')
                if not whom_rest_17:
                    whom_rest_17 = "данные не зарегистрированы"
            except:
                whom_rest_17.append('данные не зарегистрированы')
            #18
            try:
                status_18 = soup.status.text
            except:
                status_18 = "нет данных"
            #19
            try:
                special_19 = soup.object_under_construction_record.special_notes.text
            except:
                special_19 = "нет данных"
            #20
            try:
                type_20 = soup.object.common_data.type.value.text
            except:
                type_20 = "нет данных"
            #21
            try:
                cad_links_21 = soup.cad_links.land_cad_numbers.text.replace(chr(10), """ """)
            except:
                cad_links_21 = "нет данных"
            #22
            cad_price_22 = "-"

            return [obj_name_2, adress_name_3, area_4, cad_numb_5, holder_name_6, right_numb_7, right_date_8,
                    docs_regster_9, actual_egrn_10, docs_fundamental_11, vri_12, vri_by_document_13, category_zu_14, term_restrict_15,
                    numb_res_16, whom_rest_17, status_18, special_19, type_20, cad_links_21, cad_price_22]