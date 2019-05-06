import os
from flask import Flask, render_template, request, redirect, url_for
from flask.json import jsonify
import sqlite3 as sql
app = Flask(__name__)

cache = {}


@app.route('/')
def home():
    fn = os.path.join(os.path.dirname(__file__), 'db')
    print(os.listdir(fn))
    return render_template('home.html', databases=os.listdir(fn))


@app.route('/addData', methods=['POST', 'GET'])
def addData():
    print('insert')
    if request.method == 'POST':
        con = sql.connect(cache['curDB'])
        con.row_factory = sql.Row

        for key in request.form:
            print(request.form[key])
            command = 'INSERT INTO test' + \
                '(value),' + '(' + request.form[key] + ')'
            res = con.execute(command)

        return redirect(url_for('test'))


@app.route('/enternew')
def new_student():
    return render_template('student.html')


@app.route('/selectDB', methods=['POST', 'GET'])
def selectDB():
    if request.method == 'POST':
        cache['curDB'] = './db/' + request.form['getDB']

    con = sql.connect(cache['curDB'])
    con.row_factory = sql.Row

    res = con.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tableNames = []
    for name in res:
        if name[0].find('Match') == 0:
            continue
        tableNames.append(name[0])

    return render_template("selectDB.html", tables=tableNames)


@app.route('/selectMatch', methods=['POST', 'GET'])
def selectMatch():
    con = sql.connect(cache['curDB'])
    con.row_factory = sql.Row
    tmp = [request.form['getTable'], request.form['getTable2']]
    tmp.sort()
    cache['match1'] = tmp[0]
    cache['match2'] = tmp[1]

    res = con.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tableNames = []
    matchName = []

    for name in res:
        if cache['match1'] + '_' + cache['match2'] in name[0]:
            tableNames.append(name[0])
            matchName.append(name[0].split('_')[-1])

    return render_template("selectMatch.html", tables=tableNames, matchName=matchName, length=len(matchName), m1=cache['match1'], m2=cache['match2'])


@app.route('/filterData', methods=['POST', 'GET'])
def filterData():
    con = sql.connect(cache['curDB'])
    con.row_factory = sql.Row
    cur = con.cursor()

    matchNote = cache['MatchTable'].split('_')[-1]
    rows_cen = cache['rows_cen']
    names_cen = cache['names_cen']
    rows_blo = cache['rows_blo']
    names_blo = cache['names_blo']

    if 'match1' in request.form:
        print(request.form['match1'])
        command = "select rowid, * from " + request.form['match1'] + ' where '
        like = []

        for ss in request.form:
            tmp = ''
            if ss == 'match1' or request.form[ss] == '':
                continue
            tmp += ss
            tmp += ' like \'%'
            tmp += request.form[ss]
            tmp += '%\''
            like.append(tmp)
        command += ' and '.join(like)
        print(command)
        cur.execute(command)
        rows_cen = cur.fetchall()
        cache['rows_cen'] = rows_cen
    elif 'match2' in request.form:
        print(request.form['match2'])
        command = "select rowid, * from " + request.form['match2'] + ' where '
        like = []

        for ss in request.form:
            tmp = ''
            if ss == 'match2' or request.form[ss] == '':
                continue
            tmp += ss
            tmp += ' like \'%'
            tmp += request.form[ss]
            tmp += '%\''
            like.append(tmp)
        command += ' and '.join(like)
        print(command)
        cur.execute(command)
        rows_blo = cur.fetchall()
        cache['rows_blo'] = rows_blo

    return render_template("addNewEntry.html", rows_cen=rows_cen, schema_cen=names_cen, rows_blo=rows_blo, schema_blo=names_blo, matchNote=matchNote, cache=cache)


