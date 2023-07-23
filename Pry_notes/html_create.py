def create_html_file(input_data): # Модуль созддания HTML - файла с базой данных
    html = '<html>\n <head></head>\n <body>\n'
    for e in input_data :
        html += '<p> {}</p>\n'\
            .format(e)           
    html += '</body>\n</html>' 
    with open('base.html', 'w') as page:
        page.write(html)        
    return()