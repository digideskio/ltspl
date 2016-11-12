class Event:
    def __init__(self, *args):
        self.args = args


class GEventDispatcher:
    event_dic = {}

    def __init__(self):
        pass

    @staticmethod
    def addEventListener(name: str, callback):
        func_arr = GEventDispatcher.event_dic.get(name)
        if func_arr is None:
            GEventDispatcher.event_dic[name] = []
        GEventDispatcher.event_dic[name].append(callback)
        pass

    @staticmethod
    def removeEventListener(name: str, callback):
        func_arr = GEventDispatcher.event_dic.get(name)
        if func_arr is not None:
            func_arr.remove(callback)

    @staticmethod
    def dispatcherEvent(name: str, event: Event):
        func_arr = GEventDispatcher.event_dic.get(name)
        if func_arr is not None:
            for func in func_arr:
                func(event)
        pass


