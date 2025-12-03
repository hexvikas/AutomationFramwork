import openpyxl

def get_data_from_excel(path, sheet_name):
    final_list = []
    # Workbook load karo
    workbook = openpyxl.load_workbook(path)
    sheet = workbook[sheet_name]
    
    # Total rows aur columns count karo
    total_rows = sheet.max_row
    total_cols = sheet.max_column
    
    # Loop chalao (Row 2 se start kyunki Row 1 headers hai)
    for r in range(2, total_rows + 1):
        row_list = []
        for c in range(1, total_cols + 1):
            # Har cell ka data uthao
            cell_value = sheet.cell(row=r, column=c).value
            row_list.append(cell_value)
        # Row ka data list mein add karo
        final_list.append(row_list)
        
    return final_list