import gi
from gi.repository import Gio

from muchnotify import config
from muchnotify.messages import Messages

gi.require_version("Gio", "2.0")

__all__ = ["show_notification"]


Application = Gio.Application.new("notify.much", Gio.ApplicationFlags.FLAGS_NONE)
Application.register()


def show_notification():
    """If a notification is open already, asks it to update itself and returns
    immediately. Otherwise opens a notification and blocks until it is
    closed."""
    config.load()
    messages = Messages()
    summary = messages.unseen_summary()
    if summary:
        Notification = Gio.Notification.new(
            "{count} unread messages".format(count=messages.count())
        )
        Notification.set_body(summary)
        Application.send_notification(None, Notification)
