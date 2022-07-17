# TODO: Double check if this is necessary and remove it if not
def get_filepath(path: str) -> str:
    import os

    directory = os.getcwd()
    filepath = path

    if path[0] != "/":
        filepath = f"/{filepath}"

    return f"{directory}{filepath}"


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
