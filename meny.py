"""Klasser og funksjoner for et menysystem.
"""

from os import name, system
from typing import Any, Optional


_CLEAR_TERMINAL_ENABLED = False
_DEBUG_ENABLED = False


def _clear() -> None:
    """Clear the terminal screen.

    Args:

    Returns:

    Raises:
    """

    if name == "nt":
        system("clr")  # Windows
    else:
        system("clear")  # Linux, Mac


class MenyValg():
    """Representerer et menyvalg.

    Attributes:
        text: str
        function: object
        arguments: Optional[Any]
    """

    def __init__(
            self,
            text: str,
            function: object = None,
            /,
            *args: Optional[Any]):
            # /, PEP 570: pylint: disable=keyword-arg-before-vararg
            #     (https://peps.python.org/pep-0570/)
            # Er Optional[Any] riktig typing?
        self.text = text
        self.function = function
        self.arguments = args  # args er en tuple med arguments.

    # TODO(Issue l): def __str__(self) -> str:

    def run(self) -> None:
        """Kjører funksjonen til et menyvalg.

        Args:

        Returns:

        Raises:
        """

        if self.function is None:
            # TODO(Issue l): Kjør en avsluttende funksjon.
            pass
        else:
            # TODO(Issue l): Lag en try/except rundt denne.
            # DEBUG: MenyValg.run().
            if _DEBUG_ENABLED:
                print(f"DEBUG: function: {self.function}")
                print(f"DEBUG: arguments: {self.arguments}")
            # self.arguments er en tuple med arguments.
            # *self.arguments (med ledende asterix) pakker ut arguments.
            self.function(*self.arguments)


class MenyListe():
    """Representerer en menyliste.

    For å lage en ny menyliste så må vi først initialisere en tom MenyList
    og deretter bruker vi append() funksjonen for å legge til et MenyValg.

    En MenyList er et mutable objekt. Den egenskapen er viktig for
    at et MenyValg i test_meny_a skal kunne kjøre funksjonen
    test_meny_b.show() og at et MenyValg i test_meny_b skal kunne
    kjøre funksjonen test_meny_a.show().
    (Sirkulær referanse mellom to menylister, a og b.)
    (Obs! Traceback kan bli lang.)

    Attributes:
        entries: list[MenyValg]
    """

    def __init__(self):
        self.entries = []

    # TODO(Issue l): def __str__(self) -> str:

    def append(self, entry: MenyValg) -> None:
        """Legger et menyvalg til i menylisten.

        Args:

        Returns:

        Raises:
        """

        self.entries.append(entry)

    def _input(self) -> None:
        """Ber brukeren om å velge et menyvalg fra menylisten.

        Args:

        Returns:

        Raises:
        """

        # TODO(Issue l): Lag en try/except i en while loop rundt denne.
        user_input = int(
            input(f" > Skriv et tall [0-{len(self.entries) - 1}]: "))
        print(f"    > Du valgte "
              f"{self.entries[user_input].text}[{user_input}]")
        self.entries[user_input].run()

    def show(self) -> None:
        """Viser menylisten med menyvalg til brukeren.

        Args:

        Returns:

        Raises:
        """

        if _CLEAR_TERMINAL_ENABLED:
            _clear()
        print("----------------------------------------")
        for i, entry in enumerate(self.entries):
            print(f"{entry.text}[{i}]")
        print("----------------------------------------")
        self._input()


# TODO(Issue l): Fullfør docstring og diverse.
def start_meny() -> None:
    """Starter et menysystem.

    Args:

    Returns:

    Raises:
    """

    pass


# TEST: _test_meny().
def _test_meny() -> None:
    """Tester et menysystem.

    Args:

    Returns:

    Raises:
    """

    #global _CLEAR_TERMINAL_ENABLED
    #_CLEAR_TERMINAL_ENABLED = True

    #global _DEBUG_ENABLED
    #_DEBUG_ENABLED = True

    test_meny_a = MenyListe()
    test_meny_b = MenyListe()
    # DEBUG: _test_meny().
    if _DEBUG_ENABLED:
        print(f"DEBUG: id(test_meny_a): {id(test_meny_a)}")
        print(f"DEBUG: id(test_meny_b): {id(test_meny_b)}")

    test_meny_a.append(MenyValg("Valg A1.", print, "Kjører A1."))
    test_meny_a.append(MenyValg("Valg A2.", print, "Kjører A2."))
    test_meny_a.append(MenyValg("Valg A3.", print, "Kjører A3."))
    test_meny_a.append(MenyValg("Valg A4.", print, "Kjører A4."))
    test_meny_a.append(MenyValg("Meny B.", test_meny_b.show))
    test_meny_a.append(MenyValg("Avslutt."))
    # DEBUG: _test_meny().
    if _DEBUG_ENABLED:
        print(f"DEBUG: id(test_meny_a): {id(test_meny_a)}")
        print(f"DEBUG: id(test_meny_b): {id(test_meny_b)}")

    test_meny_b.append(MenyValg("Valg B1.", print, "Kjører B1."))
    test_meny_b.append(MenyValg("Valg B2.", print, "Kjører B2."))
    test_meny_b.append(MenyValg("Valg B3.", print, "Kjører B3."))
    test_meny_b.append(MenyValg("Valg B4.", print, "Kjører B4."))
    test_meny_b.append(MenyValg("Meny A.", test_meny_a.show))
    test_meny_b.append(MenyValg("Avslutt."))
    # DEBUG: _test_meny().
    if _DEBUG_ENABLED:
        print(f"DEBUG: id(test_meny_a): {id(test_meny_a)}")
        print(f"DEBUG: id(test_meny_b): {id(test_meny_b)}")

    test_meny_a.show()
    #test_meny_b.show()


if __name__ == "__main__":
    pass
    # TEST: _test_meny().
    _CLEAR_TERMINAL_ENABLED = True  # Obs!
    _DEBUG_ENABLED = False
    _test_meny()

