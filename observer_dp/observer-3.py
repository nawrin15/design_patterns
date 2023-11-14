from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def registerObserver(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def unresgisterObserver(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notifyObserver(self, msg) -> None:
        """
        Notify all observers about an event.
        """
        pass


class YoutubeChannel1(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """
    _state: int = None
    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """
    def registerObserver(self, observer: Observer) -> None:
        self._observers.append(observer)

    def unresgisterObserver(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """
    def notifyObserver(self, msg) -> None:
        """
        Trigger an update in each subscriber.
        """
        for observer in self._observers:
            observer.update(msg)

    def newVideoAdded(self, msg) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """
        self.notifyObserver(msg)



class YoutubeChannel2(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """
    _state: int = None
    _observers: List[Observer] = []
    
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """
    def registerObserver(self, observer: Observer) -> None:
        self._observers.append(observer)
    
    def unresgisterObserver(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """
    def notifyObserver(self, msg) -> None:
        """
        Trigger an update in each subscriber.
        """
        for observer in self._observers:
            observer.update(msg)

    def newVideoAdded(self, msg) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """
        self.notifyObserver(msg)


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, msg) -> None:
        """
        Receive update from subject.
        """
        pass


"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.
"""
class User1(Observer):
    def update(self, msg) -> None:
        print("User 1 " + msg)

class User2(Observer):
    def update(self, msg) -> None:
        print("User 2 " + msg)
        
class User3(Observer):
    def update(self, msg) -> None:
        print("User 3 " + msg)


if __name__ == "__main__":
    # The client code.

    youtubeChannel1 = YoutubeChannel1()
    youtubeChannel2 = YoutubeChannel2()

    user1 = User1()
    user2 = User2()
    user3 = User3()

    youtubeChannel1.registerObserver(user1)
    youtubeChannel1.registerObserver(user2)
    
    youtubeChannel2.registerObserver(user1)
    youtubeChannel2.registerObserver(user2)
    youtubeChannel2.registerObserver(user3)

    
    youtubeChannel1.newVideoAdded("video 1 is added in channel 1")
    youtubeChannel2.newVideoAdded("video 2 is added in channel 2")