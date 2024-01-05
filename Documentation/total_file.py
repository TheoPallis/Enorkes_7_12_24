

@@ Script -> Create_Excel_File.py

import pandas as pd

def create_excel_file(df1,df2,df3,df4,df5,df6) :
    with pd.ExcelWriter('����_auto.xlsx', engine='openpyxl') as writer:
        df1.to_excel(writer, sheet_name='�������', index=False)
        df2.to_excel(writer, sheet_name='�������', index=False)
        df3.to_excel(writer, sheet_name='�������', index=False)
        df4.to_excel(writer, sheet_name='�����������', index=False)
        df5.to_excel(writer, sheet_name='Checks', index=False)
        df6.to_excel(writer, sheet_name='Checklist', index=False)



@@ Script -> df1.py


df1 = pd.DataFrame({
 'A/A': [x for x in range(1,len(anathesi_df['�������� ��������'])+1)],
    '���������': anathesi_df['�������� ��������'],
    '�������' : anathesi_df['�������'].apply(lambda x : str(x)[:str(x).index(anathesi_word)]+ '�������'), #Clean �������
    '��������� ������': "",
    '���������': "",

    '��������' : anathesi_df['��������'],
    '�������' : "",
})



df1['�������'] = (r"\\lawoffice\\Applications\\ScanDocs\\������ scandocs\\" 
                  + df1['�������'].apply(lambda x: get_folder_or_filename(x, -3)) # For subfolders (eg �����������)
                   + "\\" 
                  + df1['�������'].apply(lambda x: get_folder_or_filename(x, -2)) 
                  + "\\" 
                  + df1['�������'].apply(lambda x: get_folder_or_filename(x, -1)))

df1['�������'] = df1['�������'].astype(str) 
df1['�������'] =df1['�������'].apply(lambda x : x.replace("������� �������",""))





# Apply the function to the '�������' column
df1['�������'] = df1['�������'].apply(write_hyperlink)

def write_hyperlink(link):
    # Using the openpyxl syntax to specify a hyperlink
    return f'=HYPERLINK("{link}", "{link}")'




@@ Script -> df2.py

df2 = pd.DataFrame({
 'A/A': [x for x in range(1,len(anathesi_df['�������� ��������'])+1)],
    '���������': anathesi_df['�������� ��������'],
    '����������': anathesi_df['����������'],
    '��������� ������': anathesi_df['��������� ������'],
    # '���������� ���������': anathesi_df['Date_Katathesi'],
    '���������� ���������': "-",
    
    '���������� ���������2': "",
    '���':  anathesi_df['���'].apply(lambda x :str(x).replace(".0","")).replace("nan",""),
    '���' : anathesi_df['���'].apply(lambda x :str(x).replace(".0","")).replace("nan","")
})





@@ Script -> df3.py

df3 = pd.DataFrame({
    'A/A': [x for x in range(1,len(anathesi_df['�������� ��������'])+1)],
    '���������': anathesi_df['�������� ��������'],
    '���������_1': antidikos_1,
    '���������_2': antidikos_2,
    '���������_3':antidikos_3,
    '����������_������':  last_date,
    '����������_�������' : "-",
    '��� �������': hours_col,
    '���������' : anathesi_df['���������_full'] ,
    '���������� ������' : '-',
    '�������' : AITHOUSA
})
# df3['����������_�������']= pd.to_datetime(anathesi_df['���������� ���������������  �������'], errors='coerce')
# df3['����������_�������'] = df3['����������_�������'].dt.strftime('%d/%m/%Y')
df3.replace(regex=True,inplace=True,to_replace="�.']",value="")
# df3

