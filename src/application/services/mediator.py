from typing import Any, Callable

from src.domain.events.dto import GenericEvent
from src.infra.repository.user_repository import UserRepository



class InMemoryMediator:
    def __init__(self, repo: UserRepository = UserRepository()) -> None:
        self._handlers: list[Any] = []
        self._repo = repo

    def send(self, *event: GenericEvent) -> None:
        try:
            for e in event:
                for handler in self._handlers:
                    user = self._repo.get_user_for_email(email=e.data.email)
                    if e.key not in handler.supported_events:
                        continue
                    if e.key == 'reset-password' and not user:
                        continue
                    handler.run(e)
        except AttributeError:
            pass

    def add_handler(self, handler: Any) -> None:
        if handler not in self._handlers:
            self._handlers.append(handler)

class Dispatch:
    def __init__(self, *handlers, mediator=InMemoryMediator()) -> None:
        self.handlers = handlers
        self.mediator = mediator
        self.__include_handlers()

    def __include_handlers(self) -> None:
        for handler in self.handlers:
            self.mediator.add_handler(handler)

    def __call__(self, usecase_method: Callable, *args: Any, **kwargs: Any) -> Any:
        def inner(usecase, input, *args, **kwargs) -> Any:
            self.mediator.send(GenericEvent(key=input.events, data=input))
            output = usecase_method(usecase, input)
            self.mediator.send(output)
            return output
        return inner