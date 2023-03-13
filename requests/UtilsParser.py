class UtilsParser:
    @staticmethod
    def FixRingDict(input_dict: dict) -> dict:
        fixed_dict = {}
        fixed_dict['authyn'] = int(input_dict['authyn'])
        fixed_dict['btn_yn'] = int(input_dict['btn_yn'])
        fixed_dict['cno'] = int(input_dict['cno'])
        fixed_dict['DATE'] = input_dict['f1']
        fixed_dict['rake'] = input_dict['f6']
        fixed_dict['insurance'] = input_dict['f9']
        fixed_dict['f11_ty'] = str(input_dict['f11_ty'])
        fixed_dict['type'] = input_dict['f3']
        fixed_dict['game'] = input_dict['f4']
        fixed_dict['table_name'] = input_dict['f2']
        fixed_dict['limit'] = input_dict['f5']
        fixed_dict['rake'] = input_dict['f6']
        fixed_dict['players'] = input_dict['f7']
        fixed_dict['status'] = input_dict['f8']
        fixed_dict['f8_ty'] = int(input_dict['f8_ty'])
        fixed_dict['end_date'] = input_dict['f11']
        fixed_dict['num'] = int(input_dict['num'])
        fixed_dict['p_yn'] = bool(input_dict['p_yn'])
        fixed_dict['rno'] = int(input_dict['rno'])
        fixed_dict['tno'] = int(input_dict['tno'])

        return fixed_dict 
    
    def FixRingInfDict(input_dict: dict) -> dict:
        fixed_inf_dict = {}
        fixed_inf_dict['f1'] = str(input_dict['f1'])
        fixed_inf_dict['f2'] = str(input_dict['f2'])
        fixed_inf_dict['f3'] = str(input_dict['f3'])
        fixed_inf_dict['f4'] = str(input_dict['f4'])
        fixed_inf_dict['f5'] = str(input_dict['f5'])
        fixed_inf_dict['f6'] = str(input_dict['f6'])
        fixed_inf_dict['f7'] = str(input_dict['f7'])
        fixed_inf_dict['f7_ty'] = int(input_dict['f7_ty'])
        fixed_inf_dict['f8'] = str(input_dict['f8'])
        fixed_inf_dict['f8_ty'] = int(input_dict['f8_ty'])
        fixed_inf_dict['num'] = str(input_dict['num'])
        fixed_inf_dict['uno'] = str(input_dict['uno'])

        return fixed_inf_dict

    def FixHandDict(input_dict: dict) -> dict:
        fixed_hand_dict = {}
        fixed_hand_dict['f1'] = str(input_dict['f1'])
        fixed_hand_dict['f2'] = str(input_dict['f2'])
        # fixed_hand_dict['f3'] = #######(input_dict['f3'])
        fixed_hand_dict['f4'] = str(input_dict['f4'])
        fixed_hand_dict['f5'] = str(input_dict['f5'])
        fixed_hand_dict['f5_ty'] = int(input_dict['f5_ty'])

        return fixed_hand_dict
    








