import datetime


def get_context(context):
    # current time
    context.time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")