@app.route('/filter', methods=['POST', 'GET'])
def filter():
    con = sql.connect(cache['curDB'])
    con.row_factory = sql.Row
    cur = con.cursor()
    # print("hi", request.form['getTable'])
    m1 = cache['match1'] + '_rowid'
    m2 = cache['match2'] + '_rowid'

    command = "select rowid, * from " + cache['MatchTable']
    cur.execute(command)
    # print(cur.description)
    cursor = con.execute(command)
    # instead of cursor.description:
    row = cursor.fetchone()
    names_match = []
    if row:
        names_match = row.keys()

    command = "select rowid, * from " + cache['MatchTable']
    cur.execute(command)
    # print(cur.description)
    cursor = con.execute(command)
    # instead of cursor.description:
    rows_match = cur.fetchall()
    if m1 in names_match and m2 in names_match:
        m1_idx = names_match.index(m1)
        m2_idx = names_match.index(m2)
    exc = set()
    exc2 = set()
    if names_match:
        for row in rows_match:
            exc.add(row[m1_idx])
            exc2.add(row[m2_idx])
    # print(exc)
    ss = '('
    for ee in exc:
        ss += ee + ','
    ss = ss[:-1] + ')'
    if ss[0] != '(':
        ss = '(' + ss
    command = "select rowid, * from " + \
        cache['match1'] + ' where rowid not in ' + ss
    print(request.form)
    if "show" in request.form:
        print(request.form["show"])
    if "show" in request.form and request.form["show"] == "Show all data":
        command = "select rowid, * from " + cache['match1']

    cur.execute(command)
    # print(cur.description)
    cursor = con.execute(command)
    # instead of cursor.description:
    row = cursor.fetchone()
    names_cen = row.keys()

    rows_cen = cur.fetchall()

    rows_match = cur.fetchall()

    ss = '('
    for ee in exc2:
        ss += ee + ','
    ss = ss[:-1] + ')'
    if ss[0] != '(':
        ss = '(' + ss
    # print(names_match)
    command = "select rowid, * from " + \
        cache['match2'] + ' where rowid not in ' + ss
    cur = con.cursor()
    if "show" in request.form and request.form["show"] == "Show all data":
        command = "select rowid, * from " + cache['match2']
    # print(command, ss)
    cur.execute(command)
    # print(cur.description)
    cursor = con.execute(command)
    # instead of cursor.description:
    row = cursor.fetchone()
    names_blo = row.keys()

    rows_blo = cur.fetchall()
    matchNote = cache['MatchTable'].split('_')[-1]
    cache['rows_cen'] = rows_cen
    cache['names_cen'] = names_cen
    cache['rows_blo'] = rows_blo
    cache['names_blo'] = names_blo

    return render_template("addNewEntry.html", rows_cen=rows_cen, schema_cen=names_cen, rows_blo=rows_blo, schema_blo=names_blo, matchNote=matchNote, cache=cache)


@app.route('/addNewEntry', methods=['POST', 'GET'])
def addNewEntry():
    con = sql.connect(cache['curDB'])
    con.row_factory = sql.Row
    cur = con.cursor()
    # print("hi", request.form['getTable'])
    m1 = cache['match1'] + '_rowid'
    m2 = cache['match2'] + '_rowid'

    if request.form['getTable']:
        cache['MatchTable'] = request.form['getTable']

    command = "select rowid, * from " + cache['MatchTable']
    cur.execute(command)
    # print(cur.description)
    cursor = con.execute(command)
    # instead of cursor.description:
    row = cursor.fetchone()
    names_match = []
    if row:
        names_match = row.keys()
        # print(names_match.index(m1), names_match.index(m2))
    rows_match = cur.fetchall()
    if m1 in names_match and m2 in names_match:
        m1_idx = names_match.index(m1)
        m2_idx = names_match.index(m2)
    exc = set()
    exc2 = set()
    if names_match:
        for row in rows_match:
            exc.add(row[m1_idx])
            exc2.add(row[m2_idx])
    # print(exc)
    ss = '('
    for ee in exc:
        ss += ee + ','
    ss = ss[:-1] + ')'
    if ss[0] != '(':
        ss = '(' + ss
    command = "select rowid, * from " + \
        cache['match1'] + ' where rowid not in ' + ss
    print(request.form)
    if "show" in request.form:
        print(request.form["show"])
    if "show" in request.form and request.form["show"] == "Show all data":
        command = "select rowid, * from " + cache['match1']

    cur.execute(command)
    # print(cur.description)
    cursor = con.execute(command)
    # instead of cursor.description:
    row = cursor.fetchone()
    names_cen = row.keys()

    rows_cen = cur.fetchall()

    rows_match = cur.fetchall()

    ss = '('
    for ee in exc2:
        ss += ee + ','
    ss = ss[:-1] + ')'
    if ss[0] != '(':
        ss = '(' + ss
    # print(names_match)
    command = "select rowid, * from " + \
        cache['match2'] + ' where rowid not in ' + ss
    cur = con.cursor()
    if "show" in request.form and request.form["show"] == "Show all data":
        command = "select rowid, * from " + cache['match2']
    # print(command, ss)
    cur.execute(command)
    # print(cur.description)
    cursor = con.execute(command)
    # instead of cursor.description:
    row = cursor.fetchone()
    names_blo = row.keys()

    rows_blo = cur.fetchall()
    matchNote = cache['MatchTable'].split('_')[-1]
    cache['rows_cen'] = rows_cen
    cache['names_cen'] = names_cen
    cache['rows_blo'] = rows_blo
    cache['names_blo'] = names_blo
    return render_template("addNewEntry.html", rows_cen=rows_cen, schema_cen=names_cen, rows_blo=rows_blo, schema_blo=names_blo, matchNote=matchNote, cache=cache)


