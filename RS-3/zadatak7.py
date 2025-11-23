"""
7. Objasnite korak po korak kako se ponaša event loop (kako se raspoređuju, izvršavaju i dovršavaju
korutine te koja su njihova stanja u različitim fazama izvođenja) na sljedećem primjeru:
    import asyncio
    async def timer(name, delay):
        for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        await asyncio.sleep(1)
        print(f'{name}: Vrijeme je isteklo!')
    async def main():
        timers = [
        asyncio.create_task(timer('Timer 1', 3)),
        asyncio.create_task(timer('Timer 2', 5)),
        asyncio.create_task(timer('Timer 3', 7))
        ]
        await asyncio.gather(*timers)
    asyncio.run(main())
"""


import asyncio
import logging

# Ova korutina prvi put kad se izvršava isprinta odma broj preostalih sekundi
# Zatim dolazimo do await asyncio.sleep(1) gdje se kontrola predaje event loopu
# te se timer korutina nastavlja tek nakon 1 sekundi tj nakon što se izvrši asyncio.sleep(1)
# To ponašanje se ponavlja delay iteracija, tj dok ne prođe x sekundi.
# Na kraju se ispisuje  da je vrijeme isteklo
# Detalji izvršavanja se vide u logovima
async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        await asyncio.sleep(1)
    print(f'{name}: Vrijeme je isteklo!')

async def main():
    def log_calls(func):
        def wrapper(*args, **kwargs):
            print(f"[SCHEDULE] {func.__name__} args={args}")
            return func(*args, **kwargs)
        return wrapper

    loop = asyncio.get_event_loop()
    loop.call_soon = log_calls(loop.call_soon)
    loop.call_later = log_calls(loop.call_later)
    loop.call_at = log_calls(loop.call_at)

    # Stvaramo 3 timer taska sa asyncio.create_task funkcijom
    #
    # Taskovi se schedulaju na event loopu i kreču izvršavati 
    # Prvi task bi se trebao potpuno izvršiti nakon ~3 sekunde.
    # Drugi task nakon ~5 sekundi.
    # Treci task nakon ~7 sekundi.
    timers = [
        asyncio.create_task(timer('Timer 1', 3)),
        asyncio.create_task(timer('Timer 2', 5)),
        asyncio.create_task(timer('Timer 3', 7))
    ]
    
    # Ovdje cekamo rezoluciju svih taskovi tj ćekamo da se svi izvrše
    await asyncio.gather(*timers)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    # Entrypoint u async runtime
    # Ukoliko bi pozvali unutar postojeceg event loopa
    # dobili bi RuntimeError("asyncio.run() cannot be called from a running event loop")
    # te ukoliko main funkcija nebi bila kurutina također bi dobili error samo ovaj put
    # ValueError("a coroutine was expected, got {!r}".format(main))
    # Ukoliko je sve ok stvorit ce se novi event loop i runnat ce
    # se main() korutina do kraja.
    # Kada se glavna korutina izvrši ostali
    # taskovi koji se još trebaju izvršavati tj. pending taskovi će biti prekinuti tj "cancelani"
    # te se gasi event loop.
    # U našem slučaju se to neće dogodit jer gatheramo sve taskove
    asyncio.run(main(), debug=True)
    


