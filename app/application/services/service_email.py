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
            ['destinatario1@example.com', 'destinatario2@example.com'],
        )