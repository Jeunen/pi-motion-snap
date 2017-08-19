import pusher
from settings import pushertrigger


class PusherTrigger:

    def __init__(self):
        self.client = pusher.Pusher(
            app_id=pushertrigger['APP_ID'],
            key=pushertrigger['KEY'],
            secret=pushertrigger['SECRET'],
            cluster=pushertrigger['CLUSTER'],
            ssl=pushertrigger['SSL']
        )

    def shoot(self):
        self.client.trigger(pushertrigger['CHANNEL'], pushertrigger['EVENT'], {'message': pushertrigger['MESSAGE']})
