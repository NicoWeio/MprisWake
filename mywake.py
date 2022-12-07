from contextlib import contextmanager

import dbus

bus = dbus.SessionBus()
obj = bus.get_object('org.freedesktop.PowerManagement.Inhibit',
                     '/org/freedesktop/PowerManagement/Inhibit')
inhibitMethod = obj.get_dbus_method('Inhibit', 'org.freedesktop.PowerManagement.Inhibit')
unInhibitMethod = obj.get_dbus_method('UnInhibit', 'org.freedesktop.PowerManagement.Inhibit')


@contextmanager
def inhibit(application, reason):
    cookie = inhibitMethod(application, reason)
    try:
        yield cookie
    finally:
        unInhibitMethod(cookie)
