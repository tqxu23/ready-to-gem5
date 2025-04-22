import time
class RTG_timer():
    def __init__(self):
        pass
    def get_cur_time_str(self):
        return time.strftime('%Y%m%d-%H-%M-%S', time.localtime())
    
    def start(self):
        self.starttime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print("开始时间："+ self.starttime)
    
    def end(self):
        self.endtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print("结束时间："+ self.endtime)