@app.route('/createTable', methods=['POST', 'GET'])
def createTable():
    if request.method == 'POST':
        con = sql.connect(cache['curDB'])
        con.row_factory = sql.Row

        newN = 'Match_' + cache['match1'] + '_' + \
            cache['match2'] + '_' + request.form['name']
        command = 'CREATE TABLE ' + newN + \
            ' (' + request.form['name'] + ' TEXT'
        print(newN)

        res = con.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tableNames = []
        for name in res:
            if name[0].find('Match') == 0:
                continue
            tableNames.append(name[0])

            command += ', ' + name[0] + '_rowid TEXT'

        command += ', Master TEXT, Note TEXT)'
        print(command)
        con.execute(command)

        cache['MatchTable'] = newN

        con = sql.connect(cache['curDB'])
        con.row_factory = sql.Row

        res = con.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tableNames = []
        matchName = []

        for name in res:
            if cache['match1'] in name[0] and cache['match2'] in name[0]:
                tableNames.append(name[0])
                matchName.append(name[0].split('_')[-1])

        return render_template("selectMatch.html", tables=tableNames, matchName=matchName, length=len(matchName), m1=cache['match1'], m2=cache['match2'])

        # return render_template("addNewEntry.html", )


def getDataForMatch():
    print("updating")
    con = sql.connect(cache['curDB'])
    con.row_factory = sql.Row
    cur = con.cursor()
    # print("hi", request.form['getTable'])
    m1 = cache['match1'] + '_rowid'
    m2 = cache['match2'] + '_rowid'

    command = "select rowid, * from " + cache['MatchTable']
    cur.execute(command)
    # print(cur.description)
    cursor = con.execute(command)
    # instead of cursor.description:
    row = cursor.fetchone()
    names_match = []
    if row:
        names_match = row.keys()
    # instead of cursor.description:
    rows_match = cur.fetchall()
    if m1 in names_match and m2 in names_match:
        m1_idx = names_match.index(m1)
        m2_idx = names_match.index(m2)
    exc = set()
    exc2 = set()
    if names_match:
        for row in rows_match:
            exc.add(row[m1_idx])
            exc2.add(row[m2_idx])
    # print(exc)
    ss = '('
    for ee in exc:
        ss += ee + ','
    ss = ss[:-1] + ')'
    if ss[0] != '(':
        ss = '(' + ss
    command = "select rowid, * from " + \
        cache['match1'] + ' where rowid not in ' + ss
    print(request.form)
    if "show" in request.form:
        print(request.form["show"])
    if "show" in request.form and request.form["show"] == "Show all data":
        command = "select rowid, * from " + cache['match1']

    cur.execute(command)
    # print(cur.description)
    cursor = con.execute(command)
    # instead of cursor.description:
    row = cursor.fetchone()
    names_cen = row.keys()

    rows_cen = cur.fetchall()

    rows_match = cur.fetchall()

    ss = '('
    for ee in exc2:
        ss += ee + ','
    ss = ss[:-1] + ')'
    if ss[0] != '(':
        ss = '(' + ss
    # print(names_match)
    command = "select rowid, * from " + \
        cache['match2'] + ' where rowid not in ' + ss
    cur = con.cursor()
    if "show" in request.form and request.form["show"] == "Show all data":
        command = "select rowid, * from " + cache['match2']

    print(command, ss)
    cur.execute(command)
    # print(cur.description)
    cursor = con.execute(command)
    # instead of cursor.description:
    row = cursor.fetchone()
    names_blo = row.keys()

    rows_blo = cur.fetchall()

    cache['rows_cen'] = rows_cen
    cache['names_cen'] = names_cen
    cache['rows_blo'] = rows_blo
    cache['names_blo'] = names_blo


