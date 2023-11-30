file=input()
if file.endswith('.jpeg'):
    print('Photo file')
elif file.endswith('.doc'):
    print('Word file')
elif file.endswith('.xls'):
    print('Excel file')
elif file.endswith('.ppt'):
    print('Powerpoint file')
else:
    print('Invalid file')
