def write_to_json(json_payload: str):
    import datetime
    import time

    now = datetime.datetime.now()
    unix_time = int(time.time())

    with open(
        f"output/output-{now.year}-{now.month}-{now.day}-{unix_time}.json", "w"
    ) as output_file:
        output_file.write(json_payload)
        output_file.close