"""
DEBUG LOG
DEBUG:asyncio:Using selector: EpollSelector
[SCHEDULE] call_soon args=(<TaskStepMethWrapper object at 0x78685754c460>,)  - Timer 1
[SCHEDULE] call_soon args=(<TaskStepMethWrapper object at 0x78685754c520>,)  - Timer 2
[SCHEDULE] call_soon args=(<TaskStepMethWrapper object at 0x78685754c4f0>,) - Timer 3
Timer 1: 3 sekundi preostalo... - Pozvo se Timer 1
[SCHEDULE] call_later args=(1, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None) - pozvo se asyncio.sleep u timeru 1
[SCHEDULE] call_at args=(4967.768579646, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None) - expanda se u call_at, vidimo implementaciju dolje
Timer 2: 5 sekundi preostalo... - Sve se dalje ponavlja do finishanja indvidiualnog taskanja, konačnog gathera itd itd.
[SCHEDULE] call_later args=(1, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
[SCHEDULE] call_at args=(4967.768637399, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
Timer 3: 7 sekundi preostalo...
[SCHEDULE] call_later args=(1, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
[SCHEDULE] call_at args=(4967.768685061, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
[SCHEDULE] call_soon args=(<built-in method task_wakeup of _asyncio.Task object at 0x786857d9ac20>, <Future finished result=None cb=[Task.task_wakeup()] created at /usr/lib/python3.10/asyncio/base_events.py:429>)
[SCHEDULE] call_soon args=(<built-in method task_wakeup of _asyncio.Task object at 0x786857d9b440>, <Future finished result=None cb=[Task.task_wakeup()] created at /usr/lib/python3.10/asyncio/base_events.py:429>)
[SCHEDULE] call_soon args=(<built-in method task_wakeup of _asyncio.Task object at 0x786857d9b510>, <Future finished result=None cb=[Task.task_wakeup()] created at /usr/lib/python3.10/asyncio/base_events.py:429>)
Timer 1: 2 sekundi preostalo...
[SCHEDULE] call_later args=(1, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
[SCHEDULE] call_at args=(4968.774399495, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
Timer 2: 4 sekundi preostalo...
[SCHEDULE] call_later args=(1, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
[SCHEDULE] call_at args=(4968.774757747, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
Timer 3: 6 sekundi preostalo...
[SCHEDULE] call_later args=(1, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
[SCHEDULE] call_at args=(4968.775082433, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
[SCHEDULE] call_soon args=(<built-in method task_wakeup of _asyncio.Task object at 0x786857d9ac20>, <Future finished result=None cb=[Task.task_wakeup()] created at /usr/lib/python3.10/asyncio/base_events.py:429>)
[SCHEDULE] call_soon args=(<built-in method task_wakeup of _asyncio.Task object at 0x786857d9b440>, <Future finished result=None cb=[Task.task_wakeup()] created at /usr/lib/python3.10/asyncio/base_events.py:429>)
[SCHEDULE] call_soon args=(<built-in method task_wakeup of _asyncio.Task object at 0x786857d9b510>, <Future finished result=None cb=[Task.task_wakeup()] created at /usr/lib/python3.10/asyncio/base_events.py:429>)
Timer 1: 1 sekundi preostalo...
[SCHEDULE] call_later args=(1, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
[SCHEDULE] call_at args=(4969.780728939, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
Timer 2: 3 sekundi preostalo...
[SCHEDULE] call_later args=(1, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
[SCHEDULE] call_at args=(4969.780933783, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
Timer 3: 5 sekundi preostalo...
[SCHEDULE] call_later args=(1, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
[SCHEDULE] call_at args=(4969.781132902, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
[SCHEDULE] call_soon args=(<built-in method task_wakeup of _asyncio.Task object at 0x786857d9ac20>, <Future finished result=None cb=[Task.task_wakeup()] created at /usr/lib/python3.10/asyncio/base_events.py:429>)
[SCHEDULE] call_soon args=(<built-in method task_wakeup of _asyncio.Task object at 0x786857d9b440>, <Future finished result=None cb=[Task.task_wakeup()] created at /usr/lib/python3.10/asyncio/base_events.py:429>)
[SCHEDULE] call_soon args=(<built-in method task_wakeup of _asyncio.Task object at 0x786857d9b510>, <Future finished result=None cb=[Task.task_wakeup()] created at /usr/lib/python3.10/asyncio/base_events.py:429>)
Timer 1: Vrijeme je isteklo!
[SCHEDULE] call_soon args=(<function gather.<locals>._done_callback at 0x786857543c70>, <Task finished name='Task-2' coro=<timer() done, defined at /home/spazzay/Projects/College/RS/RS-3/zadatak7.py:29> result=None cb=[gather.<locals>._done_callback() at /usr/lib/python3.10/asyncio/tasks.py:720] created at /usr/lib/python3.10/asyncio/tasks.py:337>)
Timer 2: 2 sekundi preostalo...
[SCHEDULE] call_later args=(1, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
[SCHEDULE] call_at args=(4970.786872299, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
Timer 3: 4 sekundi preostalo...
[SCHEDULE] call_later args=(1, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
[SCHEDULE] call_at args=(4970.787060984, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
[SCHEDULE] call_soon args=(<built-in method task_wakeup of _asyncio.Task object at 0x786857d9b440>, <Future finished result=None cb=[Task.task_wakeup()] created at /usr/lib/python3.10/asyncio/base_events.py:429>)
[SCHEDULE] call_soon args=(<built-in method task_wakeup of _asyncio.Task object at 0x786857d9b510>, <Future finished result=None cb=[Task.task_wakeup()] created at /usr/lib/python3.10/asyncio/base_events.py:429>)
Timer 2: 1 sekundi preostalo...
[SCHEDULE] call_later args=(1, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
[SCHEDULE] call_at args=(4971.793254473, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
Timer 3: 3 sekundi preostalo...
[SCHEDULE] call_later args=(1, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
[SCHEDULE] call_at args=(4971.7935887, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
[SCHEDULE] call_soon args=(<built-in method task_wakeup of _asyncio.Task object at 0x786857d9b440>, <Future finished result=None cb=[Task.task_wakeup()] created at /usr/lib/python3.10/asyncio/base_events.py:429>)
[SCHEDULE] call_soon args=(<built-in method task_wakeup of _asyncio.Task object at 0x786857d9b510>, <Future finished result=None cb=[Task.task_wakeup()] created at /usr/lib/python3.10/asyncio/base_events.py:429>)
Timer 2: Vrijeme je isteklo!
[SCHEDULE] call_soon args=(<function gather.<locals>._done_callback at 0x786857543c70>, <Task finished name='Task-3' coro=<timer() done, defined at /home/spazzay/Projects/College/RS/RS-3/zadatak7.py:29> result=None cb=[gather.<locals>._done_callback() at /usr/lib/python3.10/asyncio/tasks.py:720] created at /usr/lib/python3.10/asyncio/tasks.py:337>)
Timer 3: 2 sekundi preostalo...
[SCHEDULE] call_later args=(1, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
[SCHEDULE] call_at args=(4972.800145776, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
[SCHEDULE] call_soon args=(<built-in method task_wakeup of _asyncio.Task object at 0x786857d9b510>, <Future finished result=None cb=[Task.task_wakeup()] created at /usr/lib/python3.10/asyncio/base_events.py:429>)
Timer 3: 1 sekundi preostalo...
[SCHEDULE] call_later args=(1, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
[SCHEDULE] call_at args=(4973.806303259, <function _set_result_unless_cancelled at 0x786857ac2170>, <Future pending created at /usr/lib/python3.10/asyncio/base_events.py:429>, None)
[SCHEDULE] call_soon args=(<built-in method task_wakeup of _asyncio.Task object at 0x786857d9b510>, <Future finished result=None cb=[Task.task_wakeup()] created at /usr/lib/python3.10/asyncio/base_events.py:429>)
Timer 3: Vrijeme je isteklo!
[SCHEDULE] call_soon args=(<function gather.<locals>._done_callback at 0x786857543c70>, <Task finished name='Task-4' coro=<timer() done, defined at /home/spazzay/Projects/College/RS/RS-3/zadatak7.py:29> result=None cb=[gather.<locals>._done_callback() at /usr/lib/python3.10/asyncio/tasks.py:720] created at /usr/lib/python3.10/asyncio/tasks.py:337>)
[SCHEDULE] call_soon args=(<built-in method task_wakeup of _asyncio.Task object at 0x786857f72190>, <_GatheringFuture finished result=[None, None, None] cb=[Task.task_wakeup()] created at /usr/lib/python3.10/asyncio/tasks.py:665>) - Ovdje nam se zavrsio gather
[SCHEDULE] call_soon args=(<function _run_until_complete_cb at 0x786857b4ab00>, <Task finished name='Task-1' coro=<main() done, defined at /home/spazzay/Projects/College/RS/RS-3/zadatak7.py:35> result=None cb=[_run_until_complete_cb() at /usr/lib/python3.10/asyncio/base_events.py:184] created at /usr/lib/python3.10/asyncio/tasks.py:636>)
[SCHEDULE] call_soon args=(<TaskStepMethWrapper object at 0x78685754c490>,)
[SCHEDULE] call_soon args=(<function _run_until_complete_cb at 0x786857b4ab00>, <Task finished name='Task-5' coro=<BaseEventLoop.shutdown_asyncgens() done, defined at /usr/lib/python3.10/asyncio/base_events.py:535> result=None cb=[_run_until_complete_cb() at /usr/lib/python3.10/asyncio/base_events.py:184] created at /usr/lib/python3.10/asyncio/tasks.py:636>)
[SCHEDULE] call_soon args=(<TaskStepMethWrapper object at 0x78685754c5b0>,)
[SCHEDULE] call_soon args=(<function _run_until_complete_cb at 0x786857b4ab00>, <Task finished name='Task-6' coro=<BaseEventLoop.shutdown_default_executor() done, defined at /usr/lib/python3.10/asyncio/base_events.py:560> result=None cb=[_run_until_complete_cb() at /usr/lib/python3.10/asyncio/base_events.py:184] created at /usr/lib/python3.10/asyncio/tasks.py:636>)
DEBUG:asyncio:Close <_UnixSelectorEventLoop running=False closed=False debug=True>
"""

"""
def call_later(self, delay, callback, *args, context=None):
    # Arrange for a callback to be called at a given time.

    # Return a Handle: an opaque object with a cancel() method that
    # can be used to cancel the call.

    # The delay can be an int or float, expressed in seconds.  It is
    # always relative to the current time.

    # Each callback will be called exactly once.  If two callbacks
    # are scheduled for exactly the same time, it undefined which
    # will be called first.

    # Any positional arguments after the callback will be passed to
    # the callback when it is called.
    
    timer = self.call_at(self.time() + delay, callback, *args,
                            context=context)
    if timer._source_traceback:
        del timer._source_traceback[-1]
    return timer
"""