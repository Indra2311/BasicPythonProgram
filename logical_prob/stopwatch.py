import time
"""
   * Author - Indrajeet
   * Date - 05-06-2021
   * Time - 11:50 AM
   * Title - Simulate Stopwatch Program
"""


class StopWatch:
    def startstopwatch(self):
        try:
            start = int(input("Please enter 1 so start Stopwatch: "))
            start_time = time.time()
            while start == 1:
                n = int(input("Please enter 0 to stop: "))
                if n == 0:
                    break
            elapsed_time_secs = time.time() - start_time
            print(f"{round(elapsed_time_secs, 4)} sec")
        except ValueError:
            print("please read carefully whatever instruction has given to you")


st = StopWatch()
st.startstopwatch()
