import os
import mysql.connector as conn
import datetime

def getLastSolutionDate() -> datetime.datetime:
    connection = conn.connect(
        host="localhost",
        user="root",
        password="O247HY54ru",
        database="ege"
    )
    with connection.cursor() as cursor:
        cursor.execute("""SELECT MAX(date_solved) data
                            FROM `solutions`
                            LIMIT 1;"""
        )
        result = cursor.fetchall()
        return result[0][0].astimezone()
    
def get_time_created(path) -> datetime.datetime:
    return datetime.datetime.fromtimestamp(os.stat(path).st_ctime).astimezone()

def scanFiles(last_date: datetime.datetime = datetime.datetime(2020, 12, 1, 0,0,0).astimezone()):
    # last_date = getLastSolutionDate()
    res = {}
    for dir in os.listdir("./"):
        try:
            i_dir = int(dir.split(",")[0])
            res[i_dir] = dir
        except:
            pass
    values = []
    by_folder_id = {}
    for problem_id, folder in res.items():
        for file_name in [x for x in os.listdir(f"./{folder}/") if '.py' in x or ".xlsx" in x]:
            solution_path = f"./{folder}/{file_name}"
            time_created = get_time_created(solution_path)
            if time_created > last_date:
                if "AA" in file_name:
                    is_correct = True
                elif "WW" in file_name:
                    is_correct = False
                else:
                    is_correct = None
                values.append((time_created.isoformat(), problem_id, file_name, is_correct))
                if folder in by_folder_id.keys():
                    by_folder_id[folder].append((file_name, is_correct))
                else:
                    by_folder_id[folder] = [(file_name, is_correct)]
    return by_folder_id, values


# print(scanFiles(getLastSolutionDate()))