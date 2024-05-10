from typing import Any, Callable

from app.domain.events.dto import GenericEvent
from app.infra.repository.user_repository import UserRepository



class InMemoryMediator:
    def __init__(self) -> None:
        self._handlers: list[Any] = []

    def send(self, *event: GenericEvent) -> None:
        try:
            for e in event:
                for handler in self._handlers:
                    if e.key not in handler.supported_events:
                        continue
                    handler.run(e)
        except AttributeError:
            pass

    def add_handler(self, handler: Any) -> None:
        if handler not in self._handlers:
            self._handlers.append(handler)

class Dispatch:
    def __init__(self, *handlers, mediator=InMemoryMediator(), repo: UserRepository = UserRepository()) -> None:
        self.handlers = handlers
        self.mediator = mediator
        self.__include_handlers()
        self._repo = repo

    def __include_handlers(self) -> None:
        for handler in self.handlers:
            self.mediator.add_handler(handler)

    def __call__(self, usecase_method: Callable, *args: Any, **kwargs: Any) -> Any:
        def inner(usecase, input, *args, **kwargs) -> Any:
            user = self._repo.get_user_for_email(email=input.email)
            if user:
                self.mediator.send(GenericEvent(key="reset-password", data=input))
                output = usecase_method(usecase, input)
                self.mediator.send(output)
                return output
            return user
        return inner