# This file will get executed when the function is executed
from alloydb_utility import AlloyDB


def main(request):
    request_json = request.get_json()
    query_type = request_json["query_type"]
    try:
        alloydb_obj = AlloyDB()
        if query_type == "select":
            result = alloydb_obj.select_query(
                """SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';"""
            )
            print(result)
        return "Task Completed Successfully"
    except Exception as e:
        print(e)
        return e