@app.route('/addmatchrec', methods=['POST', 'GET'])
def addmatchrec():
    if request.method == 'POST':
        try:
            print(request.form["match1"])
            # nm = request.form['nm']
            # addr = request.form['add']
            # city = request.form['city']
            # pin = request.form['pin']
            #
            with sql.connect(cache['curDB']) as con:
                cur = con.cursor()
            con.row_factory = sql.Row
            m1 = cache['match1']
            m2 = cache['match2']
            master = request.form["master"]
            Note = request.form["Note"]
            print("match1", len(request.form.getlist("match1")))
            print("match2", len(request.form.getlist("match2")))
            print(master, Note)
            matchNote = cache['MatchTable'].split('_')[-1]
            for i in range(len(request.form.getlist("match1"))):
                for j in range(len(request.form.getlist("match2"))):
                    print(request.form.getlist("match1")[
                          i], request.form.getlist("match2")[j])
                    command = "INSERT INTO " + \
                        cache['MatchTable'] + " (" + m1 + "_rowid, " + m2 + \
                        "_rowid, " + matchNote + \
                        ", Master, Note) VALUES(?, ?, ?, ?, ?)"
                    print(command)
                    cur.execute(
                        command, (request.form.getlist("match1")[i], request.form.getlist("match2")[j], request.form['matchInput'], master, Note))
                    # print("add a record")
            con.commit()
            # print(request.form['matchInput'])
            msg = "Record successfully added"

        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            # print(msg)
            command = "select * from " + cache['MatchTable']
            con = sql.connect(cache['curDB'])
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute(command)
            # print(cur.description)
            cursor = con.execute(command)
            # instead of cursor.description:
            row = cursor.fetchone()
            names = row.keys()
            rows = cur.fetchall()

            getDataForMatch()
            matchNote = cache['MatchTable'].split('_')[-1]

            return render_template("addNewEntry.html", rows_cen=cache['rows_cen'], schema_cen=cache['names_cen'], rows_blo=cache['rows_blo'], schema_blo=cache['names_blo'], matchNote=matchNote, cache=cache)
            con.close()


@app.route('/getMatchlist', methods=['POST', 'GET'])
def getMatchlist():

    try:

        matchTable = request.form['getTable']

        command = "select rowid, * from " + matchTable

        with sql.connect(cache['curDB']) as con:
            cur = con.cursor()

        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute(command)

        cursor = con.execute(command)
        # instead of cursor.description:
        row = cursor.fetchone()
        names = row.keys()
        rows = cur.fetchall()

        cache['match_schema'] = names
        cache['match_rows'] = rows
        cache['match_table'] = matchTable

        return render_template("matchtable.html", rows=rows, schema=names, msg="")

    except:
        return render_template("error.html", msg="The table is empty now. Please, insert some data first")


