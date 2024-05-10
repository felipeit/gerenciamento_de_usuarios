from django.core.mail import send_mail

from app.domain.events.dto import GenericEvent


class SendEmailResetPasswordHandler:
    supported_events: list[str] = ["reset-password"]

    def run(self, event: GenericEvent) -> None:
        send_mail(
            'Reset de senha',
            f"""
                Sr(a) {event.data.email}, sua nova senha é: {event.data.password}

                att,
                    IT support
            """,
            'remetente@example.com',
            [event.data.email],
        )

class SendEmailNewUserHandler:
    supported_events: list[str] = ["new-user"]

    def run(self, event: GenericEvent) -> None:
        send_mail(
            'Seja bem vindo!',
            f"""
                Sr(a) {event.data.email}, sua senha é: {event.data.password}

                att,
                    IT support
            """,
            'remetente@example.com',
            [event.data.email],
        )