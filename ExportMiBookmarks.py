# coding=utf-8
import datetime
import sqlite3

conn = sqlite3.connect('browser2.db')
cursor = conn.cursor()
cursor.execute('SELECT _id,title,url,folder,parent,created  FROM bookmarks;')
values = cursor.fetchall()
length = len(values)

with open('MiBookmarks'+datetime.datetime.now().date().strftime('%Y%m%d')+'.html', "w", encoding='utf-8') as f:
    f.write('<!DOCTYPE NETSCAPE-Bookmark-file-1>\n')
    f.write('<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n')
    f.write('<TITLE>MiBookmarks</TITLE>\n'+'<H1>Bookmarks</H1>\n'+'<DL><p>\n')
    for i in range(0, length):
        if values[i][3] == 1:
            p = values[i][0]
            f.write('\n<DT><H3 ADD_DATE="" ' + 'LAST_MODIFIED="">' + values[i][1] + '</H3>')
            f.write('\n<DL><p>')
            for j in range(0, length):
                if (values[j][4] == p) & (values[j][3] != 1):
                    f.write(
                        '\n<DT><A HREF="' + values[j][2] + '" ADD_DATE="' + str(values[j][5] // 1000) + '" ICON="">' +
                        values[j][1] + '</A>')
            f.write('\n</DL><p>')
    f.write('\n</DL><p>')
cursor.close()
conn.close()