@app.route('/getEntryInfo', methods=['POST', 'GET'])
def getEntryInfo():

    try:

        # matchTable = cache['match_table']
        #
        # command = "select * from " + matchTable
        #
        # with sql.connect(cache['curDB']) as con:
        #     cur = con.cursor()
        #
        # con.row_factory = sql.Row
        # cur = con.cursor()
        # cur.execute(command)
        #
        # cursor = con.execute(command)
        # # instead of cursor.description:
        # row = cursor.fetchone()
        #
        # print(cache['match_rows'])
        # entry = cache['match_rows'][request.form['info']]
        # print(entry)
        # return render_template("matchtable.html", rows=cache['match_rows'], schema=cache['match_schema'], msg="")
        msg = ''
        matchTable = cache['match_table']

        print(cache['match_rows'])
        entry = cache['match_rows'][int(request.form['info'])]
        tmp = []

        if 'delete' in request.form:
            print(request.form['delete'])
            msg = "Delete data successfully. Data information is shown below."
            command_delete = "DELETE FROM " + matchTable + \
                " where rowid=" + str(request.form['delete'])
            with sql.connect(cache['curDB']) as con_det:
                cur_det = con_det.cursor()
            con_det.row_factory = sql.Row
            cur_det = con_det.cursor()
            print(command_delete)
            cur_det.execute(command_delete)

            con_det.commit()

            command = "select rowid, * from " + matchTable

            with sql.connect(cache['curDB']) as con:
                cur = con.cursor()

            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute(command)

            cursor = con.execute(command)
            # instead of cursor.description:
            row = cursor.fetchone()
            names = row.keys()
            rows = cur.fetchall()
            print("delete rows:", rows)
            cache['match_schema'] = names
            cache['match_rows'] = rows
            cache['match_table'] = matchTable

        print(entry)
        for i in range(2, len(entry) - 2):
            if entry[i]:
                tmp.append(('_'.join(cache['match_schema']
                                     [i].split('_')[:-1]), int(entry[i])))
                if len(tmp) == 2:
                    print(tmp)
                    break

        table1 = str(tmp[0][0])
        table2 = str(tmp[1][0])

        command1 = "select rowid, * from " + \
            table1 + " where rowid=" + str(tmp[0][1])
        command2 = "select rowid, * from " + \
            table2 + " where rowid =" + str(tmp[1][1])

        with sql.connect(cache['curDB']) as con1:
            cur1 = con1.cursor()

        con1.row_factory = sql.Row
        cur1 = con1.cursor()

        cur1.execute(command1)

        cursor1 = con1.execute(command1)
        # instead of cursor.description:
        rows1 = cur1.fetchall()
        row1 = cursor1.fetchone()
        schema1 = row1.keys()

        with sql.connect(cache['curDB']) as con2:
            cur2 = con2.cursor()

        con2.row_factory = sql.Row
        cur2 = con2.cursor()

        cur2 = con2.cursor()

        cur2.execute(command2)

        cursor2 = con2.execute(command2)
        # instead of cursor.description:
        rows2 = cur2.fetchall()
        row2 = cursor2.fetchone()
        schema2 = row2.keys()

        info_schema = [schema1] + [schema2]
        info = [rows1] + [rows2]
        # print(info)

        return render_template("matchtable.html", rows=cache['match_rows'], schema=cache['match_schema'], info=info, info_schema=info_schema, msg=msg)

    except:
        return render_template("error.html", msg="The table is empty now. Please, insert some data first")


@app.route('/matchlist')
def matchlist():

    con = sql.connect(cache['curDB'])
    con.row_factory = sql.Row
    matchTable = cache['MatchTable']
    cur = con.cursor()
    cur.execute('select rowid, * from ' + matchTable)
    cursor = con.execute('select * from ' + matchTable)
    row = cursor.fetchone()
    names_match = row.keys()
    rows = cur.fetchall()

    return render_template("matchtable.html", rows=rows, names=names_match, msg='')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']

            with sql.connect("riedeltest.db") as con:
                cur = con.cursor()

                cur.execute(
                    "INSERT INTO students(name, addr, city, pin) VALUES(?, ?, ?, ?)", (nm, addr, city, pin))

                con.commit()
                msg = "Record successfully added"

        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html", msg=msg)
            con.close()


@app.route('/addmatch', methods=['POST', 'GET'])
def addmatch():
    if request.method == 'POST':
        try:
            with sql.connect("riedeltest.db") as con:
                cur = con.cursor()
                cen_id = request.form['match1']
                blo_id = request.form['match2']
                master = request.form['master']
                Note = request.form['Note']
                print(cen_id, blo_id)

                cur.execute(
                    "INSERT INTO Match_Table(census_rowid, block_book_rowid, Master, Note) VALUES(?, ?, ?, ?)", (cen_id, blo_id, master, Note))
                con.commit()
                msg = "Record successfully added"

        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html", msg=msg)
            con.close()


@app.route('/list')
def list():
    con = sql.connect("riedeltest.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from censuses")
    # print(cur.description)
    cursor = con.execute('select * from censuses')
    # instead of cursor.description:
    row = cursor.fetchone()
    names_cen = row.keys()

    rows_cen = cur.fetchall()

    cur = con.cursor()
    cur.execute("select * from block_book")
    # print(cur.description)
    cursor = con.execute('select * from block_book')
    # instead of cursor.description:
    row = cursor.fetchone()
    names_blo = row.keys()

    rows_blo = cur.fetchall()

    return render_template("list.html", rows_cen=rows_cen, schema_cen=names_cen, rows_blo=rows_blo, schema_blo=names_blo)


if __name__ == '__main__':
    app.run(debug=True)
